from typing import List, Dict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)

def get_llm():
    """Get Gemini LLM instance"""
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0.7,
        convert_system_message_to_human=True,
        max_retries=2
    )

logger.info("✓ Course generator initialized with Google Gemini Pro")



class Chapter(BaseModel):
    title: str = Field(description="Title of the chapter")
    description: str = Field(description="Brief description of what will be covered")
    topics: List[str] = Field(description="List of sub-topics in this chapter")

class CourseStructure(BaseModel):
    course_title: str = Field(description="Title of the course")
    modules: List[Chapter] = Field(description="List of chapters/modules in the course")

def generate_course_structure(summary_text: str) -> CourseStructure:
    logger.info("Generating course structure with Gemini...")
    
    parser = JsonOutputParser(pydantic_object=CourseStructure)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an expert curriculum designer. Create a comprehensive course structure based on the provided document summaries. 
The course should be detailed and cover all aspects of the material.

IMPORTANT: You MUST respond with ONLY valid JSON. Do not include any markdown formatting, explanations, or text outside the JSON structure.

{format_instructions}"""),
        ("user", "Document Summary: {summary}\n\nGenerate a structured course curriculum in JSON format.")
    ])
    
    chain = prompt | get_llm() | parser
    
    result = chain.invoke({
        "summary": summary_text,
        "format_instructions": parser.get_format_instructions()
    })
    logger.info("✓ Course structure generated successfully")
    return result

def generate_chapter_content(chapter_title: str, topics: List[str], context_text: str) -> str:
    logger.info(f"Generating chapter content for: {chapter_title}")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert professor. Write a detailed, comprehensive lecture note for the following chapter. Include examples, code snippets (if applicable), and deep explanations. Use Markdown format."),
        ("user", "Chapter: {title}\nTopics: {topics}\n\nContext from Documents:\n{context}\n\nWrite the full chapter content.")
    ])
    
    chain = prompt | get_llm() | StrOutputParser()
    result = chain.invoke({
        "title": chapter_title,
        "topics": ", ".join(topics),
        "context": context_text
    })
    logger.info("✓ Chapter content generated")
    return result

class QuizQuestion(BaseModel):
    question: str = Field(description="The question text")
    options: List[str] = Field(description="4 possible answers")
    correct_answer: int = Field(description="Index of the correct answer (0-3)")
    explanation: str = Field(description="Explanation of why the answer is correct")

class Quiz(BaseModel):
    questions: List[QuizQuestion] = Field(description="List of 5-10 quiz questions")

def generate_quiz(chapter_content: str) -> Quiz:
    logger.info("Generating quiz with Gemini...")
    
    parser = JsonOutputParser(pydantic_object=Quiz)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an exam creator. Create a multiple-choice quiz based on the provided chapter content to test the student's understanding.

IMPORTANT: You MUST respond with ONLY valid JSON. Do not include any markdown formatting, explanations, or text outside the JSON structure.

{format_instructions}"""),
        ("user", "Chapter Content:\n{content}\n\nGenerate a quiz in JSON format.")
    ])
    
    chain = prompt | get_llm() | parser
    result = chain.invoke({
        "content": chapter_content,
        "format_instructions": parser.get_format_instructions()
    })
    logger.info("✓ Quiz generated")
    return result

class Assignment(BaseModel):
    title: str = Field(description="Title of the assignment")
    description: str = Field(description="Detailed instructions for the assignment")
    tasks: List[str] = Field(description="Step-by-step tasks to complete")

def generate_assignment(chapter_content: str) -> Assignment:
    logger.info("Generating assignment with Gemini...")
    
    parser = JsonOutputParser(pydantic_object=Assignment)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a practical instructor. Create a hands-on assignment or project based on the provided chapter content. It should apply the concepts learned.

IMPORTANT: You MUST respond with ONLY valid JSON. Do not include any markdown formatting, explanations, or text outside the JSON structure.

{format_instructions}"""),
        ("user", "Chapter Content:\n{content}\n\nGenerate a practical assignment in JSON format.")
    ])
    
    chain = prompt | get_llm() | parser
    result = chain.invoke({
        "content": chapter_content,
        "format_instructions": parser.get_format_instructions()
    })
    logger.info("✓ Assignment generated")
    return result
