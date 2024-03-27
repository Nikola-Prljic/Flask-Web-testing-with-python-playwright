PORT = 8001
DB_NAME = board.sqlite
CREATE_DB = python3 -m flask --app board init-db
START_FLASK = python3 -m flask --app board run --host="0.0.0.0" --port ${PORT} --debug --use-socketio

.PHONY: all clear fclear docker

all:
	@python3 docker/create_key.py
	@python3 board/__init__.py

start-flask:
	@python3 board/__init__.py

clear:
	rm -f board.sqlite

fclear: clear
	rm -f .env

re: fclear all

docker:
	python3 docker/create_env_docker.py
	docker-compose up
	docker-compose stop

docker-stop:
	docker-compose down
	docker volume rm flask-web-testing-with-python-playwright_datadir

docker-fclear:
	docker image prune --all --force
