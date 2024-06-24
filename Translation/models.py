from Translation import LoginManager, app, db

with app.app_context():
    db.create_all()
