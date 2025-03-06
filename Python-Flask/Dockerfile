FROM ubuntu
#FROM python:3.9.10-slim-buster

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install pipx
RUN apt-get -y install python3-venv
RUN python3 -m venv my-venv
RUN my-venv/bin/pip install flask

#RUN pipx install flask
#RUN pipx install flask-mysql

WORKDIR /opt/source-code

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run --host=0.0.0.0:5000
#CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0:5000"]

#EXPOSE 5000 5000