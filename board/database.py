import os
import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext

def init_app(app):
    app.teardown_appcontext(close_db)
    """ init_db_command() """
    """ app.cli.add_command(init_db_command) """

""" @click.command("init-db") """
def init_db_command():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))

    """  click.echo("You successfully initialized the database!") """

def get_db():
    print(os.getenv('DB_HOST'))
    if "db" not in g:
        g.db = mysql.connector.connect(
            host = current_app.config['DB_HOST'],
            user = current_app.config["DB_USERNAME"],
            passwd = current_app.config["DB_PASSWORD"],
            db = current_app.config["DB_DATABASE"],
        )
    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()
