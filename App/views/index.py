from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_jwt_extended import jwt_required
from App.models import Exercise
from App.controllers import create_user, create_routine, create_workout, create_exercise
from App.database import db
import json

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/loginpage', methods=['GET'])
def login_page():
    return render_template('login.html')    

@index_views.route('/signuppage', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@index_views.route('/profilepage', methods=['GET'])
@jwt_required()
def profile_page():
    return render_template('profile.html')

@index_views.route('/exercise/<int:id>', methods=['GET'])
def exercise(id):
    exercise = Exercise.query.filter_by(id=id).first()
    return render_template('exercise.html', exercise=exercise)


@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    create_user('rick', 'rickpass')
    with open('exercises.json', encoding = "ISO-8859-1") as file:
        exercises = json.load(file)
        records =[]
        # return jsonify(lenght=len(exercises['exercises']))
        for exercise in exercises['exercises']:
            image = exercise['name'].replace(' ', '_')
            image = image.replace('/', '_')
            imagelink = f"https://raw.githubusercontent.com/wrkout/exercises.json/master/exercises/{image}/images/0.jpg"
            instructions = ""
            for instruct in exercise['instructions']:
                instructions += instruct
            record = Exercise(exercise['name'], exercise['level'], exercise['primaryMuscles'][0], instructions, imagelink)
            records.append(record)
        db.session.bulk_save_objects(records)
        db.session.commit()
    create_routine()
    create_workout()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})