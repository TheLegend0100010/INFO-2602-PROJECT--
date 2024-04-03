from App.models import Workout
from App.database import db

def create_workout():
    workout = Workout()
    db.session.add(workout)
    db.session.commit()
    return workout