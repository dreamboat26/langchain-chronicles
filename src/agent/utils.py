import os
from langchain_community.document_loaders import WebBaseLoader
from agent.state import Section

def load_and_format_urls(url_list):
    """Load web pages from URLs and format them into a readable string.
    
    Args:
        url_list (str or list): Single URL or list of URLs to load and format
        
    Returns:
        str: Formatted string containing metadata and content from all loaded documents,
             separated by '---' delimiters. Each document includes:
             - Title
             - Source URL
             - Description
             - Page content
    """

    # Clean and normalize the input URLs
    if not isinstance(url_list, list):
        raise ValueError("url_list must be a list of strings")
    
    # Clean each URL in the list
    urls = [url.strip() for url in url_list if url.strip()]

    loader = WebBaseLoader(urls)
    docs = loader.load()

    formatted_docs = []
    
    for doc in docs:
        # Format metadata
        metadata_str = (
            f"Title: {doc.metadata.get('title', 'N/A')}\n"
            f"Source: {doc.metadata.get('source', 'N/A')}\n"
            f"Description: {doc.metadata.get('description', 'N/A')}\n"
        )
        
        # Format content (strip extra whitespace and newlines)
        content = doc.page_content.strip()
        
        # Combine metadata and content
        formatted_doc = f"---\n{metadata_str}\nContent:\n{content}\n---"
        formatted_docs.append(formatted_doc)
    
    # Join all documents with double newlines
    return "\n\n".join(formatted_docs)

def read_dictation_file(file_path: str) -> str:
    """Read content from a text file audio-to-text dictation."""
    try:
        # Try to get directory from __file__ (for module imports)
        current_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        # Fallback for Jupyter notebooks
        current_dir = os.getcwd()
    notes_dir = os.path.join(current_dir, "notes")
    absolute_path = os.path.join(notes_dir, file_path)
    print(f"Reading file from {absolute_path}")
    try:
        with open(absolute_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Warning: File not found at {absolute_path}")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""
    
def format_sections(sections: list[Section]) -> str:
    """ Format a list of sections into a string """
    formatted_str = ""
    for idx, section in enumerate(sections, 1):
        formatted_str += f"""
{'='*60}
Section {idx}: {section.name}
{'='*60}
Description:
{section.description}
Main body: 
{section.main_body}
Content:
{section.content if section.content else '[Not yet written]'}
"""