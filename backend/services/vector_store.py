import os
from typing import List
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
import logging

logger = logging.getLogger(__name__)

VECTOR_STORE_PATH = "faiss_index"

def get_embeddings():
    """
    Use HuggingFace embeddings (free, runs locally) instead of OpenAI
    This avoids API quota issues and is completely free!
    """
    logger.info("Using HuggingFace embeddings (all-MiniLM-L6-v2) - Free & Local!")
    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )

def create_vector_store(documents: List[Document]):
    logger.info("Creating vector store with HuggingFace embeddings...")
    embeddings = get_embeddings()
    vector_store = FAISS.from_documents(documents, embeddings)
    vector_store.save_local(VECTOR_STORE_PATH)
    logger.info("✓ Vector store created and saved")
    return vector_store

def load_vector_store():
    embeddings = get_embeddings()
    if os.path.exists(VECTOR_STORE_PATH):
        logger.info("Loading existing vector store...")
        return FAISS.load_local(VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True)
    logger.warning("No vector store found")
    return None
