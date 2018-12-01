from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app, test_data=False, load_init_data=True):
    db.app = app
    db.init_app(app)
    db.create_all()
