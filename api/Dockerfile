FROM python:3.6

ADD . /code

WORKDIR /code

RUN pip install --upgrade pip \
  && pip install -r requirements.txt

EXPOSE 5000
