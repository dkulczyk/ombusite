Ombusite on Docker
==================

Build your images:

    docker build -f docker/Dockerfile -t ombu/website:devel .
   
Run the container:

    docker run \
    -v /Users/axolx/docker-volumes/ombusite:/var/www/ombusite.local \
    -p 80:8000 --name ombusite ombu/website:devel

This will run a simple webserver on the `output` directory, so you should be
able to access the site through the ip or hostname of your Docker host.

Invoke Pelican commands:

    docker exec ombusite pelican -s config_development.py -d -v

