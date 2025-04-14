# 📧 Conversational Email Bot (AI Job Assistant)

An email assistant built using **FastAPI**, **Streamlit**, and **Python** that automatically replies to job-related emails based on keywords. Designed as a home assessment project for AI Engineer Intern roles.

---

## 🚀 Features

- ✉️ Send custom emails through a user-friendly interface
- 🔍 Search and filter emails by sender, recipient, or keywords
- 🤖 Auto-reply for emails containing keywords like *job*, *interview*, *resume*, etc.
- 💾 In-memory email storage (can be replaced with database)
- ⚡ FastAPI backend + Streamlit frontend

---

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Validation**: Pydantic models
- **HTTP**: Python `requests` library

---

## 📂 Project Structure

ConversationalEmailBot/ 
│ 
|└── backend/ 
├── main.py
├── ai.py 
├── models.py 
├── database.py
│ 
│└── frontend/ 
|── app.py 
|
├── requirements.txt # Python dependencies 
|
├── README.md # Project overview 

---

## 🧪 How to Run

**### 1. Clone the repo**

**### 2. Install dependencies**

**### 3. Start the backend (FastAPI)**
└──uvicorn main:app --reload

**### 4. Start the frontend (Streamlit)**
└──cd frontend
└──streamlit run app.py



👤 Author
Yash Aparajit
AI/ML Engineer
LinkedIn: linkedin.com/in/yashaparajit







