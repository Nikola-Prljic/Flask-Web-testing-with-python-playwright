import os
import mariadb
from dotenv import load_dotenv

def execute_sql_file(db, filename):
    try:
        with open(filename, 'r') as file:
            sql_commands = file.read().split(';')
            cursor = db.cursor()
            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)
            db.commit()
            cursor.close()
            print("Schema.sql executed successfully.")
    except Exception as e:
        print("Error executing schema.sql:", e)

def reset_database():
    try:
        load_dotenv()
        print(os.getenv('FLASK_DB_HOST'))
        db = mariadb.connect(
        host = os.getenv('FLASK_DB_HOST'),
        user = os.getenv("FLASK_DB_USERNAME"),
        passwd = os.getenv("FLASK_DB_PASSWORD"),
        db = os.getenv("FLASK_DB_DATABASE"),
        )

        execute_sql_file(db, 'tests/create_database/schema.sql')
        db.close()
        print("db closed")

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")