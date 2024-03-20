import secrets

key = secrets.token_hex()
f = open(".env", "w")
f.write("ENVIRONMENT=\"Development\"\n")
f.write(f"FLASK_SECRET_KEY={str(key)}\n")
f.write("FLASK_DB_HOST=localhost")
f.write("FLASK_DB_USERNAME=niki")
f.write("FLASK_DB_PASSWORD=ktmsx")
f.write("FLASK_DB_DATABASE=mydb")      
f.close()
