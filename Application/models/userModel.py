from Application import app, db
from sqlalchemy.orm import *
from Application.models.postModel import Post

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(25), nullable=False, default='default.jpg')
    password = db.Column(db.String(40), nullable=False)
    posts = relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return (self.username, self.email, self.phone)
    