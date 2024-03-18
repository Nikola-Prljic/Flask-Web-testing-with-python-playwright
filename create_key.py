import secrets

key = secrets.token_hex()
f = open(".env", "w")
f.write("ENVIRONMENT=\"Development\"\n")
f.write(f"FLASK_SECRET_KEY={str(key)}\n")
f.write("FLASK_DATABASE=board.sqlite\n")        
f.close()
