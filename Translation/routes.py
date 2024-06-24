from flask import Flask, redirect, render_template, request, url_for

from Translation import UserMixin, app, db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/features')
def features():
    return render_template('features.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('signin.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('signup.html')



@app.route('/feed',methods=['GET', 'POST'])
def feedback():
    render_template('feedback.html')



@app.route('/dash',methods=['GET', 'POST'])
def dashboard():
    render_template('dashboard.html')

