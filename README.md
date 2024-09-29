# MultiPDF Chat App

## Introduction

The MultiPDF Chat App is a Python application that allows you to chat with multiple PDF documents. You can ask questions about the PDFs using natural language, and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the loaded PDFs.

## How It Works

![PDF-LangChain](https://github.com/user-attachments/assets/baa7ed44-1e4e-4626-9348-7da5c12bcc41)

The application follows these steps to provide responses to your questions:

1. **PDF Loading**: The app reads multiple PDF documents and extracts their text content.
2. **Text Chunking**: The extracted text is divided into smaller chunks that can be processed effectively.
3. **Language Model**: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.
4. **Similarity Matching**: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.
5. **Response Generation**: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

## Dependencies and Installation

To install the MultiPDF Chat App, please follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command:
      pip install -r requirements.txt
3. Obtain an API key from OpenAI and add it to the .env file in the project directory

## Usage

To use the MultiPDF Chat App, follow these steps: 
- Ensure that you have installed the required dependencies and added the OpenAI API key to the .env file.
- Run the app.py file using the Streamlit CLI. Execute the following command: streamlit run app.py
- The application will launch in your default web browser, displaying the user interface.
- Load multiple PDF documents into the app by following the provided instructions.
- Ask questions in natural language about the loaded PDFs using the chat interface.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and improvements are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.


    

   
