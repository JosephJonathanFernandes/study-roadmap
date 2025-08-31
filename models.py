from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    tasks = db.relationship('Task', backref='topic', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    task_name = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending / in-progress / completed
    due_date = db.Column(db.Date, nullable=True)
