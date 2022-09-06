
from flask import Blueprint, render_template, request, jsonify, url_for, redirect, flash
from . import db
from .models import Users, Reply, Blogs
import json
from sqlalchemy import func, Date, desc
from datetime import date
from flask_login import login_user, login_required, logout_user, current_user


views = Blueprint('views', __name__)

#dashboard
@views.route('/dashboard',methods=['GET','POST'])
def dashboard():
    if request.method == 'POST':
        title = request.form.get('title')
        brief = request.form.get('brief')
        if len(title) < 1:
            flash('Blog title is too short!', category='error')
        else:
            new_blog = Blogs(brief=brief,title=title, user_id=current_user.id)
            db.session.add(new_blog)
            db.session.commit()
            flash('Blog added!', category='success')
    blogs = Blogs.query.all()
    print(blogs)
    users = Users.query.all()
    return render_template('dashboard.html',blogs=blogs,users=users)