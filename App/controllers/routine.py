from App.models import Routine
from App.database import db

def create_routine():
    routine = Routine()
    db.session.add(routine)
    db.session.commit()
    return routine