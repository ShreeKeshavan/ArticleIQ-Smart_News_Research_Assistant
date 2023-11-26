import os
import streamlit as st
import pickle
from langchain import OpenAI
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.chains import RetrievalQAWithSourcesChain
from dotenv import load_dotenv

# Load data from URLs using the UnstructuredURLLoader
def load_data(urls):
    loader = UnstructuredURLLoader(urls=urls)
    return loader.load()

# Split data into manageable chunks for processing
def split_data(data):
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000,
        chunk_overlap=100)
    return text_splitter.split_documents(data)

# Generate embeddings for the individual data chunks
def embed_data(individual_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    return FAISS.from_documents(individual_chunks, embeddings)

# Save the FAISS index to a file for later retrieval
def save_faiss_index(file_path, vector_data):
    with open(file_path, "wb") as fp:
        pickle.dump(vector_data, fp)

# Load the FAISS index from the file
def load_faiss_index(file_path):
    with open(file_path, 'rb') as fp:
        return pickle.load(fp)

# Create a retrieval chain for question-answering using the vector store
def retrieval_chain(llm, vector_store):
    return RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vector_store.as_retriever())

# Use the retrieval chain to find and return an answer to a question, along with sources
def find_answer(retrieval_chain, question):
    return retrieval_chain({"question": question})  # Removed return_only_outputs=True

def main():
    load_dotenv()
    
    # Set up the Streamlit interface
    st.markdown("## ArticleIQ - Smart News Research Assistant 🔍")

    # To collect URLs from user input, increase the range as needed if more are required.
    st.sidebar.title("Articles URLs 👇")
    urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]
    
    activate_articleiq = st.sidebar.button("Activate ArticleIQ")
    status_display = st.empty()
    
    file_path = 'FAISS_Vector_Data.pkl'
    llm = OpenAI(temperature=0.7, max_tokens=500)  # "text-davinci-003"
    
    # If the button is clicked, start processing the URLs
    if activate_articleiq:
        data = load_data(urls)
        status_display.text('Loading Data ⏳')
        
        individual_chunks = split_data(data)
        status_display.text('Splitting Data ✂️')
        
        vector_data = embed_data(individual_chunks)
        status_display.text('Embedding Vectors 📥📤')
        
        save_faiss_index(file_path, vector_data)
        
    # Allow the user to enter a question and get an answer
    question = status_display.text_input('Question: ')
    if question:
        if os.path.exists(file_path):
            vector_store = load_faiss_index(file_path)
            retrieval_chain_obj = retrieval_chain(llm, vector_store)
            final_output = find_answer(retrieval_chain_obj, question)
            st.header("IQ's Answer")
            st.write(final_output["answer"])
            
            # Display the sources for further reading
            sources = final_output.get("sources", '')
            if sources:
                st.subheader("Further reading:")
                sources_str = sources.split("\n") 
                for source in sources_str:
                    st.write(source)  

if __name__ == "__main__":
    main()