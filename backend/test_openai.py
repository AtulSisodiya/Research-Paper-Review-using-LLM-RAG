"""
Test script to verify OpenAI API key is working
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

print("Testing OpenAI API connection...")
print(f"API Key present: {'OPENAI_API_KEY' in os.environ}")

if 'OPENAI_API_KEY' in os.environ:
    api_key = os.environ['OPENAI_API_KEY']
    print(f"API Key (first 10 chars): {api_key[:10]}...")
    
    try:
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
        response = llm.invoke("Say 'Hello, API is working!'")
        print(f"\n✅ SUCCESS! OpenAI API is working!")
        print(f"Response: {response.content}")
    except Exception as e:
        print(f"\n❌ ERROR: OpenAI API failed!")
        print(f"Error: {str(e)}")
else:
    print("\n❌ ERROR: OPENAI_API_KEY not found in environment!")
