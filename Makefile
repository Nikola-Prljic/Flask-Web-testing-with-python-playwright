PORT = 8000
DB_NAME = board.sqlite
CREATE_DB = python3 -m flask --app board init-db
START_FLASK = python3 -m flask --app board run --port ${PORT} --debug

all:
	@if [ ! -f ./${DB_NAME} ]; then \
		echo "\n---CREATE NEW DATABASE---\nDB NAME: board.sqlite\n"; \
		${CREATE_DB}; \
	fi;
	@${START_FLASK}

clear:
	rm -f board.sqlite

re: clear all
