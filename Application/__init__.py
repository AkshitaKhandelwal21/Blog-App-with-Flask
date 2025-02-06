from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)


app.config['SECRET_KEY'] = 'asdfghjkl'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Application.db"

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)


from Application.routes import home
from Application.routes import users