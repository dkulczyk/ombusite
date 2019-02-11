FROM python:3-slim

MAINTAINER OMBU

# Hack to make postgresql-client install work on slim
RUN mkdir -p /usr/share/man/man1 \
    && mkdir -p /usr/share/man/man7 && \
    apt-get update && apt-get install -y \
    python \
    postgresql-client \
    libpq-dev \
    libjpeg-dev && \
    rm -rf /var/lib/apt/lists/*

VOLUME /var/www/ombusite.local

WORKDIR /var/www/ombusite.local

ENV DJANGO_SETTINGS_MODULE=website.settings.docker

ADD requirements/base.txt requirements/development.txt requirements/

RUN pip install -r requirements/development.txt

ADD . /var/www/ombusite.local

EXPOSE 8000

ENTRYPOINT  ["./docker/wait-for-postgres.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
