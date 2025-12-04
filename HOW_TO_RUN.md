# 🚀 How to Run the LangChain Course Generator Application

This guide will walk you through running your LangChain Course Generator application step by step.

---

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Structure](#project-structure)
3. [First-Time Setup](#first-time-setup)
4. [Running the Application](#running-the-application)
5. [Stopping the Application](#stopping-the-application)
6. [Troubleshooting](#troubleshooting)

---

## ✅ Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Node.js 18+** and npm - [Download Node.js](https://nodejs.org/)
- **Google Gemini API Key** - [Get API Key](https://makersuite.google.com/app/apikey)

---

## 📁 Project Structure

Your application has two main parts:

```
d:\1DG Internship\langchain project\
├── backend/          # FastAPI Python server
│   ├── main.py
│   ├── requirements.txt
│   ├── .env         # API keys (you need to create this)
│   └── .venv/       # Python virtual environment
│
└── frontend/        # Next.js React application
    ├── package.json
    └── node_modules/
```

---

## 🔧 First-Time Setup

### Step 1: Set Up the Backend

#### 1.1 Create Environment File

Create a file named `.env` in the `backend` folder:

**Location**: `d:\1DG Internship\langchain project\backend\.env`

**Contents**:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> **Note**: Replace `your_gemini_api_key_here` with your actual Gemini API key.

#### 1.2 Create Virtual Environment (First Time Only)

Open PowerShell and run:

```powershell
cd "d:\1DG Internship\langchain project\backend"
python -m venv .venv
```

#### 1.3 Activate Virtual Environment

```powershell
.venv\Scripts\Activate.ps1
```

> **Troubleshooting**: If you get an execution policy error, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

#### 1.4 Install Python Dependencies

```powershell
pip install -r requirements.txt
```

---

### Step 2: Set Up the Frontend

#### 2.1 Install Node.js Dependencies (First Time Only)

Open a **new PowerShell window** and run:

```powershell
cd "d:\1DG Internship\langchain project\frontend"
npm install
```

---

## ▶️ Running the Application

Once you've completed the first-time setup, follow these steps every time you want to run the application:

### Terminal 1: Start the Backend Server

1. Open PowerShell
2. Navigate to the backend folder:
   ```powershell
   cd "d:\1DG Internship\langchain project\backend"
   ```

3. Activate the virtual environment:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

4. Start the backend server:
   ```powershell
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

✅ **Backend is now running at**: `http://localhost:8000`

---

### Terminal 2: Start the Frontend Server

1. Open a **NEW** PowerShell window (keep the backend running!)
2. Navigate to the frontend folder:
   ```powershell
   cd "d:\1DG Internship\langchain project\frontend"
   ```

3. Start the frontend development server:
   ```powershell
   npm run dev
   ```

You should see:
```
▲ Next.js 16.0.6
- Local:    http://localhost:3000
✓ Ready in 1309ms
```

✅ **Frontend is now running at**: `http://localhost:3000`

---

### Access Your Application

Open your web browser and go to:

**🌐 http://localhost:3000**

You should see the LangChain Course Generator interface!

---

## 🛑 Stopping the Application

To stop the servers:

1. Go to **Terminal 1** (Backend) and press `Ctrl + C`
2. Go to **Terminal 2** (Frontend) and press `Ctrl + C`
3. (Optional) Deactivate the Python virtual environment in Terminal 1:
   ```powershell
   deactivate
   ```

---

## 🔍 Troubleshooting

### Backend Issues

#### ❌ "Module not found" errors
**Solution**: Make sure the virtual environment is activated and dependencies are installed:
```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

#### ❌ "Port 8000 already in use"
**Solution**: Either:
- Stop the process using port 8000, or
- Use a different port:
  ```powershell
  uvicorn main:app --reload --host 0.0.0.0 --port 8001
  ```

#### ❌ "API key errors" or "GEMINI_API_KEY not found"
**Solution**: 
- Check that `.env` file exists in the `backend` folder
- Verify your Gemini API key is correct
- Make sure there are no extra spaces in the `.env` file

---

### Frontend Issues

#### ❌ "Cannot find module" or dependency errors
**Solution**: Delete and reinstall dependencies:
```powershell
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json
npm install
```

#### ❌ "Port 3000 already in use"
**Solution**: Next.js will automatically use port 3001 if 3000 is busy. Check the terminal output for the actual port.

#### ❌ "Failed to fetch" or "Connection refused"
**Solution**: Make sure the backend server is running on port 8000 first.

---

## 📝 Quick Reference Commands

### Backend (Terminal 1)
```powershell
cd "d:\1DG Internship\langchain project\backend"
.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend (Terminal 2)
```powershell
cd "d:\1DG Internship\langchain project\frontend"
npm run dev
```

### Access Application
```
http://localhost:3000
```

---

## 💡 Tips

1. **Always start the backend first**, then the frontend
2. **Keep both terminals open** while using the application
3. **Check the terminal output** for any error messages
4. **The backend must be running** for the frontend to work properly
5. **Use `Ctrl + C`** to stop servers gracefully

---

## 🎯 What Each Server Does

### Backend (Port 8000)
- Handles PDF processing
- Manages course generation using Gemini AI
- Provides API endpoints for the frontend
- Manages vector store and embeddings

### Frontend (Port 3000)
- Provides the user interface
- Handles user interactions
- Communicates with the backend API
- Displays generated courses

---

## 🆘 Still Having Issues?

If you encounter any problems:

1. **Check both terminal windows** for error messages
2. **Verify your Gemini API key** is valid and has quota
3. **Make sure Python and Node.js** are properly installed
4. **Try restarting** both servers
5. **Check your internet connection** (required for Gemini API)

---

**Happy Learning! 🎓**
