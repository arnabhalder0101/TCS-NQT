import os
import requests
from bs4 import BeautifulSoup
import numpy as np
import time
import random
import tempfile

from langchain_community.document_loaders import BSHTMLLoader
from langchain_core.documents import Document  # updated document import
from langchain_text_splitters import CharacterTextSplitter

from langchain_openai import OpenAIEmbeddings
from langchain_openai.chat_models import ChatOpenAI   # updated import path
from langchain_community.vectorstores import FAISS

from langchain_core.prompts import PromptTemplate
# from langchain_core.memory import ConversationBufferMemory  # memory from core

# Configuration variables
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50
MAX_TOKENS = 15000
MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0.4

# Set up OpenAI API key
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    OPENAI_API_KEY = input("Please enter your OpenAI API key: ")
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def fetch_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

def process_website(url):
    html_content = fetch_html(url)
    if not html_content:
        raise ValueError("No content could be fetched from the website.")

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html') as temp_file:
        temp_file.write(html_content)
        temp_file_path = temp_file.name

    try:
        loader = BSHTMLLoader(temp_file_path)
        documents = loader.load()
    except ImportError:
        print("'lxml' not installed — falling back to html.parser")
        loader = BSHTMLLoader(temp_file_path, bs_kwargs={'features': 'html.parser'})
        documents = loader.load()

    os.unlink(temp_file_path)

    print(f"\nNumber of documents loaded: {len(documents)}")
    if documents:
        print("Sample of loaded content:", documents[0].page_content[:200], "...")
        print("Metadata:", documents[0].metadata)

    text_splitter = CharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    texts = text_splitter.split_documents(documents)
    print(f"Number of text chunks after splitting: {len(texts)}")
    return texts

def print_sample_embeddings(texts, embeddings):
    if texts:
        sample_text = texts[0].page_content
        sample_embedding = embeddings.embed_query(sample_text)
        print("\nSample Text:")
        print(sample_text[:200] + "..." if len(sample_text) > 200 else sample_text)
        print("\nSample Embedding (first 10 dims):", np.array(sample_embedding)[:10])
        print("Embedding shape:", np.array(sample_embedding).shape)
    else:
        print("No texts available for embedding sample.")

# Initialize LLM & embeddings
llm = ChatOpenAI(model_name=MODEL_NAME, temperature=TEMPERATURE, max_tokens=MAX_TOKENS)
embeddings = OpenAIEmbeddings()

# Prompt template
template = """Context: {context}

Question: {question}

Answer the question concisely based only on the given context. If the context doesn't contain relevant information, say "I don't have enough information to answer that question."""
PROMPT = PromptTemplate.from_template(template)

# Memory (chat history)
# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def rag_query(vectorstore, query: str):
    retriever = vectorstore.as_retriever()  # default parameters
    docs = retriever.invoke(query)  # returns list of Document
    return docs

def respond_with_context(docs, query: str):
    context = "\n\n".join([d.page_content for d in docs])
    full_prompt = PROMPT.format(context=context, question=query)
    print("Full prompt:", full_prompt)
    resp = llm.generate_prompt([full_prompt])  # using chat model to generate
    return resp.generations[0][0].text

if __name__ == "__main__":
    print("Welcome — RAG Pipeline (updated for new LangChain).")

    while True:
        url = input("Enter a website URL (or 'quit'): ")
        if url.lower() == 'quit':
            print("Goodbye!")
            break

        try:
            print("Processing website …")
            texts = process_website(url)
            if not texts:
                print("No content found — try another URL.")
                continue

            print("Creating vector store …")
            vectorstore = FAISS.from_documents(texts, embeddings)

            print_sample_embeddings(texts, embeddings)

            print("Ready! You can now ask questions about the content.")

            while True:
                user_query = input("\nYour query (or 'new' for new site, 'quit' to exit): ")
                if user_query.lower() == 'quit':
                    print("Exiting. Bye.")
                    exit()
                if user_query.lower() == 'new':
                    break

                docs = rag_query(vectorstore, user_query)
                if not docs:
                    print("No relevant chunks found.")
                else:
                    answer = respond_with_context(docs, user_query)
                    print("Answer:", answer)

        except Exception as e:
            print("Error:", e)
            print("Try a different URL or check your network.")
