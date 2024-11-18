# **File Sharing System**

A FastAPI-based web application for securely uploading, sharing, and managing files. This project is designed to provide a simple yet robust platform for file sharing.

---

## **Features**

- **File Upload:** Upload files to the server for sharing.
- **File Management:** View, delete, and manage uploaded files.
- **Authentication:** Secure access to the system using JWT authentication.
- **API Support:** RESTful API endpoints for easy integration.
- **Real-Time Notifications:** WebSocket support for real-time file activity updates.

---

## **Tech Stack**

- **Backend Framework:** FastAPI
- **Server:** Uvicorn
- **Database:** MongoDB (or another NoSQL/SQL database of your choice)
- **Authentication:** JWT
- **Frontend:** Optional (React/HTML/CSS/JS)
- **Dependencies Management:** Python virtual environment (`venv`)

---

## **Installation**

### **Prerequisites**
- Python 3.9 or later installed on your system.
- Git installed on your system.
- MongoDB instance running (if using MongoDB).
- A virtual environment tool (like `venv`).

### **Steps**
1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/file_sharing_system.git
   cd file_sharing_system

python -m venv venv
source venv/Scripts/activate  # On Windows
source venv/bin/activate      # On macOS/Linux


pip install -r requirements.txt

Set Environment Variables Create a .env file in the root directory and configure the following:

env
Copy code
DATABASE_URL=mongodb://localhost:27017/file_sharing
SECRET_KEY=your_secret_key_here
Run the Server

bash
Copy code
uvicorn app.main:app --reload
Access the Application Open your browser and go to http://127.0.0.1:8000.

