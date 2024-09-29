# LangChain Chatbot with Streamlit GUI

Welcome to the GitHub repository for the LangChain Chatbot with Streamlit GUI! This project is a comprehensive guide to building a chatbot capable of interacting with websites, extracting information, and communicating in a user-friendly manner. It leverages the power of LangChain 0.1.0 and integrates it with a Streamlit GUI for an enhanced user experience.

## Features

- **Website Interaction**: The chatbot uses the latest version of LangChain to interact with and extract information from various websites.
- **Large Language Model Integration**: Compatibility with models like GPT-4, Mistral, Llama2, and Ollama. In this code, GPT-4 is used, but you can change it to any other model.
- **Streamlit GUI**: A clean and intuitive user interface built with Streamlit, making it accessible for users with varying levels of technical expertise.
- **Python-based**: Entirely coded in Python.

## Brief Explanation of RAG

A RAG bot stands for Retrieval-Augmented Generation. This means we augment the knowledge of our LLM with new information that we pass in our prompt. We first vectorize all the text that we want to use as "augmented knowledge" and then look through the vectorized text to find the most similar text to our prompt. We then pass this text to our LLM as a prefix.

For a clearer understanding, refer to the YouTube video tutorial, and see the diagram below that illustrates the process:

![RAG Diagram](path_to_your_diagram_image) <!-- Replace with the actual path to your diagram image -->

## Installation

- Ensure you have Python installed on your system. Then clone this repository.
- pip install -r requirements.txt
- OPENAI_API_KEY=[your-openai-api-key]

## Usage
To run the Streamlit app: streamlit run app.py

## Contributing

This repository is meant as supporting material for the YouTube video tutorial. Therefore, I am not accepting any pull requests unless they are for fixing bugs or typos.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments :  
- LangChain for providing the framework.
- Streamlit for creating the user-friendly interface.
- Alejandro AO
 
