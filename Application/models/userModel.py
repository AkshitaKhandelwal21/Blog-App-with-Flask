from Application import app, db, login
from sqlalchemy.orm import *
from Application.models.postModel import Post
from flask_login import UserMixin

@login.user_loader
def userByID(user_id):
    id = User.query.get(int(user_id))
    return id


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    image_file = db.Column(db.String(25), nullable=False, default='default.jpg')
    password = db.Column(db.String(40), nullable=False)
    posts = relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return (self.username, self.email, self.phone)
    