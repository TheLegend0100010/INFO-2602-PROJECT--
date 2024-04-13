from App.database import db

class Exercise(db.Model):
    id = db.Column(db.Integer, autoincrement= True, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    level = db.Column(db.String(20), nullable = False)
    muscle = db.Column(db.String(20), nullable = False)
    instructions = db.Column(db.String(5000), nullable = False)
    image = db.Column(db.String(160), nullable = False)

    def __init__(self, name, level, muscle, image):
        self.name = name
        self.level = level
        self.muscle = muscle
        self.instructions = instructions
        self.image = image

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'level': self.level,
            'muscle': self.muscle,
            'instructions': self.instructions,
            'image': self.image
        }