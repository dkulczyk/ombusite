FROM python:2.7-slim

MAINTAINER Martin Rio

RUN apt-get update && apt-get install -y \
    build-essential \
	git \
	npm \
	python \
	python-dev \
	python-setuptools && \
	rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/nodejs /usr/bin/node && \
    npm install -g less@1.3.1

RUN easy_install pip

COPY . /var/www/ombusite.local

RUN pip install -r /var/www/ombusite.local/requirements.txt

WORKDIR /var/www/ombusite.local

EXPOSE 8000

CMD cd output && python -m SimpleHTTPServer 8000
