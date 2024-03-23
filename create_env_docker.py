import secrets
import linecache

if linecache.getline('.env', 1) == "compose env\n":
    exit(0)

flask_key = secrets.token_hex()
db_pw = secrets.token_hex()
db_root_pw = secrets.token_hex()

f = open(".env", "w")

f.write("compose env\n")
f.write("ENVIRONMENT=\"Development\"\n")
f.write(f"FLASK_SECRET_KEY={str(flask_key)}\n")
f.write("FLASK_DB_HOST=0.0.0.0\n")
f.write("FLASK_DB_USERNAME=niki\n")
f.write(f"FLASK_DB_PASSWORD={str(db_pw)}\n")
f.write("FLASK_DB_DATABASE=mydb\n")
f.write("FLASK_DB_PORT=3307\n")

f.write("MARIADB_DATABASE=mydb\n")
f.write(f"MARIADB_ROOT_PASSWORD={str(db_root_pw)}\n")
f.write(f"MARIADB_PASSWORD={str(db_pw)}\n")
f.write("MARIADB_USER=niki\n")
f.write("MYSQL_TCP_PORT=3307\n")

f.close()