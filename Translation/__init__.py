from Translation import routes
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '1234567890'
