from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

migrate = Migrate()
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.routes import main_routes, member_routes
    app.register_blueprint(main_routes)
    app.register_blueprint(member_routes)

    return app
