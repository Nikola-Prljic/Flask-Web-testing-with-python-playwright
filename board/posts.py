from flask import (
    Blueprint, 
    redirect,
    render_template,
    request,
    url_for,
)

import json

from click import echo

from board.database import get_db

bp = Blueprint("posts", __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        message = request.form["message"]
        if message:
            db = get_db()
            cursor = db.cursor(dictionary=True)
            """ cursor.execute("SELECT post_number FROM posts WHERE id = (SELECT MAX(id) FROM posts)")
            row = cursor.fetchone()
            next_post_number = row['post_number']
            next_post_number = next_post_number + 1
            echo(next_post_number) """
            cursor.execute(
                "INSERT INTO post (author, message) VALUES (%s, %s)",
                (author, message)
            )
            """ cursor.commit() , (SELECT IFNULL(MAX(post_number), 0) + 1 FROM post) """
            cursor.close()
            db.commit()
            return redirect(url_for("posts.posts"))

    return render_template("posts/create.html")

@bp.route("/posts")
def posts():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, author, message, created FROM post ORDER BY created DESC")
    posts = cursor.fetchall()
    cursor.close()
    return render_template("posts/posts.html", posts=posts)