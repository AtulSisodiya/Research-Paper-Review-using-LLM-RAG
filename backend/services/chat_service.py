from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from services.vector_store import load_vector_store
import logging

logger = logging.getLogger(__name__)

def get_chat_llm():
    """Get Gemini LLM for chat"""
    return ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.5,
        convert_system_message_to_human=True
    )

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def get_chat_response(query: str, chat_history: list = []):
    logger.info(f"Chat query received: {query[:50]}...")
    vector_store = load_vector_store()
    if not vector_store:
        return "Please upload documents first to start chatting."
    
    retriever = vector_store.as_retriever()
    
    system_prompt = (
        "You are an assistant for a course generated from PDF documents. "
        "Use the following pieces of retrieved context to answer the question. "
        "If you don't know the answer, say that you don't know. "
        "Use three sentences maximum and keep the answer concise."
        "\n\n"
        "{context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    rag_chain = (
        {"context": retriever | format_docs, "input": RunnablePassthrough()}
        | prompt
        | get_chat_llm()
        | StrOutputParser()
    )
    
    response = rag_chain.invoke(query)
    logger.info("✓ Chat response generated")
    return response
