:

🚀 DevPal – AI Chatbot with React & FastAPI
📌 Overview

DevPal is a full-stack AI chatbot application that allows users to chat with an AI assistant in real time.
The project is built with a React frontend and a FastAPI backend, with support for LLMs (Ollama / OpenAI / others).

It mimics a ChatGPT-like experience with:

Real-time chat UI

Typing indicators

Streaming AI responses

Modern UI with animations (Lottie / Framer Motion)

🏗️ Tech Stack
Frontend (React)

React 18 – component-based UI

Axios – API calls to backend

Lottie-React – animated bot (robot animation)

Framer Motion – smooth UI transitions

Bootstrap / Custom CSS – styling

Backend (FastAPI)

FastAPI – lightweight Python API framework

Uvicorn – ASGI server

Ollama (LLM provider, can be swapped with OpenAI or HuggingFace)

StreamingResponse – stream messages for a ChatGPT-like typing effect

📂 Project Structure
DevPal/
│── backend/
│   ├── main.py              # FastAPI backend entrypoint
│   ├── requirements.txt     # Python dependencies
│
│── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── index.js         # React entrypoint
│   │   ├── App.js           # Root component
│   │   ├── assets/
│   │   │   └── robot.json   # Bot animation file
│   │   ├── Components/
│   │   │   ├── ChatWindow.jsx
│   │   │   ├── MessageBubble.jsx
│   │   │   └── ThemeToggle.jsx
│   │   ├── hooks/
│   │   │   └── useChat.js   # Custom chat hook (optional)
│   ├── package.json         # Node dependencies

⚙️ Installation & Setup
1. Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
uvicorn main:app --reload


Runs backend at:
👉 http://127.0.0.1:8000

2. Frontend Setup
cd frontend
npm install
npm start


Runs frontend at:
👉 http://localhost:3000

💡 Features

✅ Interactive Chat – send & receive messages like ChatGPT
✅ Streaming Responses – AI types word by word
✅ Typing Indicator – shows when the bot is thinking
✅ Modern UI – bot avatar, animations, dark/light theme
✅ Keyboard Shortcuts – press Enter to send messages
✅ Extensible Backend – switch AI model provider easily

🔄 API Contract
Endpoint

POST /chat

Request
{
  "message": "Hello, DevPal!"
}

Response
{
  "reply": "Hi! I'm DevPal, your AI assistant."
}


(or streamed response if using StreamingResponse)

🌐 Future Improvements

🔗 Multi-model support (OpenAI, HuggingFace, Gemini, Ollama)

💾 Save chat history in MongoDB / PostgreSQL

👥 Multi-user authentication

🎤 Voice input & speech synthesis

📱 Mobile-friendly PWA