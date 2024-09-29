# MySQL Python Chatbot with GPT-4 and Mistral AI

Welcome to the GitHub repository for our tutorial on building a natural language SQL chatbot using GPT-4! This project guides you through the development of a chatbot that can interpret natural language queries, generate SQL queries, and fetch results from a SQL database, all in an intuitive and user-friendly way. It utilizes the power of OpenAI's GPT-4 model, integrated with a Streamlit GUI for an enhanced interaction experience.

## Features

- **Natural Language Processing**: Uses GPT-4 to interpret and respond to user queries in natural language.
- **SQL Query Generation**: Dynamically generates SQL queries based on the user's natural language input.
- **Database Interaction**: Connects to a SQL database to retrieve query results, demonstrating practical database interaction.
- **Streamlit GUI**: Features a user-friendly interface built with Streamlit, making it easy for users of all skill levels.
- **Python-based**: Entirely coded in Python, showcasing best practices in software development with modern technologies.

## Brief Explanation of How the Chatbot Works

The chatbot works by taking a user's natural language query, converting it into a SQL query using GPT-4, executing the query on a SQL database, and then presenting the results back to the user in natural language. This process involves several steps of data processing and interaction with the OpenAI API and a SQL database, all seamlessly integrated into a Streamlit application.

For a better understanding, refer to the architecture diagram below:
![mysql-chains](https://github.com/user-attachments/assets/4f7e480d-5253-48d8-90cb-880b8d2b43dd)

## Installation 
- Ensure you have Python installed on your machine. Then clone this repository.
- Install the required packages: pip install -r requirements.txt
- Create your own .env file with the necessary variables, including your OpenAI API key: OPENAI_API_KEY=[your-openai-api-key]

## Usage

To launch the Streamlit app and interact with the chatbot:streamlit run app.py

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements 
Alejandro AO for his youtube tutorial



