# 🎓 AI Course Generator

Transform your PDF documents into interactive courses with AI-powered content generation, quizzes, and assignments.

![Course Generator](https://img.shields.io/badge/AI-Course%20Generator-blue?style=for-the-badge)
![Next.js](https://img.shields.io/badge/Next.js-16-black?style=for-the-badge&logo=next.js)
![FastAPI](https://img.shields.io/badge/FastAPI-Python-green?style=for-the-badge&logo=fastapi)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange?style=for-the-badge&logo=google)

## ✨ Features

- 📄 **PDF Upload**: Upload multiple PDF documents
- 🤖 **AI Course Generation**: Automatic course structure creation using Google Gemini
- 📚 **Interactive Content**: Notes, quizzes, and assignments for each module
- 💬 **AI Chat Tutor**: Ask questions about course content
- 🎨 **Modern UI**: Beautiful dark theme with glass morphism effects
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- ⚡ **Real-time Processing**: Live progress tracking during generation

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 18+
- Google Gemini API Key

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ai-course-generator
```

### 2. Backend Setup

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install
```

### 4. Start Development Servers

**Option A: Start both servers with one command**
```bash
python start_dev.py
```

**Option B: Start servers separately**

Backend:
```bash
cd backend
uvicorn main:app --reload
```

Frontend:
```bash
cd frontend
npm run dev
```

### 5. Open the Application

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 🏗️ Architecture

### Backend (FastAPI + Python)
- **FastAPI**: Modern web framework for APIs
- **Google Gemini**: AI model for content generation
- **LangChain**: Framework for LLM applications
- **FAISS**: Vector database for document search
- **HuggingFace**: Free embeddings for semantic search

### Frontend (Next.js + React)
- **Next.js 16**: React framework with App Router
- **React 19**: Latest React with concurrent features
- **Framer Motion**: Smooth animations and transitions
- **Tailwind CSS**: Utility-first CSS framework
- **Lucide React**: Beautiful icons

## 📁 Project Structure

```
ai-course-generator/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── routers/               # API endpoints
│   │   ├── files.py           # File upload
│   │   ├── course.py          # Course generation
│   │   └── chat.py            # Chat functionality
│   ├── services/              # Business logic
│   │   ├── pdf_service.py     # PDF processing
│   │   ├── course_generator.py # AI course generation
│   │   ├── vector_store.py    # Document embeddings
│   │   └── chat_service.py    # Chat with documents
│   └── uploads/               # Uploaded files
├── frontend/
│   ├── app/
│   │   ├── page.tsx           # Main landing page
│   │   ├── layout.tsx         # Root layout
│   │   └── globals.css        # Global styles
│   ├── components/
│   │   ├── landing/           # Landing page components
│   │   ├── course/            # Course viewer components
│   │   ├── shared/            # Shared components
│   │   └── ui/                # UI primitives
│   └── lib/
│       ├── utils.ts           # Utility functions
│       └── animations.ts      # Animation variants
└── README.md
```

## 🎯 How It Works

1. **Upload PDFs**: Users upload one or more PDF documents
2. **AI Processing**: Google Gemini analyzes the content and creates a course structure
3. **Content Generation**: For each module, AI generates:
   - Detailed notes with explanations
   - Multiple-choice quizzes with explanations
   - Practical assignments with step-by-step tasks
4. **Interactive Learning**: Users can:
   - Navigate through modules
   - Take quizzes with instant feedback
   - Complete assignments
   - Chat with AI tutor about content

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the `backend` directory:

```env
# Required: Google Gemini API Key
GOOGLE_API_KEY=your_gemini_api_key_here

# Optional: OpenAI API Key (if you want to use OpenAI instead)
OPENAI_API_KEY=your_openai_key_here
```

### Getting API Keys

**Google Gemini API Key:**
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key to your `.env` file

## 🎨 UI Components

The application features a modern design system with:

- **Glass Morphism**: Translucent cards with blur effects
- **Dark Theme**: Professional dark color scheme
- **Smooth Animations**: Framer Motion powered transitions
- **Responsive Layout**: Mobile-first design
- **Interactive Elements**: Hover effects and micro-interactions

## 🧪 Testing

Test the backend:
```bash
cd backend
python test_backend.py
```

## 🚀 Deployment

### Backend Deployment
- Deploy to platforms like Railway, Render, or Heroku
- Set environment variables in your deployment platform
- Ensure Python 3.8+ is available

### Frontend Deployment
- Deploy to Vercel, Netlify, or similar platforms
- Update API base URL in `frontend/api/client.ts`
- Build with `npm run build`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Troubleshooting

### Common Issues

**Backend won't start:**
- Check if Python dependencies are installed: `pip install -r requirements.txt`
- Verify your Google API key is set in `.env`
- Ensure port 8000 is not in use

**Frontend won't start:**
- Check if Node.js dependencies are installed: `npm install`
- Verify Node.js version is 18+
- Ensure port 3000 is not in use

**Course generation fails:**
- Check your Google API key is valid
- Ensure uploaded files are valid PDFs
- Check backend logs for detailed error messages

**Chat not working:**
- Make sure you've uploaded documents first
- Check if vector store was created successfully
- Verify the chat service is running

### Getting Help

- Check the console logs in your browser (F12)
- Check backend logs in the terminal
- Ensure all dependencies are installed
- Verify API keys are correct

## 🎉 Features Roadmap

- [ ] User authentication and profiles
- [ ] Course sharing and collaboration
- [ ] Advanced quiz types (drag-drop, fill-in-blank)
- [ ] Progress tracking and analytics
- [ ] Export courses to PDF/SCORM
- [ ] Multi-language support
- [ ] Voice narration for courses
- [ ] Integration with LMS platforms

---

Made with ❤️ using AI and modern web technologies