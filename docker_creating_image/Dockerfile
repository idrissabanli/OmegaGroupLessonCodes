FROM python:3.9.10
ARG DIR=/code

WORKDIR $DIR

COPY . .

RUN apt update

RUN pip install -r requirements.txt

ENV FLASK_APP="app.py"

# CMD [ "flask", "run", "-h", "0.0.0.0", "-p", "5000" ]

# docker run -p 5002:5000 omega:1.0.0