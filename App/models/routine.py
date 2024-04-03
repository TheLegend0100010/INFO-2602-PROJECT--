from App.database import db

class Routine(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    def __init__(self):
        print(1)