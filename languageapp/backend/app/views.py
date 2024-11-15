from flask import Blueprint, jsonify, request
from .models import Lesson, UserProgress
from . import db

api_bp = Blueprint("api", __name__)

@api_bp.route("/lessons", methods=["GET"])
def get_lessons():
    lessons = Lesson.query.all()
    return jsonify([{"id": lesson.id, "title": lesson.title, "content": lesson.content} for lesson in lessons])

@api_bp.route("/users/<int:user_id>/progress", methods=["GET", "PUT"])
def user_progress(user_id):
    if request.method == "GET":
        progress = UserProgress.query.filter_by(user_id=user_id).all()
        return jsonify([{"lesson_id": p.lesson_id, "progress": p.progress} for p in progress])

    if request.method == "PUT":
        data = request.json
        progress_entry = UserProgress.query.filter_by(user_id=user_id, lesson_id=data["lesson_id"]).first()
        if progress_entry:
            progress_entry.progress = data["progress"]
        else:
            new_progress = UserProgress(user_id=user_id, lesson_id=data["lesson_id"], progress=data["progress"])
            db.session.add(new_progress)
        db.session.commit()
        return jsonify({"status": "progress updated"})
