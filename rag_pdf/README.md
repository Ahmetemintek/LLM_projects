# RAG PDF Question Answering App

This Streamlit application allows users to upload PDF documents and ask questions about their content using RAG (Retrieval-Augmented Generation) and OpenAI's language models.

## Features

- PDF document upload
- Question answering based on uploaded documents
- Utilizes OpenAI's API for natural language processing
- Built with Streamlit for an interactive web interface

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```

## Usage

1. Upload a PDF file
2. Enter your question in the text input
3. Click "Ask" to get an answer based on the document content

## Technologies

- Streamlit
- OpenAI API
- LlamaIndex
- PyPDF2
