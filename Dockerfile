FROM python:3.12

RUN apt update
RUN apt-get install libmariadb-dev -y
RUN apt-get install python3-dev -y

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "make"]