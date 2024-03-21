from flask import Blueprint, request, render_template, redirect, url_for
from click import echo
from flask import flash
from flask_login import login_user, current_user, login_required, logout_user

from board.userClass import User

bp = Blueprint("auth", __name__)

@bp.route("/login", methods=("GET", "POST"))
def login():
    if current_user.is_authenticated:
        return render_template("auth/home.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username and password:
            user = User.get(username)
            if user and user.password == password:
                login_user(user)
                flash('Logged in successfully.')
                return render_template("pages/home.html")
    return render_template("auth/login.html")

@bp.route("/register", methods=("GET", "POST"))
def register():
    if current_user.is_authenticated:
        return render_template("auth/home.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username and password:
            if User.add(username, password) == True:
                return redirect(url_for("auth.login"))
            #else
                #Do something if user name is taken!
    return render_template("auth/register.html")

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('pages.home'))
