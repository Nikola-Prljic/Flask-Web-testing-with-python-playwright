from flask import Blueprint, render_template
from flask_login import current_user

bp = Blueprint("games", __name__)

@bp.route("/games")
def game():
    if current_user.is_authenticated:
        return render_template("games/game.html")
    return render_template("pages/home.html")
