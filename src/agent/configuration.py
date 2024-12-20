import os
from dataclasses import dataclass, fields
from typing import Any, Optional

from langchain_core.runnables import RunnableConfig
from dataclasses import dataclass

DEFAULT_BLOG_STRUCTURE = """The blog post should follow this strict three-part structure:

1. Introduction (max 1 section)
   - Start with ### Key Links and include user-provided links  
   - Brief overview of the problem statement
   - Brief overview of the solution/main topic
   - Maximum 100 words

2. Main Body (exactly 2-3 sections)
    - Each section must:
      * Cover a distinct aspect of the main topic
      * Include at least one relevant code snippet
      * Be 150-200 words
    - No overlap between sections

3. Conclusion (max 1 section)
   - Brief summary of key points
   - Key Links
   - Clear call to action
   - Maximum 150 words"""

@dataclass(kw_only=True)
class Configuration:
    """The configurable fields for the chatbot."""
    blog_structure: str = DEFAULT_BLOG_STRUCTURE
    
    @classmethod
    def from_runnable_config(
        cls, config: Optional[RunnableConfig] = None
    ) -> "Configuration":
        """Create a Configuration instance from a RunnableConfig."""
        configurable = (
            config["configurable"] if config and "configurable" in config else {}
        )
        values: dict[str, Any] = {
            f.name: os.environ.get(f.name.upper(), configurable.get(f.name))
            for f in fields(cls)
            if f.init
        }
        return cls(**{k: v for k, v in values.items() if v})