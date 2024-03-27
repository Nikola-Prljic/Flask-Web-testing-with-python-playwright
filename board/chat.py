from flask import Blueprint, render_template
from flask_login import current_user

bp = Blueprint("chat", __name__)

@bp.route("/chat")
def home():
    if current_user.is_authenticated:
        return render_template("chat/chat.html")
    return render_template("pages/login.html")