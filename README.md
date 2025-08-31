# Study Roadmap Tracker

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green?logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A simple Flask web app to organize your study goals, track progress, and stay motivated.

---

## 🚀 Features
- Add, edit, delete study tasks
- Track progress by percentage
- Mark tasks as completed
- Clean, responsive UI (Bootstrap)
- Persistent storage (SQLite)

---

## 🛠️ Tech Stack
- Python 3.11+
- Flask
- SQLite
- Bootstrap

---

## 📂 Project Structure
```
study-roadmap-flask/
│── app.py              # Main Flask app
│── models.py           # Database models
│── routes.py           # App routes
│── requirements.txt    # Dependencies
│── README.md           # Documentation
│── .gitignore          # Git ignored files
│
├── instance/
│   └── database.db     # SQLite database
│
├── templates/
│   ├── base.html       # Common layout
│   ├── dashboard.html  # Main dashboard
│   ├── add_task.html   # Add task form
│   ├── add_topic.html  # Add topic form
│
└── static/
    └── style.css       # Custom styles
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
   # On Windows
   .venv\Scripts\activate
   # On Linux/Mac
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the app:**
   ```bash
   flask run
   # or
   python app.py
   ```
5. **Open in browser:**
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## ✅ Future Enhancements
- User authentication (login/register)
- Progress analytics (charts/graphs)
- Export study plan as PDF/CSV
- Notifications/reminders

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).