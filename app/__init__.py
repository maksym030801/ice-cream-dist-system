from flask import Flask
# from app.routes import auth, orders, statistics
from app.routes import init_app
from app.models import db
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'optional_default')

    # We used sqlite db to show you my testing results.
    # But we sqlite is a lightweight db and is not proper for our project.
    # We should use mysql or any other db.
    # Sqlite is only for local simple test.
    # We can change easily sqlite db to mysql by updating one line.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../icecream2.db?timeout=20'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser:mypassword@127.0.0.1/icecreamdb'  # for mysql

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # auth.init_app(app)
    # orders.init_app(app)
    # statistics.init_app(app)
    init_app(app)

    db.init_app(app)
    with app.app_context():
        # Create all tables
        db.create_all()

    return app
