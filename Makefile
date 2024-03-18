PORT = 8000
DB_NAME = board.sqlite
CREATE_DB = python3 -m flask --app board init-db
START_FLASK = python3 -m flask --app board run --port ${PORT} --debug

all:
	@if [ ! -f ./.env ]; then \
		echo "\n---CREATE NEW .env---"; \
		python3 create_key.py; \
	fi;
	@if [ ! -f ./${DB_NAME} ]; then \
		echo "\n---CREATE NEW DATABASE---\nDB NAME: board.sqlite\n"; \
		${CREATE_DB}; \
	fi;
	@${START_FLASK}

clear:
	rm -f board.sqlite

fclear: clear
	rm -f .env

re: fclear all
