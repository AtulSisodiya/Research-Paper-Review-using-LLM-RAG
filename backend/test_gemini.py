import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0.7
)

try:
    print("Testing Gemini 1.5 Flash...")
    response = llm.invoke("Hello, how are you?")
    print("Response received:")
    print(response.content)
    print("✓ Test successful!")
except Exception as e:
    print(f"❌ Test failed: {e}")
