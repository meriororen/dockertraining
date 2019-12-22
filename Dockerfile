FROM ubuntu

RUN apt update
RUN apt install -y python python-pip

RUN pip install flask
RUN pip install flask-mysql

COPY . /opt/source-code/

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run -h 0.0.0.0 -p 8000
