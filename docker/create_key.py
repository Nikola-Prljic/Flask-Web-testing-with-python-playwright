import secrets
import linecache

if linecache.getline('.env', 1) == "local env\n":
    exit(0)

key = secrets.token_hex()
f = open(".env", "w")
f.write("local env\n")
f.write("ENVIRONMENT=\"Development\"\n")
f.write(f"FLASK_SECRET_KEY={str(key)}\n")
f.write("FLASK_DB_HOST=0.0.0.0\n")
f.write("FLASK_DB_USERNAME=niki\n")
f.write("FLASK_DB_PASSWORD=ktmsx\n")
f.write("FLASK_DB_DATABASE=mydb\n")    
f.write("FLASK_DB_PORT=3306\n")
f.close()
