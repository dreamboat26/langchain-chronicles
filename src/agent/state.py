import operator
from dataclasses import dataclass, field
from pydantic import BaseModel, Field
from typing_extensions import Annotated, List

class Section(BaseModel):
    name: str = Field(
        description="Name for this section of the report.",
    )
    description: str = Field(
        description="Brief overview of the main topics and concepts to be covered in this section.",
    )
    content: str = Field(
        description="The content of the section."
    )   
    main_body: bool = Field(
        description="Whether this is a main body section."
    )   

class Sections(BaseModel):
    sections: List[Section] = Field(
        description="Sections of the report.",
    )

@dataclass(kw_only=True)
class BlogState:
    transcribed_notes_file: str   
    urls: List[str] = field(default_factory=list) # List of urls     
    sections: list[Section] = field(default_factory=list) 
    completed_sections: Annotated[list, operator.add] # Send() API key
    blog_main_body_sections: str = field(default=None) # Main body sections from research
    final_blog: str = field(default=None) # Final report
    
@dataclass(kw_only=True)
class BlogStateInput:
    transcribed_notes_file: str # Blog notes
    urls: List[str] = field(default_factory=list) # List of urls     

@dataclass(kw_only=True)
class BlogStateOutput:
    final_blog: str = field(default=None) # Final report

@dataclass(kw_only=True)
class SectionState:
    section: Section # Report section   
    transcribed_notes_file: str = field(default=None) 
    urls: List[str] = field(default_factory=list) # List of urls 
    blog_main_body_sections: str = field(default=None) # Main body sections from research
    completed_sections: list[Section] = field(default_factory=list) # Final key we duplicate in outer state for Send() API
    
@dataclass(kw_only=True)
class SectionOutputState:
    completed_sections: list[Section] = field(default_factory=list) # Final key we duplicate in outer state for Send() API