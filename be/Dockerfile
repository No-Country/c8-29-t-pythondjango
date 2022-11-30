FROM python:3.10-slim-bullseye

WORKDIR /app

#RUN apt-get update && apt-get install -y libpq-dev gdal-bin libgdal-dev
RUN pip install --upgrade pip

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./ ./

CMD python3 manage.py migrate && \
    python3 manage.py runserver 0.0.0.0:8000
