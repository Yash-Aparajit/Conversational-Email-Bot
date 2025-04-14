# Conversational Email Bot (AI Job Assistant) 🤖📧

A lightweight email simulation app built with FastAPI (backend) and Streamlit (frontend). The app allows you to send, search, and auto-reply to emails based on keywords related to jobs, resumes, and interviews.

---

## Features 🚀

- Send emails between users (simulated)
- Automatically generate AI-based replies if job-related keywords are detected
- Search emails by sender, recipient, or keyword
- Easy-to-use Streamlit UI

---

## Tech Stack 🛠️

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Data Storage**: In-memory Python list (for testing/demo purposes)
- **Others**: UUID, Requests, Pydantic

---

## How to Run ⚙️

Install dependencies, then:

1. Run the backend:
├──`uvicorn main:app --reload`  
2. In a new terminal, run the frontend:
├──`streamlit run frontend/app.py`  
3. Open the app in your browser and test it out!

---

## Folder Structure 📁

ConversationalEmailBot/ <br>
│ └── backend/ <br>
├── main.py  <br>
├── ai.py <br>
├── models.py <br> 
├── config.py <br>
│ <br>
├── requirements.txt <br> 
├── README.md <br>
│ └── frontend/ <br>
└── app.py <br>

---

👤 Author <br>
Yash Aparajit <br>
AI/ML Engineer <br>
LinkedIn: linkedin.com/in/yashaparajit <br>
