from flask import (
    Blueprint, 
    redirect,
    render_template,
    request,
    url_for,
)

import json

from click import echo

from database import get_db

from flask_login import login_required, current_user

bp = Blueprint("posts", __name__)

@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        author = current_user.username
        message = request.form["message"]
        if message:
            db = get_db()
            cursor = db.cursor(dictionary=True)
            cursor.execute(
                "INSERT INTO post (author, message) VALUES (%s, %s)",
                (author, message)
            )
            cursor.close()
            db.commit()
            return redirect(url_for("posts.posts"))
    return render_template("posts/create.html")

@bp.route("/posts")
@login_required
def posts():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, author, message, created FROM post ORDER BY created DESC")
    posts = cursor.fetchall()
    cursor.close()
    return render_template("posts/posts.html", posts=posts)