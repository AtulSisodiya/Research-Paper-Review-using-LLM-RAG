#!/usr/bin/env python3
"""
Simple test script to verify backend functionality
"""
import requests
import json
import sys

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_root():
    """Test root endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ Root endpoint working")
            return True
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Root endpoint error: {e}")
        return False

def main():
    print("🧪 Testing Backend Endpoints...")
    print("-" * 40)
    
    # Test basic endpoints
    health_ok = test_health()
    root_ok = test_root()
    
    if health_ok and root_ok:
        print("\n✅ Backend is working correctly!")
        print("\n🚀 You can now:")
        print("1. Start the backend: cd backend && uvicorn main:app --reload")
        print("2. Start the frontend: cd frontend && npm run dev")
        print("3. Open http://localhost:3000 in your browser")
    else:
        print("\n❌ Backend has issues. Make sure it's running:")
        print("cd backend && uvicorn main:app --reload")
        sys.exit(1)

if __name__ == "__main__":
    main()