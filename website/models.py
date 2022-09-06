from time import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Users(db.Model, UserMixin):
    userId = db.Column(db.Integer, primary_key=True) #primary key
    userName = db.Column(db.String(150))
    userPassword = db.Column(db.String(250))
    userEmail = db.Column(db.String(150))
    userPhone = db.Column(db.String(100))

    blogs = db.relationship('Blogs')
    replies = db.relationship('Reply')

    def get_id(self):
           return (self.userId)
class Blogs(db.Model):
    blogId = db.Column(db.Integer,primary_key=True ) #primary key
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    title = db.Column(db.String(500))
    brief = db.Column(db.String(1000))
    desciption = db.Column(db.String(25000))
    userId = db.Column(db.Integer, db.ForeignKey('users.userId')) #foreign key
    
    replies = db.relationship('Reply')
    # users = db.relationship('Users')

class Reply(db.Model):
    replyId = db.Column(db.Integer,primary_key=True ) #primary key
    comments = db.Column(db.String(25000))
    userId = db.Column(db.Integer, db.ForeignKey('users.userId')) #foreign key
    blogId = db.Column(db.Integer, db.ForeignKey('blogs.blogId')) #foreign key





    # blogs = db.relationship('Blog')
    # users = db.relationship('Users')
