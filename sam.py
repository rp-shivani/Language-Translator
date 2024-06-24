from flask import Flask, redirect, render_template, request, url_for,jsonify
from flask_bcrypt import Bcrypt
from flask_login import (LoginManager, UserMixin, login_required, login_user,
                         logout_user)
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import EqualTo, InputRequired, Length, ValidationError
import os




# def get_translation_client():
#     return translate.Client()

# def translate_text(text, target_language):
#     client = get_translation_client()
#     result = client.translate(text, target_language=target_language)
#     translated_text = result['translatedText']
#     return translated_text
from translate import Translator
from langdetect import detect

# from Translation import db, UserMixin
# from Translation import app

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.config['SECRET_KEY'] = '1234567890'

LoginManager = LoginManager(app)
LoginManager.login_view = 'login'


@LoginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


db = SQLAlchemy(app)

Bcrypt = Bcrypt(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/features')
def features():
    return render_template('features.html')


@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user:
#             if Bcrypt.check_password_hash(user.password, form.password.data):
#                 login_user(user)
#                 return redirect(url_for('index'))
#     return render_template('signin.html', form=form)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if Bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                next_page = request.args.get('next')
                if next_page and not next_page == url_for('login'):
                    return redirect(next_page)
                return redirect(url_for('translator'))
    return render_template('signin.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/feed',methods=['GET', 'POST'])
def feedback():
    return render_template('feedback.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = Bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)




from deep_translator import GoogleTranslator
from gtts import gTTS
def translate_text(text, target_language):
    translated = GoogleTranslator(source='auto', target=target_language).translate(text)
    return translated

# @app.route('/translator', methods=['GET', 'POST'])
# def translator():
#     if request.method == 'POST':
#         text_to_translate = request.form['text']
#         target_language = request.form['target_language']
#         translated_text = translate_text(text_to_translate, target_language)
#         return render_template('translator.html', translated_text=translated_text)
#     return render_template('translator.html')



def translate_text(text, target_language):
    translated = GoogleTranslator(source='auto', target=target_language).translate(text)
    return translated

def speak_text(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("translated_audio.mp3")
    os.system("start translated_audio.mp3")  # For Windows

@app.route('/translator', methods=['GET', 'POST'])
def translator():
    if request.method == 'POST':
        text_to_translate = request.form['text']
        target_language = request.form['target_language']
        translated_text = translate_text(text_to_translate, target_language)
        speak_text(translated_text, lang=target_language)  # Speak the translated text
        return render_template('translator.html', translated_text=translated_text)
    return render_template('translator.html')



# def translate_text(text, target_language):
#     translated = GoogleTranslator(source='auto', target=target_language).translate(text)
#     return translated

# def generate_audio(text, lang='en'):
#     tts = gTTS(text=text, lang=lang, slow=False)
#     audio_file = "translated_audio.mp3"
#     tts.save(audio_file)
#     return audio_file

# @app.route('/translator', methods=['POST', 'GET'])
# def translator():
#     text_to_translate = request.form['text']
#     target_language = request.form['target_language']
#     translated_text = translate_text(text_to_translate, target_language)
#     audio_file = generate_audio(translated_text, lang=target_language)
#     audio_url = request.url_root + audio_file
#     return jsonify({'translated_text': translated_text, 'audio_url': audio_url})


















if __name__ == '__main__':
    with app.app_context():
        print("ffffffffffffffffffffffffffffffffffff")
        db.create_all()
        print('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
    app.run(debug=True)
