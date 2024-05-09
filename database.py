from langchain.vectorstores.chroma import Chroma    
from langchain_community.embeddings.ollama import OllamaEmbeddings
import os
import shutil

CHROMA_PATH = "chroma"

def clean_db():
  if os.path.exists(CHROMA_PATH):
    shutil.rmtree(CHROMA_PATH)

def get_db():
  embedding_function = OllamaEmbeddings(model="mxbai-embed-large")

  return Chroma(persist_directory=CHROMA_PATH,
    embedding_function=embedding_function,
    collection_metadata={"hnsw:space": "cosine"})