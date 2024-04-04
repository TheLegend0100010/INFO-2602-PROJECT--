from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_jwt_extended import jwt_required
from App.models import db
from App.controllers import create_user, create_routine, create_workout

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

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    create_user('rick', 'rickpass')
    create_routine()
    create_workout()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})