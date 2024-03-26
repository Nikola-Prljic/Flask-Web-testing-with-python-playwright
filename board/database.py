import sys
import os
import mariadb
import click
from flask import current_app, g
from flask.cli import with_appcontext
import flask_login

def init_app(app):
    app.teardown_appcontext(close_db)

def get_db():
    if "db" not in g:
        try:
            g.db = mariadb.connect(
                host = current_app.config['DB_HOST'],
                user = current_app.config["DB_USERNAME"],
                passwd = current_app.config["DB_PASSWORD"],
                db = current_app.config["DB_DATABASE"],
                port = current_app.config["DB_PORT"],
            )
            return g.db
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()
