from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

migrate = Migrate()
db = SQLAlchemy()

def fix_database_url(url):
    """
    Ensure the DATABASE_URL uses 'postgresql://' instead of 'postgres://'.
    """
    if url and url.startswith("postgres://"):
        return url.replace("postgres://", "postgresql://", 1)
    return url

def create_app(config_class=None):
    app = Flask(__name__)

    # Load configuration
    if config_class:
        app.config.from_object(config_class)
    else:
        # Fallback to environment-based DATABASE_URL
        app.config['SQLALCHEMY_DATABASE_URI'] = fix_database_url(os.getenv('DATABASE_URL'))
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.routes import main_routes, member_routes
    app.register_blueprint(main_routes)
    app.register_blueprint(member_routes)

    return app

