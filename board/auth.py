from flask import Blueprint, request, render_template, redirect, url_for
from click import echo

from board.userClass import User

bp = Blueprint("auth", __name__)

from board.database import get_db

@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username and password:
            user = User.get(username, None)
            if user and user.password == password:
                return render_template("pages/home.html")
    return render_template("auth/login.html")

@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username and password:
            if User.add(username, password) == True:
                return redirect(url_for("auth.login"))
            #else
                #Do something if user name is taken!
    return render_template("auth/register.html")

