FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY setup.py /usr/src/app/
RUN pip install -e .

COPY . /usr/src/app