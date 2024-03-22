import os
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from . import database
import flask_login
from . import userClass

from board import games, pages, posts, auth, database

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    database.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(games.bp)
    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return userClass.User.get(user_id)
        # Load a user from the user_id provided by Flask-Login

    return app
