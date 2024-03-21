PORT = 8000
DB_NAME = board.sqlite
CREATE_DB = python3 -m flask --app board init-db
START_FLASK = python3 -m flask --app board run --host="0.0.0.0" --port ${PORT} --debug

all:
	@if [ ! -f ./.env ]; then \
		echo "\n---CREATE NEW .env---"; \
		python3 create_key.py; \
	fi;
	@${START_FLASK}

clear:
	rm -f board.sqlite

fclear: clear
	rm -f .env

re: fclear all

docker:
	docker-compose up -d
	@${START_FLASK}
	docker-compose stop

docker-stop:
	docker-compose down
	docker volume rm flask-web-testing-with-python-playwright_datadir
	docker image prune --all --force 
