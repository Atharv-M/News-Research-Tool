# News-Research-Tool

**AI-powered news summarization and Q&A assistant**

The **News-Research-Tool** lets users submit news article URLs, processes them into vector embeddings via Google Gemini, and enables intelligent, natural-language querying with reference-backed answers.

---

##  Features

-  **Streamlit-powered UI** – Enter up to 3 news articles via a sidebar for a clean interface.
-  **Content ingestion** – Fetches URL text with `UnstructuredURLLoader`.
-  **Smart text splitting** – Uses `RecursiveCharacterTextSplitter` to prepare text for embeddings.
-  **Embeddings** – Converts text chunks to vector representations using `GoogleGenerativeAIEmbeddings`.
-  **Efficient vector search** – Stores embeddings in a FAISS index (`vector_indexx`) for fast retrieval.
-  **Retrieval-based Q&A** – Employs `RetrievalQAWithSourcesChain` with Google Gemini to answer user queries, including source references.

---

##  ‍ How It Works

**Workflow:**

```

URLs → Loader → Text Splitter → Embeddings → FAISS Index → Retriever → Gemini LLM → Answer + Sources

````

1. **User input** – Paste up to three article URLs into the sidebar.
2. **Processing** – The app fetches, splits, and embeds article content.
3. **Querying** – User poses a natural-language question.
4. **Response** – The app retrieves relevant content from FAISS and uses Gemini to answer, with clear sources.

---

##  Setup & Usage

```bash
git clone https://github.com/Atharv-M/News-Research-Tool.git
cd News-Research-Tool
pip install -r requirements.txt
````

1. Create a `.env` file in the project root:

   ```dotenv
   GOOGLE_API_KEY=your_google_api_key_here
   ```

2. Run the app:

   ```bash
   streamlit run app.py
   ```

3. In the Streamlit interface:

   * Enter up to 3 news article URLs in the sidebar.
   * Click **Process URLs** to fetch and index data.
   * Ask your question in the input box and get answers with clear sources.

---

## Project Structure

```
news-research-tool/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .env                      # (Not committed) Environment variables
└── vector_indexx/            # Generated FAISS index directory
```

---

## Example Session

* **Input URLs:**

  * `https://example.com/news/article1`
  * `https://example.com/news/article2`
* **Question:** “What are the main economic impacts mentioned?”
* **Output:**

  ```
  The articles highlight rising inflation and unemployment as key economic impacts...
  Sources:
  - https://example.com/news/article1
  - https://example.com/news/article2
  ```

---

## Future Improvements

* [ ] Support more than 3 URLs per session
* [ ] Add PDF and other document ingestion
* [ ] Cache embeddings for faster loading
* [ ] Enhance UI (e.g., better source visualization)

---

## For Recruiters / Developers

### Recruiters

* **Modern tech stack:** Streamlit, LangChain, FAISS, and Google Gemini.
* **Problem solved:** Makes large-scale news comprehension easy via AI-driven retrieval and Q\&A.
* **Scalable & interactive:** Clean interface, modular design suitable for extension.

### Developers

* **Modular design:** Clear separation of loader, splitting, embedding, indexing, and retrieval.
* **Vector search foundation:** FAISS allows expanding to any document-based QA.
* **Future-ready:** Easily extendable to support other formats, LLMs, or caching strategies.






