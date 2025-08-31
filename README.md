# Study Roadmap Flask

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green?logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern Flask web app to track your study progress, manage tasks and topics, and visualize your learning journey.

---

## 🚀 Features
- User authentication (register/login/logout)
- Add, edit, delete study tasks and topics
- Track progress with status (pending, in-progress, completed)
- Visual analytics (pie chart)
- Profile page with avatar upload and password change
- Responsive, accessible UI (Bootstrap 5, FontAwesome)
- Flash messages, tooltips, modals, and confirmation dialogs
- Persistent storage (SQLite)

---

## 🛠️ Tech Stack
- Python 3.11+
- Flask
- Flask-Login
- SQLAlchemy
- Bootstrap 5
- FontAwesome
- Chart.js

---

## 📂 Project Structure
```
study-roadmap-flask/
│── app.py              # Main Flask app
│── models.py           # Database models
│── routes.py           # App routes
│── auth.py             # Authentication routes
│── profile.py          # Profile routes
│── requirements.txt    # Dependencies
│── README.md           # Documentation
│── .gitignore          # Git ignored files
│
├── instance/
│   └── database.db     # SQLite database
│
├── static/
│   ├── style.css       # Custom styles
│   └── avatars/        # User profile images
│
├── templates/
│   ├── base.html       # Common layout
│   ├── dashboard.html  # Main dashboard
│   ├── add_task.html   # Add task form
│   ├── add_topic.html  # Add topic form
│   ├── register.html   # Registration page
│   ├── login.html      # Login page
│   └── profile.html    # Profile page
```

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/study-roadmap-flask.git
   cd study-roadmap-flask
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the app:**
   ```bash
   python app.py
   ```
5. **Open in browser:**
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## ✅ Future Enhancements
- Export study plan as PDF/CSV
- Notifications/reminders
- Progress analytics (charts/graphs)
- Task deadlines and priorities
- Multi-user support

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).