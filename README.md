# Robo Blogger

Creating polished blog posts is traditionally time-consuming and challenging. The gap between having great ideas and turning them into well-structured content can be significant. Robo Blogger addresses this challenge by transforming the content creation process. The key insight is that our best ideas often come when we're away from the keyboard - while walking, commuting, or right after a meeting. Robo Blogger leverages this by:

1. **Capturing Ideas Naturally**: Instead of starting with writing, [simply speak your thoughts using any voice-to-text app](https://hamel.dev/blog/posts/audience/#build-a-voice-to-content-pipeline)
2. **Maintaining Structure**: Convert raw ideas into polished content while following proven blog post patterns
3. **Grounding in Documentation**: Optionally incorporate reference materials to ensure accuracy and depth

The workflow is streamlined to three steps:
1. **Voice Capture**: Record your thoughts using any dictation app (e.g., Flowvoice)
2. **Planning**: Claude 3.5 Sonnet converts your dictation and structure into a coherent plan
3. **Writing**: Automated generation of each blog section following the plan, using your dictation and any documentation links

This approach builds on concepts from our previous [Report mAIstro](https://github.com/langchain-ai/report-mAIstro) project, but specifically optimized for blog post creation. By separating idea capture from content structuring, Robo Blogger helps maintain the authenticity of your original thoughts while ensuring professional presentation.

![robo-blogger](https://github.com/user-attachments/assets/0599ebc3-bcd7-4a1f-abe5-07ee4e828ec8)

## Quickstart

Set API keys for the LLM of choice (default is Anthropic Claude 3.5 Sonnet):
```
cp .env.example .env
```

Clone the repository and launch the assistant [using the LangGraph server](https://langchain-ai.github.io/langgraph/cloud/reference/cli/#dev):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone https://github.com/langchain-ai/robo-blogger.git
cd robo-blogger
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev
```

This will open LangGraph Studio in your browser. 

### Required Input

The only required input is the name of the audio dictation file (e.g., `audio_dictation.txt` in `notes` folder). You can use any audio-to-voice dictation app (e.g., [Flowvoice](https://www.flowvoice.ai/)) to create this file. 
```
notes/audio_dictation.txt
```

![Screenshot 2024-12-16 at 4 53 37 PM](https://github.com/user-attachments/assets/de7acd1f-9ee3-49f5-8aef-26bcda8ae479)

### Optional Inputs

Two additional inputs are optional: 
1. A list of URLs to documentation that you want to use to help write the blog post.
2. A template for the blog post structure.

![Screenshot 2024-12-16 at 3 20 10 PM](https://github.com/user-attachments/assets/8903f08c-eba0-4abc-b5a6-8bd3eff8fe9a)

In the `configuration` tab, you can provide template for the blog post structure (see ## Customization below for examples).

![Screenshot 2024-12-16 at 4 45 12 PM](https://github.com/user-attachments/assets/1712c440-68c0-4655-bd5f-8078fbfa125e)

## Customization

We've found that blog posts typically follow a consistent structure. For example, we have:

* Product update: https://blog.langchain.dev/langgraph-cloud/
* Perspective: https://blog.langchain.dev/what-is-an-agent/

Templates for different types of blog posts can be passed in as a configuration option. 

### Product Update Example

URLs provided: 
* "https://langchain-ai.github.io/langgraph/concepts/", 
* "https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/",
* "https://langchain-ai.github.io/langgraph/concepts/deployment_options/"

Blog structure provided: 
* [`examples/product_update/template.txt`](examples/product_update/template.txt)

Audio dictation provided: 
* [`notes/langgraph_cloud.txt`](notes/langgraph_cloud.txt)

Resulting blog post: 
* [`examples/product_update/langgraph_update.md`](examples/product_update/langgraph_update.md)

### Perspective Example

URLs provided: 
* "https://langchain-ai.github.io/langgraph/concepts/high_level/", 
* "https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/",
* "https://www.deeplearning.ai/the-batch/issue-253/"

Blog structure provided: 
* [`examples/perspective/template.txt`](examples/perspective/template.txt)

Audio dictation provided: 
* [`notes/agents.txt`](notes/agents.txt)

Resulting blog post: 
* [`examples/perspective/agents.md`](examples/perspective/agents.md)
