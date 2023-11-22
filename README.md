<h1>ArticleIQ - Smart News Research Assistant</h1>

<h2>Introduction</h2>
<p>ArticleIQ is a Smart News Research Assistant application designed to streamline the process of finding answers to your queries from the content of provided articles. The application is built using the Langchain, Streamlit framework and makes use of the powerful OpenAI GPT-3 model for information retrieval and question-answering tasks.</p>

<h2>Getting Started</h2>
<p>Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.</p>

<h3>Prerequisites</h3>
<p>Make sure you have Python installed on your machine. You can download Python <a href="https://www.python.org/">here</a>.</p>

<h2>Installation</h2>
<p>Clone the repository to your local machine:</p>

```bash
git clone https://github.com/ShreeKeshavan/ArticleIQ-Smart_News_Research_Assistant.git
```

<p>Navigate to the project directory and install the required packages:</p>

```bash
cd ArticleIQ-Smart_News_Research_Assistant
pip install -r requirements.txt
```

<p>Run the Streamlit application:</p>

```bash
streamlit run main.py
```

<p>The Streamlit app will open in your default web browser.</p>

<h2>Usage</h2>
<p>Upon running the application, you'll see an interface where you can input up to three article URLs for analysis.</p>

<ul>
<li>Enter the URLs of the articles in the sidebar.</li>
<li>Click on the "Activate ArticleIQ" button. The application will start processing the articles - loading the data, splitting it into manageable chunks, embedding these chunks, and saving them to a FAISS index.</li>
<li>Once processing is done, input your question in the 'Question:' field.</li>
<li>The application will retrieve the most relevant answer to your question from the content of the articles provided.</li>
</ul>


<h2>License</h2>
<p>This project is licensed under the Apache License 2.0- see the LICENSE.md file for details.</p>
