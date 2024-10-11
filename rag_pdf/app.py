import streamlit as st
from openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import Settings
from llama_index.core import Document
from llama_index.readers.file import PDFReader
from llama_index.llms.openai import OpenAI
import tempfile
import os

from dotenv import load_dotenv
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Setting up the LLM
llm = OpenAI(
    model="gpt-3.5-turbo",
    system_prompt="""You are an AI assistant helping with questions about documents. 
    If the question is not related to the document, you say 'It seems like your question is not related to the document.'
    If the correct answer is not found in the document, you say 'The answer is not present in the document.' """,
    temperature=0.5
)
Settings.llm = llm



def load_pdf_index(uploaded_file):
    """
    Load the PDF index from the uploaded file
    """
    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            # Write the contents of the uploaded file to the temporary file
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name

        # Use the temporary file path with SimpleDirectoryReader
        reader = SimpleDirectoryReader(input_files=[tmp_file_path]).load_data()
        index = VectorStoreIndex.from_documents(reader)

        # Remove the temporary file
        os.unlink(tmp_file_path)

        return index
    
    except Exception as e:
        st.error(f"Error loading PDF index: {e}")
        return None


def get_response_from_query(index, query):
    """
    Get the response from the query
    """
    query_engine= index.as_query_engine()
    response= query_engine.query(query)
    return response


def main():
    """
    Main function to run the app
    """
    
    st.title("Chat your PDF 📄💬")
    st.header("Chat your PDF with OpenAI")

    with st.sidebar:
        with st.expander("About this app"):
            st.write("This app allows you to chat with a PDF file using OpenAI and LlamaIndex.")

        
        uploaded_file= st.file_uploader("Upload your PDF file here...", type="pdf")

        if uploaded_file:
            index= load_pdf_index(uploaded_file)

            if index:
                st.success("File loaded successfully")

    user_input= st.text_input("", placeholder="Please enter your question here...")

    if user_input:
        response= get_response_from_query(index, user_input)
        st.write(response.response)


if __name__ == "__main__":
    main()










