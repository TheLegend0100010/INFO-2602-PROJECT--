from App.models import Exercise
from App.database import db

def create_exercise(name, level, muscle, image):
    exercise = Exercise(name, level, muscle, image)
    db.session.add(exercise)
    db.session.commit()
    return exercise
