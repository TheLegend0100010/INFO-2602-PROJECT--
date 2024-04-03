from App.database import db
from .routine import Routine

class Workout(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    db.relationship('Routine', backref = "workout", lazy = True)

    def __init__(self):
        print(1)