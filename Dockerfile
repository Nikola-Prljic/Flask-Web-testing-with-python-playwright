FROM python:3.12

RUN apt update
RUN apt-get install mariadb-client -y
RUN apt-get install libmariadb-dev -y
RUN apt-get install python3-dev -y

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Specify your application's dependencies (like a database) and command to run your application
CMD ["make"]
