from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)


app.config['SECRET_KEY'] = 'asdfghjkl'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Application.db"

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login = LoginManager(app)
login.login_view = '/login'


from Application.routes import home
from Application.routes import users
from Application.routes import posts