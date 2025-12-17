from flask import Flask
from app.database import db
from app.config import Config
from app.controllers.employee_controller import employee_bp
from app.exceptions.error_handler import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(employee_bp)

    # register global exception handlers
    register_error_handlers(app)

    return app
