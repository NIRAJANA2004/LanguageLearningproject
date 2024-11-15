from . import db
from .models import Lesson

def populate_database():
    lesson1 = Lesson(title="Introduction to French", content="Learn basic French words...")
    lesson2 = Lesson(title="Advanced Spanish Grammar", content="Understand complex Spanish grammar rules...")
    db.session.add_all([lesson1, lesson2])
    db.session.commit()
