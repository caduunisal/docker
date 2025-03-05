#FROM ubuntu
FROM python:3.9.10-slim-buster

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip

RUN pip install Flask
RUN pip install flask-mysql

COPY . /opt/source-code

#ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0:5000"]