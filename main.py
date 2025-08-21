import os 
import streamlit as st
import asyncio

try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
import pickle
import time
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv


load_dotenv() # here to load our api key from .env file

st.title("News Research Tool 🔎 ")

st.sidebar.title("News Article URLS")

urls=[]
for i in range(3):
    url=st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_cliked=st.sidebar.button("Process URLS")
index_dir="vector_indexx"

main_placefolder=st.empty()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.6,max_tokens=500)

if process_url_cliked:
    #load the data
    loader=UnstructuredURLLoader(urls=urls)
    main_placefolder.text("Data Loading Started...✅✅✅")
    data=loader.load()
    #split data
    text_splitter=RecursiveCharacterTextSplitter(
        separators=['\n\n','\n','.',','],
        chunk_size=1000
        )
    main_placefolder.text("Text Splitter...started..✅✅✅")
    docs=text_splitter.split_documents(data)
    # create Embediings and save it
    embeddings=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004") #use to make vectors 
    vectorindex=FAISS.from_documents(docs,embeddings)
    main_placefolder.text("Embedding vector started Building...✅✅✅")
    time.sleep(2)

    #save the Faiss index to a file
    vectorindex.save_local(index_dir)
    # vector_index=FAISS.load_local("vector_indexx",embeddings,allow_dangerous_deserialization=True)
    # with open(file_path,"wb") as f:
    #     pickle.dump(vectorindex,f)
query=st.text_input("Question: ")
if query:
    if os.path.exists(index_dir):
        embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
        vectorstore=FAISS.load_local(index_dir,embeddings,allow_dangerous_deserialization=True)
        chain=RetrievalQAWithSourcesChain.from_llm(llm=llm,retriever=vectorstore.as_retriever())
        result=chain({"question": query}, return_only_outputs=True)
        st.header("Answer")
        #{"answer":"","source":[]}
        st.write(result["answer"])

        # Display sources of available
        sources=result.get("sources",'').strip()
        if sources:
            st.subheader("sources:")
            sources_list=sources.split("\n") # split the source by newline
            for src in sources_list:
                st.write(src)


