from fastapi import APIRouter, HTTPException, Body
from typing import List, Dict
from services.pdf_service import load_and_split_pdfs, UPLOAD_DIR
from services.vector_store import create_vector_store, load_vector_store
from services.course_generator import (
    generate_course_structure, 
    generate_chapter_content,
    generate_quiz,
    generate_assignment
)
import os
import logging
import traceback

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/generate-structure", tags=["Course"])
async def create_course_structure(filenames: List[str] = Body(...)):
    try:
        # 1. Load PDFs
        logger.info(f"[STEP 1] Loading PDFs: {filenames}")
        file_paths = [os.path.join(UPLOAD_DIR, f) for f in filenames]
        
        # Check if files exist
        for fp in file_paths:
            if not os.path.exists(fp):
                logger.error(f"File not found: {fp}")
                raise HTTPException(status_code=404, detail=f"File not found: {os.path.basename(fp)}")
        
        logger.info(f"[STEP 1] All files exist, loading documents...")
        documents = load_and_split_pdfs(file_paths)
        logger.info(f"[STEP 1] ✓ Loaded {len(documents)} document chunks")
        
        # 2. Create Vector Store
        logger.info("[STEP 2] Creating vector store...")
        vector_store = create_vector_store(documents)
        logger.info("[STEP 2] ✓ Vector store created successfully")
        
        # 3. Generate Summary
        logger.info("[STEP 3] Generating summary from documents...")
        summary_text = " ".join([doc.page_content for doc in documents[:5]]) 
        logger.info(f"[STEP 3] ✓ Summary generated (length: {len(summary_text)} chars)")
        
        # 4. Generate Structure
        logger.info("[STEP 4] Calling Gemini to generate course structure...")
        structure = generate_course_structure(summary_text)
        logger.info("[STEP 4] ✓ Course structure generated successfully")
        logger.info(f"Generated structure: {structure}")
        
        return structure
        
    except Exception as e:
        logger.error(f"❌ Error in create_course_structure: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Failed to generate course structure: {str(e)}")

@router.post("/generate-chapter", tags=["Course"])
async def create_chapter_content(chapter_title: str = Body(...), topics: List[str] = Body(...)):
    try:
        logger.info(f"Generating chapter: {chapter_title}")
        vector_store = load_vector_store()
        if not vector_store:
            raise HTTPException(status_code=400, detail="Vector store not found. Please upload files first.")
        
        # Retrieve relevant context
        logger.info("Retrieving relevant context...")
        retriever = vector_store.as_retriever(search_kwargs={"k": 5})
        docs = retriever.invoke(f"{chapter_title}: {', '.join(topics)}")
        context_text = "\n\n".join([d.page_content for d in docs])
        logger.info(f"Retrieved {len(docs)} relevant documents")
        
        # Generate Content
        logger.info("Generating chapter content...")
        content = generate_chapter_content(chapter_title, topics, context_text)
        logger.info("✓ Chapter content generated")
        
        # Generate Assessment
        logger.info("Generating quiz...")
        quiz = generate_quiz(content)
        logger.info("✓ Quiz generated")
        
        logger.info("Generating assignment...")
        assignment = generate_assignment(content)
        logger.info("✓ Assignment generated")
        
        return {
            "content": content,
            "quiz": quiz,
            "assignment": assignment
        }
    except Exception as e:
        logger.error(f"❌ Error in create_chapter_content: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Failed to generate chapter: {str(e)}")
