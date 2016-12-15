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

    docker exec ombusite pelican -s config_development.py -d -v --relative-urls

Production Deployment
---------------------

To invoke fab taks that talk to AWS, export the AWS_ACCESS_KEY_ID, 
AWS_SECRET_ACCESS_KEY and AWS_DEFAULT_REGION variables to the environment for
 a user with sufficient access in AWS.

    docker run \
    -v /Users/axolx/docker-volumes/ombusite:/var/www/ombusite.local \
    -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION \
    ombu/website:devel \
    fab deploy 
