📰 News Research Tool 🔎
📌 Overview

The News Research Tool is an AI-powered application that allows users to input news article URLs, process the content, and ask natural language questions about the collected information. The tool converts article text into vector embeddings, stores them in a FAISS vector database, and uses Google Gemini (via LangChain) to retrieve the most relevant answers along with their sources.

This project is built using:

Streamlit → Interactive UI

LangChain → LLM orchestration

Google Gemini API → Language model & embeddings

FAISS → Vector database for fast retrieval

UnstructuredURLLoader → Extracts text from URLs

⚙️ How It Works

Enter URLs
User provides up to 3 news article URLs via the sidebar.

Data Loading
The tool fetches article content using UnstructuredURLLoader.

Text Splitting
Articles are split into smaller chunks using RecursiveCharacterTextSplitter to make them embedding-friendly.

Embedding Generation
Each chunk is converted into vector embeddings using GoogleGenerativeAIEmbeddings.

Vector Store (FAISS)
Embeddings are stored in a FAISS index (vector_indexx directory).

Question Answering

When a user asks a question:
The tool loads the FAISS index.
Finds the most relevant chunks (vector similarity search).
Uses RetrievalQAWithSourcesChain with Gemini to generate an answer with sources.

🖼️ Workflow Diagram
URLs → Loader → Text Splitter → Embeddings → FAISS Index → Retriever → Gemini LLM → Answer + Sources

🚀 Getting Started
1. Clone Repository
git clone https://github.com/yourusername/news-research-tool.git
cd news-research-tool

2. Install Dependencies
pip install -r requirements.txt

3. Setup Environment Variables

Create a .env file in the project root and add your Google API Key:
GOOGLE_API_KEY=your_google_api_key_here

4. Run the App
streamlit run app.py

🖥️ Usage

Enter up to 3 news article URLs in the sidebar.
Click Process URLs to fetch, split, and store embeddings.
Type a question in the input box.
Get answers with references to sources.

📂 Project Structure
📦 news-research-tool
 ┣ 📜 app.py              # Main Streamlit app
 ┣ 📜 requirements.txt    # Python dependencies
 ┣ 📜 .env                # API key (not committed to repo)
 ┗ 📂 vector_indexx       # FAISS vector index (generated after processing)

🔮 Example

Input URLs:
https://example.com/news/article1
https://example.com/news/article2

Question:
"What are the main economic impacts mentioned in these articles?"

Output:
Answer:
The articles highlight rising inflation and unemployment as key economic impacts...  

Sources:
https://example.com/news/article1  
https://example.com/news/article2  

🌟 Future Improvements

Support for more than 3 URLs
PDF and document support
Caching embeddings for faster reloads
Enhanced UI with better source visualization
