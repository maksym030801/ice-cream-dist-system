from flask import Flask
from .auth import auth_bp
from .orders import orders_bp
from .statistics import stats_bp

def init_app(app: Flask):
    app.register_blueprint(auth_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(stats_bp)
