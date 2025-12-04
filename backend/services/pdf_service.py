import os
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

UPLOAD_DIR = "uploads"

def save_upload_file(upload_file, destination: str):
    try:
        with open(destination, "wb") as buffer:
            while content := upload_file.file.read(1024 * 1024):  # Read in chunks
                buffer.write(content)
    finally:
        upload_file.file.close()

def load_and_split_pdfs(file_paths: List[str]) -> List[Document]:
    documents = []
    for file_path in file_paths:
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        documents.extend(docs)
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    return text_splitter.split_documents(documents)
