from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# from app.routes import books

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Ensure secure storage of user passwords
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a secure, random key

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    
    from app.routes.auth import bp as auth_bp  # Update this import
    from app.routes.books import bp as books_bp
    from app.routes.reviews import bp as reviews_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(reviews_bp)

    return app
