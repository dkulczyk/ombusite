OMBU Website
============

The OMBU Website runs on Django.

Installation
------------

### Prerequisites

You will need the following software properly installed on your computer:

- Git
- Docker

### Installation steps

- Obtain the code:

        git clone git@github.com:ombu/ombusite.git ombusite
        cd ombusite

- Start all services:

        docker-compose -f docker/docker-compose.yml up

### More tips

- Spare some typing:

        alias doco="docker-compose -f docker/docker-compose.yml"
        doco up

- Or, start each service individually:

        doco up db
        doco up web
        doco up gulp

- Run `manage.py` commands. For example, to setup a fresh DB:

        doco run web python manage.py migrate        
        doco run web python manage.py build_test_content
        doco run web python manage.py createsuperuser


### Build a Docker image

    doco build web
