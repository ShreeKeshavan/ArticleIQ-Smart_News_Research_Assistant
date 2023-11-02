# Import necessary libraries
import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQAWithSourcesChain
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Streamlit interface
st.markdown("## ArticleIQ - Smart News Research Assistant 🔍")

# Set up sidebar for URL inputs
st.sidebar.title("Articles URLs 👇")
urls = []
# Collect up to 3 URLs from the user
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

# Set up "Activate ArticleIQ" button
activate_articleiq = st.sidebar.button("Activate ArticleIQ")
# Set path for FAISS Vector Data pickle file
file_path = 'FAISS_Vector_Data.pkl'

# Create an empty Streamlit container for status display
status_display = st.empty()
# Initialize OpenAI model
llm = OpenAI(temperature = 0.9, max_tokens = 500)

# If "Activate ArticleIQ" button is clicked
if activate_articleiq:
    # Load data from URLs
    loader = UnstructuredURLLoader(urls = urls)
    status_display.text('Loading Data ⏳')
    data = loader.load()
        
    # Split data into manageable chunks
    status_display.text('Splitting Data ✂️')
    text_splitter = RecursiveCharacterTextSplitter( separators= ['\n\n', '\n', '.', ','], chunk_size = 1000)
    individual_chunks = text_splitter.split_documents(data)

    # Embed chunks and save to FAISS index
    embeddings = OpenAIEmbeddings()
    vector_data = FAISS.from_documents(individual_chunks, embeddings)
    status_display.text('Embedding Vectors 📥📤')
    time.sleep(2)

    # Save FAISS index to pickle file
    with open(file_path, "wb") as fp:
        pickle.dump(vector_data, fp)

# Collect question from user
question = status_display.text_input('Question: ')
# If a question is entered
if question:
    # If FAISS index pickle file exists
    if os.path.exists(file_path):
        # Load FAISS index from pickle file
        with open(file_path, 'rb') as fp:
            vector_store = pickle.load(fp)
            # Initialize retrieval chain
            retrieval_chain = RetrievalQAWithSourcesChain.from_llm(llm = llm, retriever = vector_store.as_retriever())
            # Find answer to question
            final_output = retrieval_chain({"question": question}, return_only_outputs = True)

            # Display answer
            st.header("IQ's Answer")
            st.write(final_output["answer"])

            # Display sources if available
            sources = final_output.get("Sources", "")
            if sources:
                st.subheader("Further reading:")
                sources_list = sources.split("/n")
                for source in sources_list:
                    st.write(source)