import os
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager

from board import pages, posts, auth, database

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    database.init_app(app)

    """ login_manager = LoginManager()
    login_manager.init_app(app) """

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    app.register_blueprint(auth.bp)
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")
    return app
