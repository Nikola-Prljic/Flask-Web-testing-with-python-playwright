from flask import Blueprint, request, render_template, redirect, url_for

bp = Blueprint("auth", __name__)

from board.database import get_db

@bp.route("/login")
def login():
    return render_template("auth/login.html")

@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username:               #need to check if user exist!!!
            db = get_db()
            db.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
            db.commit()
            return redirect(url_for("auth.login"))
    print("hello")
    return render_template("auth/register.html")

