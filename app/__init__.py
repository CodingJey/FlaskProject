from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create instances of Flask extensions
db = SQLAlchemy()

def create_app(config_name='development'):
    # Create the Flask application
    app = Flask(__name__)

    # Load configuration settings based on the provided config_name
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    # Initialize Flask extensions
    db.init_app(app)
    ma.init_app(app)

    # Import and register blueprints
    from app.routes.user_routes import user_blueprint
    from app.routes.other_entity_routes import other_entity_blueprint

    app.register_blueprint(user_blueprint)
    app.register_blueprint(other_entity_blueprint)

    return app
