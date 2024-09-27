# Local RAG Agent with LLaMA3

This repository implements a Local Retrieval-Augmented Generation (RAG) agent using LLaMA3 and various adaptive retrieval techniques. The agent is designed to intelligently route questions, perform fallback searches, and self-correct responses.

## Overview

The Local RAG Agent combines several key ideas from recent research papers on RAG:
- **Routing:** Adaptively routes questions to appropriate retrieval methods.
- **Fallback:** Uses web search when the retrieved documents are deemed irrelevant.
- **Self-correction:** Assesses and corrects answers to minimize hallucinations.

## Components

### Models

- **LLM:** Uses [Ollama](https://ollama.com) with `llama3.2:3b-instruct-fp16`.
- **Embeddings:** Utilizes [GPT4All Embeddings](https://github.com/Nomic-AI/gpt4all) with LangChain.

### Retrieval

- **Search Engine:** Integrated with [Tavily](https://tavily.com) for optimized web search.

### Tracing 

- Utilizes [LangSmith](https://langsmith.com) for tracing execution.

### Vector Store

- Implements a local vector store using [SKLearnVectorStore](https://github.com/LangchainAI/langchain).

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
