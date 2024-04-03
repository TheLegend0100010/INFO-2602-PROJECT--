from App.database import db

class Routine(db.Model):
    id = db.Column(db.Integer, autoincrement = True)