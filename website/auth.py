from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user
from website import views, auth
from .models import Users, Blogs, Reply
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
import json
from sqlalchemy import update

auth = Blueprint('auth', __name__)

@auth.route('/' , methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userEmail = request.form.get('userEmail')
        userPassword = request.form.get('userPassword')

        user = Users.query.filter_by(userEmail=userEmail).first()
        if user:
            if check_password_hash(user.userPassword, userPassword):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.dashboard'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html")



@auth.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'POST':
        userEmail = request.form.get('userEmail')
        userName = request.form.get('userName')
        userPassword = request.form.get('userPassword')
        

        user = Users.query.filter_by(userEmail=userEmail).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(userEmail) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(userName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(userPassword) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = Users(userEmail=userEmail, userName=userName, userPassword=userPassword)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.dashboard'))
    return render_template("register.html")
