from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Topic, Task
from datetime import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def dashboard():
    topics = Topic.query.all()
    return render_template("dashboard.html", topics=topics)

@main_bp.route("/add_topic", methods=["GET", "POST"])
def add_topic():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        topic = Topic(name=name, description=description)
        db.session.add(topic)
        db.session.commit()
        return redirect(url_for("main.dashboard"))
    return render_template("add_topic.html")

@main_bp.route("/add_task", methods=["GET", "POST"])
def add_task():
    topics = Topic.query.all()
    if request.method == "POST":
        topic_id = request.form.get("topic_id")
        task_name = request.form.get("task_name")
        due_date = request.form.get("due_date")
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d") if due_date else None
        task = Task(topic_id=topic_id, task_name=task_name, due_date=due_date_obj)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("main.dashboard"))
    return render_template("add_task.html", topics=topics)

@main_bp.route("/update_task/<int:task_id>", methods=["POST"])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    new_status = request.form.get("status")
    task.status = new_status
    db.session.commit()
    return redirect(url_for("main.dashboard"))
