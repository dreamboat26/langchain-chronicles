# Langchain Chat-CSV with OpenAI

This is a Python application that allows you to load a CSV file and ask questions about its contents using natural language. The application leverages Language Models (LLMs) to generate responses based on the CSV data, ensuring that answers are relevant to the information present in the CSV.

## How It Works

The application reads the CSV file and processes the data using OpenAI LLMs alongside Langchain Agents. The CSV agent utilizes tools to find answers to your questions and generates appropriate responses with the help of the LLM.

### Features
- Load CSV files and query their contents.
- Natural language interaction with the data.
- Built with Streamlit for an intuitive user interface.
- Uses Langchain to facilitate LLM interactions.

## Installation

To install the repository, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies by running: pip install -r requirements.txt
3. Obtain an OpenAI API key and add it to the .env file.

## Usage

To use the application, execute the main.py file using the Streamlit CLI. Ensure you have Streamlit installed before running the application. Use the following command in your terminal: streamlit run main.py

## Acknowledgements 
Alejandro AO for his youtube tutorial

