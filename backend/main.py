from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI(title="LangChain Course Generator")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from routers import files, course, chat

app.include_router(files.router)
app.include_router(course.router)
app.include_router(chat.router)

@app.get("/")
async def root():
    logger.info("✅ Root endpoint called")
    return {"message": "LangChain Course Generator API is running", "status": "healthy"}

@app.get("/health")
async def health_check():
    logger.info("✅ Health check endpoint called")
    return {"status": "healthy", "message": "Backend is running properly"}
