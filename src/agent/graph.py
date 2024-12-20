from langchain_anthropic import ChatAnthropic 
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.runnables import RunnableConfig

from langgraph.constants import Send
from langgraph.graph import START, END, StateGraph

import agent.configuration as configuration
from agent.state import Sections, BlogState, BlogStateInput, BlogStateOutput, SectionState
from agent.prompts import blog_planner_instructions, main_body_section_writer_instructions, intro_conclusion_instructions
from agent.utils import load_and_format_urls, read_dictation_file, format_sections

# ------------------------------------------------------------
# LLMs 
claude_3_5_sonnet = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0) 

# ------------------------------------------------------------
# Graph
def generate_blog_plan(state: BlogState, config: RunnableConfig):
    """ Generate the report plan """

    # Read transcribed notes
    user_instructions = read_dictation_file(state.transcribed_notes_file)

    # Get configuration
    configurable = configuration.Configuration.from_runnable_config(config)
    blog_structure = configurable.blog_structure

    # Format system instructions
    system_instructions_sections = blog_planner_instructions.format(user_instructions=user_instructions, blog_structure=blog_structure)

    # Generate sections 
    structured_llm = claude_3_5_sonnet.with_structured_output(Sections)
    report_sections = structured_llm.invoke([SystemMessage(content=system_instructions_sections)]+[HumanMessage(content="Generate the sections of the blog. Your response must include a 'sections' field containing a list of sections. Each section must have: name, description, and content fields.")])

    return {"sections": report_sections.sections}

def write_section(state: SectionState):
    """ Write a section of the report """

    # Get state 
    section = state.section
    urls = state.urls

    # Read transcribed notes
    user_instructions = read_dictation_file(state.transcribed_notes_file)

    # Load and format urls
    url_source_str = "" if not urls else load_and_format_urls(urls)

    # Format system instructions
    system_instructions = main_body_section_writer_instructions.format(section_name=section.name, 
                                                                       section_topic=section.description, 
                                                                       user_instructions=user_instructions, 
                                                                       source_urls=url_source_str)

    # Generate section  
    section_content = claude_3_5_sonnet.invoke([SystemMessage(content=system_instructions)]+[HumanMessage(content="Generate a blog section based on the provided information.")])
    
    # Write content to the section object  
    section.content = section_content.content

    # Write the updated section to completed sections
    return {"completed_sections": [section]}

def write_final_sections(state: SectionState):
    """ Write final sections of the report, which do not require web search and use the completed sections as context """

    # Get state 
    section = state.section
    
    # Format system instructions
    system_instructions = intro_conclusion_instructions.format(section_name=section.name, 
                                                               section_topic=section.description, 
                                                               main_body_sections=state.blog_main_body_sections, 
                                                               source_urls=state.urls)

    # Generate section  
    section_content = claude_3_5_sonnet.invoke([SystemMessage(content=system_instructions)]+[HumanMessage(content="Generate an intro/conclusion section based on the provided main body sections.")])
    
    # Write content to section 
    section.content = section_content.content

    # Write the updated section to completed sections
    return {"completed_sections": [section]}

def initiate_section_writing(state: BlogState):
    """ This is the "map" step when we kick off web research for some sections of the report """    
        
    # Kick off section writing in parallel via Send() API for any sections that require research
    return [
        Send("write_section", SectionState(
            section=s,
            transcribed_notes_file=state.transcribed_notes_file,
            urls=state.urls,
            completed_sections=[]  # Initialize with empty list
        )) 
        for s in state.sections 
        if s.main_body
    ]

def gather_completed_sections(state: BlogState):
    """ Gather completed main body sections"""    

    # List of completed sections
    completed_sections = state.completed_sections

    # Format completed section to str to use as context for final sections
    completed_report_sections = format_sections(completed_sections)

    return {"blog_main_body_sections": completed_report_sections}

def initiate_final_section_writing(state: BlogState):
    """ This is the "map" step when we kick off research on any sections that require it using the Send API """    

    # Kick off section writing in parallel via Send() API for any sections that do not require research
    return [
        Send("write_final_sections", SectionState(
            section=s,
            blog_main_body_sections=state.blog_main_body_sections,
            urls=state.urls,
            completed_sections=[]  # Initialize with empty list
        )) 
        for s in state.sections 
        if not s.main_body
    ]

def compile_final_blog(state: BlogState):
    """ Compile the final blog """    

    # Get sections
    sections = state.sections
    completed_sections = {s.name: s.content for s in state.completed_sections}

    # Update sections with completed content while maintaining original order
    for section in sections:
        section.content = completed_sections[section.name]

    # Compile final report
    all_sections = "\n\n".join([s.content for s in sections])

    return {"final_blog": all_sections}

# Add nodes and edges 
builder = StateGraph(BlogState, input=BlogStateInput, output=BlogStateOutput, config_schema=configuration.Configuration)
builder.add_node("generate_blog_plan", generate_blog_plan)
builder.add_node("write_section", write_section)
builder.add_node("compile_final_blog", compile_final_blog)
builder.add_node("gather_completed_sections", gather_completed_sections)
builder.add_node("write_final_sections", write_final_sections)
builder.add_edge(START, "generate_blog_plan")
builder.add_conditional_edges("generate_blog_plan", initiate_section_writing, ["write_section"])
builder.add_edge("write_section", "gather_completed_sections")
builder.add_conditional_edges("gather_completed_sections", initiate_final_section_writing, ["write_final_sections"])
builder.add_edge("write_final_sections", "compile_final_blog")
builder.add_edge("compile_final_blog", END)

graph = builder.compile() 
