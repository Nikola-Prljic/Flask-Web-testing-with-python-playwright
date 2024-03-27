from flask import Blueprint, request, render_template, redirect, url_for
from click import echo
from flask import flash
from flask_login import login_user, current_user, login_required, logout_user

from userClass import User

bp = Blueprint("auth", __name__)

def get_login_data(*args):
    username = request.form[args[0]]
    password = request.form[args[1]]
    error = False
    if len(username) < 1:
        error = True
        flash("Username is empty")
    if len(password) < 1:
        error = True
        flash("Password is empty")
    return dict({"name" : username, "pass" : password, "error" : error})

@bp.route("/login", methods=("GET", "POST"))
def login():
    if current_user.is_authenticated:
        return render_template("pages/home.html")
    if request.method != "POST":
        return render_template("auth/login.html")

    login_data = get_login_data("username", "password")
    print(login_data["error"])
    if login_data["error"] == True:
        return render_template("auth/login.html")

    user = User.get(login_data["name"])
    if user and user.password == login_data["pass"]:
        login_user(user)
        return render_template("pages/home.html")
    else:
        flash("Username or password is wrong")
    return render_template("auth/login.html")

@bp.route("/register", methods=("GET", "POST"))
def register():
    if current_user.is_authenticated:
        return render_template("pages/home.html")
    if request.method == "POST":

        login_data = get_login_data("username", "password")
        if login_data["error"] == True:
            return render_template("auth/register.html")
        if login_data["name"] and login_data["pass"]:
            if User.add(login_data["name"], login_data["pass"]) == True:
                return redirect(url_for("auth.login"))
            flash('Name is already taken')
    return render_template("auth/register.html")

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('pages.home'))
