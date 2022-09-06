from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy() 

DB_NAME = "database.db"
# SQL_SERVER_USER_PASS_IP_PORT = 'DESKTOP-CJEOG7N\SQLEXPRESS'

basedir = path.abspath(path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    # encrypts the cookie data
    
    
    #app.config['SQLALCHEMY_DATABASE_URI'] = r'mssql+pyodbc://{}/{}?driver=SQL+Server+Native+Client+11.0'.format(SQL_SERVER_USER_PASS_IP_PORT, DB_NAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///' + path.join(basedir, DB_NAME)
    print("server connected!")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "ajmi"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Users,Blogs,Reply
    
    db.create_all(app=app)

    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(id):
    #     return Users.query.get(int(id))

    return app

