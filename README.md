# 📊 Python Log Analyzer Dashboard (Dockerized)

A web-based log analyzer built using Flask and Docker. This application allows users to upload log files and analyze ERROR, WARNING, and INFO messages in real-time.

## 🧠 Features
- Upload log files via UI
- Analyze ERROR / WARNING / INFO logs
- Real-time results display
- Docker containerized application
- Persistent storage using Docker volumes

---

## 🛠️ Tech Stack
- Python (Flask)
- Docker
- HTML

---

## 📁 Project Structure

log-analyzer-advanced/
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│ └── index.html
└── logs/


--

## 🐳 Docker Setup

### Build Image

docker build -t log-analyzer-advanced .


### Run Container

docker run -p 5001:5000 -v $(pwd)/logs:/app/logs log-analyzer-advanced


---

## 🌐 Access Application
http://localhost:5001

---

## ☁️ Deployment (Render)

This project is deployed using a cloud platform:

- Create account on Render
- Connect GitHub repository
- Select **Web Service**
- Environment: **Docker**
- Branch: **main**
- Deploy automatically using Dockerfile

---

## 📸 Screenshot
https://1drv.ms/i/c/351c3fb795fe3dba/IQATGyN8_To7RaV-cxlQlotBAdiZVFSqM9hqFGEz6kXbu8s?e=qA1IzJ
https://python-log-analyzer-dashboard.onrender.com
---

## 💡 Learning Outcomes
- Built Flask-based web application
- Implemented file upload & log parsing
- Containerized application using Docker
- Used Docker volumes for persistent storage
- Deployed application to cloud

---
---
