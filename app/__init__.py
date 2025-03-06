from flask import Flask
from app.utils.db import init_db
from app.routes.project_routes import project_bp
from app.routes.file_routes import file_bp
from app.routes.llm_routes import llm_bp


def create_app():
    app = Flask(__name__)

    # Initialize Database
    init_db(app)

    # Register Blueprints (Modular Routes)
    app.register_blueprint(project_bp)
    app.register_blueprint(file_bp)
    app.register_blueprint(llm_bp)

    return app