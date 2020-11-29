FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN python3.9 -m pip install --upgrade pip
RUN pip3.9 install setuptools
RUN pip3.9 install -r /requirements.txt
RUN mkdir /app
WORKDIR /app
COPY . ./app
RUN adduser -D user
USER user
