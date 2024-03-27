import os
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
import database
import flask_login
import userClass
import chat
from flask_socketio import SocketIO
import ioChat

import games, pages, posts, auth, database

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    database.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(games.bp)
    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    app.register_blueprint(chat.bp)
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {os.getenv('FLASK_DB_PORT')}")

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return userClass.User.get(user_id)

    socketio = SocketIO(app)

    ioChat.ioHandler(socketio)

    return app, socketio


if __name__ == "__main__":
    app, socketio = create_app()
    socketio.run(app, host='0.0.0.0', port=8001, debug=True, allow_unsafe_werkzeug=True)
