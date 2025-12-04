import os
import logging
from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from services.pdf_service import save_upload_file, UPLOAD_DIR

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/upload", tags=["Upload"])
async def upload_files(files: List[UploadFile] = File(...)):
    logger.info(f"📤 Received upload request with {len(files)} files")
    
    if not os.path.exists(UPLOAD_DIR):
        logger.info(f"Creating upload directory: {UPLOAD_DIR}")
        os.makedirs(UPLOAD_DIR)
    
    saved_files = []
    for file in files:
        logger.info(f"Processing file: {file.filename}")
        
        if not file.filename.endswith('.pdf'):
            logger.warning(f"Skipping non-PDF file: {file.filename}")
            continue
            
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        logger.info(f"Saving to: {file_path}")
        save_upload_file(file, file_path)
        saved_files.append(file_path)
        logger.info(f"✓ Saved: {file.filename}")
    
    if not saved_files:
        logger.error("No valid PDF files uploaded")
        raise HTTPException(status_code=400, detail="No valid PDF files uploaded")
    
    filenames = [os.path.basename(f) for f in saved_files]
    logger.info(f"✅ Upload complete. Saved files: {filenames}")
    return {"message": "Files uploaded successfully", "filenames": filenames}
