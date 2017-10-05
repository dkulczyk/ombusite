LMS on Docker
=============

Build your images:

    docker build -f docker/Dockerfile.devel -t nwpp/lms:devel .

Start all services:

    docker-compose -f docker/docker-compose.yml up

Spare some typing:

    alias doco="docker-compose -f docker/docker-compose.yml"
    doco up

Or, start each service individually:

    doco up db
    doco up web
    doco up gulp

Run `manage.py` commands. For example, to setup a fresh DB:

    doco run web python manage.py migrate
    doco run web python manage.py build_test_content
    doco run web python manage.py createsuperuser
