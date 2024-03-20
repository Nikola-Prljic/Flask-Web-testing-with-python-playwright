from flask import Blueprint, render_template
from flask_login import current_user

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    if current_user.is_authenticated:
        return render_template("pages/about.html")
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")
