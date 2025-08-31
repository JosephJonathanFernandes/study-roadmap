from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models import db, Topic, Task
from datetime import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
@login_required
def dashboard():
    topics = Topic.query.all()
    # Analytics: count tasks by status
    status_counts = {'pending': 0, 'in-progress': 0, 'completed': 0}
    for topic in topics:
        for task in topic.tasks:
            print(f"Task: {task.task_name}, Status: '{task.status}'")  # Debug print
            if task.status in status_counts:
                status_counts[task.status] += 1
    print(f"Status counts: {status_counts}")  # Debug print
    return render_template("dashboard.html", topics=topics, status_counts=status_counts)

@main_bp.route("/add_topic", methods=["GET", "POST"])
@login_required
def add_topic():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        topic = Topic(name=name, description=description)
        db.session.add(topic)
        db.session.commit()
        flash("Topic added successfully!", "success")
        return redirect(url_for("main.dashboard"))
    return render_template("add_topic.html")

@main_bp.route("/add_task", methods=["GET", "POST"])
@login_required
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
        flash("Task added successfully!", "success")
        return redirect(url_for("main.dashboard"))
    return render_template("add_task.html", topics=topics)

@main_bp.route("/update_task/<int:task_id>", methods=["POST"])
@login_required
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    new_status = request.form.get("status")
    task.status = new_status
    db.session.commit()
    flash(f"Task status updated to {new_status.capitalize()}!", "info")
    return redirect(url_for("main.dashboard"))

@main_bp.route("/delete_task/<int:task_id>", methods=["POST"])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully!", "warning")
    return redirect(url_for("main.dashboard"))

@main_bp.route("/delete_topic/<int:topic_id>", methods=["POST"])
@login_required
def delete_topic(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    # Delete all tasks under this topic first
    for task in topic.tasks:
        db.session.delete(task)
    db.session.delete(topic)
    db.session.commit()
    flash("Topic and its tasks deleted!", "warning")
    return redirect(url_for("main.dashboard"))
