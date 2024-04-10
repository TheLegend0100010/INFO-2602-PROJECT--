from App.database import db

class Excercise(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    level = db.Column(db.String, nullable = False)
    muscle = db.Column(db.String, nullable = False)
    instructions = db.Column(db.String(300), nullable = False)
    
    def __init__(self, name, level, muscle, instructions):
        self.name = name
        self.level = level
        self.muscle = muscle
        self.instructions = instructions