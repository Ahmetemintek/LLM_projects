import streamlit as st
from openai import OpenAI
import os
from llama_index.core import VectorStoreIndex
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import Settings
from llama_index.embeddings.openai import OpenAIEmbedding

from dotenv import load_dotenv
load_dotenv()

# Set up the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set up the embedding model
embed_model = OpenAIEmbedding(api_key=os.getenv("OPENAI_API_KEY"))
Settings.embed_model = embed_model

# Function to extract details from a webpage and create an index
def extract_webpage_details(url):
    documents = SimpleWebPageReader(html_to_text=True).load_data([url])
    index = VectorStoreIndex.from_documents(documents)
    return index

# Function to generate content based on the index and a prompt
def generate_content(index, prompt, chat_history):
    # Retrieve relevant chunks from the index
    retriever = index.as_retriever(similarity_top_k=3)
    nodes = retriever.retrieve(prompt)
    
    # Prepare the context from retrieved nodes
    context = "\n".join([node.node.text for node in nodes])
    
    # Prepare chat history for the API call
    messages = [
        {"role": "system", "content": "You are a helpful assistant that answers questions based on the given context."},
        {"role": "user", "content": f"Context: {context}\n\nRemember this context for our conversation."}
    ]
    
    # Add chat history
    messages.extend(chat_history)
    
    # Add the new user message
    messages.append({"role": "user", "content": prompt})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )
    
    return response.choices[0].message.content

def main():
    st.set_page_config(page_title="Webpage Chat", page_icon="💬")
    
    st.title("💬 Webpage Chat")
    st.markdown("### 🌐 Chat about any webpage using OpenAI!")

    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    url = st.text_input("🔗 Enter the URL of the webpage:")

    try:
        if url:
            with st.spinner("🔍 Indexing webpage..."):
                index = extract_webpage_details(url)
                st.session_state.index = index
                st.success("✅ Webpage indexed successfully!")

        # Display chat history
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if prompt := st.chat_input("💬 Enter your message:"):
            # Display user message
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate and display assistant response
            if 'index' in st.session_state:
                with st.chat_message("assistant"):
                    with st.spinner("🤔 Thinking..."):
                        response = generate_content(st.session_state.index, prompt, st.session_state.chat_history)
                        st.markdown(response)

                # Update chat history
                st.session_state.chat_history.append({"role": "user", "content": prompt})
                st.session_state.chat_history.append({"role": "assistant", "content": response})
            else:
                st.warning("⚠️ Please index a webpage first.")

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()