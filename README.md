# ArticleIQ - Smart News Research Assistant 🔍

ArticleIQ is an AI-powered tool designed to assist with researching and analyzing news articles. By leveraging state-of-the-art language models, Langchain and vector search technology, ArticleIQ provides insightful answers to your questions based on the content of the provided news articles.

## Project Description

ArticleIQ utilizes Streamlit to create an interactive web interface where users can input URLs of news articles they want to analyze. It processes the text of these articles using the LangChain library, which includes components such as OpenAI for language modeling, UnstructuredURLLoader for data loading, RecursiveCharacterTextSplitter for text splitting, and FAISS for vector storage and search. The tool creates vector embeddings with either OpenAI or HuggingFace's Instruct embeddings, and uses a retrieval-based question-answering system to provide users with precise answers and sources for further reading.

## Technical Architecture
![IMG_4234](https://github.com/ShreeKeshavan/ArticleIQ-Smart_News_Research_Assistant/assets/114231374/09624ebf-f1be-4f2e-89ab-b8e17c788d5a)

**The main libraries and technologies used in this project include:**

- Streamlit: For creating the interactive web interface.
- LangChain: To facilitate the construction of the retrieval-based QA chain.
- OpenAI: Providing access to powerful language models for text generation and embedding.
- HuggingFace Transformers: For alternative language model embeddings if desired.
- FAISS (Facebook AI Similarity Search): For efficient similarity search and retrieval of text chunks.
- Python's Pickle: For saving and loading the FAISS vector index.
- dotenv: For loading environment variables securely.

## Installation Guide

To set up ArticleIQ, you'll need Python 3.6 or higher. Follow these steps:

1. Clone the repository:

```python
git clone https://github.com/ShreeKeshavan/ArticleIQ-Smart_News_Research_Assistant.git
```

<p>Navigate to the project directory and install the required packages:</p>

```python
cd ArticleIQ-Smart_News_Research_Assistant
pip install -r requirements.txt
```

<p>Run the Streamlit application:</p>

```python
streamlit run main.py
```

## Usage Instructions

To use ArticleIQ, follow these steps:

1. Run the Streamlit application: streamlit run main.py
2. Open your web browser and go to `localhost:8501` to view the app.
3. Input the URLs of the news articles you want to analyze in the sidebar.
4. Click "Activate ArticleIQ" to process the articles.
5. Once processed, you can ask questions in the provided text field to get answers based on the articles' content.

## Features

- Streamlit web interface for easy interaction.
- Supports multiple news articles through URL input.
- Vector embedding generation for efficient information retrieval.
- Question-answering system with sources for in-depth research.

## Examples

Here's a short example of how to interact with ArticleIQ:

1. Input URLs:
- URL 1: `https://example.com/news-article-one`
- URL 2: `https://example.com/news-article-two`

2. Click "Activate ArticleIQ" to process the articles.

3. Ask a question:
- Input: "What are the main points discussed in the articles?"

4. Receive an answer along with sources for further reading.
   
## ArticleIQ-Streamlit Application Interface Overview
![image](https://github.com/ShreeKeshavan/ArticleIQ-Smart_News_Research_Assistant/assets/114231374/1e9c024d-6672-4137-804f-7a8532442e31)

## Documentation

For more detailed information on the project's architecture and functions, please refer to the `ArticleIQ Project Documentation` folder in the repository.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
