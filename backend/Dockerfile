FROM ubuntu:latest


RUN apt update -y && apt install -yq  python3-dev python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --break-system-packages -r requirements.txt

COPY . /app

ENV FLASK_APP=run.py
ENV C_FORCE_ROOT="true"
ENV SQLALCHEMY_DATABASE_URI="sqlite:///easave.sqlite3"

RUN echo 'alias act="source env/bin/activate"' >> ~/.bashrc
RUN echo 'alias ee="export FLASK_APP=run.py && export FLASK_DEBUG=0"' >> ~/.bashrc

CMD [ "uwsgi", "--http", "0.0.0.0:5000", \
               "--protocol", "uwsgi", \
               "--master", \
               "--wsgi", "run:app" ]