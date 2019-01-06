OMBU Website
============

The OMBU Website runs on Django.

Installation
------------

### Installation steps

Obtain the code:

    git clone git@github.com:ombu/ombusite.git ombusite
    cd ombusite

Start all services:

    docker-compose up -d

Run `manage.py` commands:

    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser

To clean up (stop and remove containers, networks, images, and volumes):

        docker-compose down

### Build a Docker image

Docker Compose will automatically build missing images when running the `up`
task. The `build` task is also available when updating or troubleshooting
images:  

    docker-compose build web
