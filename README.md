# 🤖 DevPal – AI Chat Assistant

DevPal is a **modern AI-powered chat assistant** built with **FastAPI (backend)** and **React (frontend)**.  
It provides real-time messaging, smooth UI animations, retry on errors, and a typing indicator – inspired by ChatGPT’s experience.  

---

## 🚀 Features

- ⚡ **FastAPI Backend** – clean REST API at `/chat`  
- 💬 **Real-time Messaging** with typing indicator  
- 🎨 **Modern UI** with animations (Framer Motion)  
- 🌓 **Light/Dark Mode** toggle ready  
- 🔁 **Retry Failed Messages** (with pulsing retry button)  
- 🚨 **Shake Animation on Errors** so users don’t miss them  
- ⌨️ **Press Enter to Send** messages  
- 📱 **Responsive Design** – works on desktop & mobile  

---

## 🛠️ Tech Stack

### Backend
- [FastAPI](https://fastapi.tiangolo.com/) – Python async web framework  
- [Uvicorn](https://www.uvicorn.org/) – ASGI server  
- AI Model: **Ollama (LLaMA2)** *(can be swapped with OpenAI or others)*  

### Frontend
- [React](https://react.dev/) – Component-based UI  
- [Axios](https://axios-http.com/) – API calls  
- [Framer Motion](https://www.framer.com/motion/) – animations  
- [CSS3 / Custom Theme Variables] – for modern styling  

---

## ⚙️ Setup Instructions

### 1️⃣ Backend Setup (FastAPI)

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/devpal.git
   cd devpal/backend

2. Create virtual environment:

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

3. Install dependencies:

pip install -r requirements.txt

4.Run FastAPI server:

uvicorn main:app --reload


2️⃣ Frontend Setup (React)

1. Go to frontend folder:

cd ../frontend

2. Install dependencies:

npm install

3. Start dev server:

npm start
