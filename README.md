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

The up command should result in the website running `http://localhost`.

- One can also control the website services individually:

        doco up db
        doco up web
        doco up gulp

- One can also interact with `manage.py` in the web service. For example,
  to setup a fresh DB:

        doco run web python manage.py migrate        
        doco run web python manage.py createsuperuser

- To clean up (stop and remove containers, networks, images, and volumes):

        doco down

### Build a Docker image

Docker Compose will automatically build missing images when running the `up`
task. The `build` task is also available when updating or troubleshooting
images:  

    doco build web
