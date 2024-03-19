from flask_login import UserMixin
from board.database import get_db
from click import echo 

class User(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def get(username, db):
        if db is None:
            db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT username, password FROM users WHERE username = (%s);", [username])
        user_data = cursor.fetchall()
        cursor.close()
        if user_data:
            return User(user_data[0]["username"], user_data[0]["password"])
        return None

    def add(username, password):
        db = get_db()
        user = User.get(username, db)
        if user is not None:
            return False
        cursor = db.cursor(dictionary=True)
        cursor.execute("INSERT INTO users (username,password) VALUES (%s,%s)", (username,password))
        cursor.close()
        db.commit()
        return True
