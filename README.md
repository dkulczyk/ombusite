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

Visit `http://localhost:8000`

To clean up (stop and remove containers, networks, images, and volumes):

        docker-compose down

### Build a Docker image

Docker Compose will automatically build missing images when running the `up`
task. The `build` task is also available when updating or troubleshooting
images:  w

    docker-compose build web


Remote environments
-------------------

### Running the remote application locally for testing

    docker build -t ombusite_remote -f application/docker/Dockerfile.remote application
    docker run -e DOMAIN=localhost -p 5000:5000 ombusite_remote

Visit `http://localhost:5000`

### Launching remote environments

The AWS resources that run the remote environments are provisioned by the 
CloudFormation templates in this repository. 

Export AWS credentials to the shell environment:

        export AWS_ACCESS_KEY_ID=...
        export AWS_SECRET_ACCESS_KEY=...
        export AWS_DEFAULT_REGION=us-west-2

Provide required SSM parameters, global and for the desired `<env>`:

- `/ombusite/github_access_token`
- `/ombusite/<env>/database_password`
- `/ombusite/<env>/version`

For example:

    aws ssm put-parameter \
        --name /ombusite/<env>/database_password \
        --type "String" \
        --value "<password>"

Launch a remote environment:

    ./infrastructure/scripts/stack-launch <env> <component>
    
Where component is one of `application` or `pipeline`:

- Application: Provide the application
- Pipeline: Provides a continuous deployment pipeline

Record the names of the stacks created with stack-launch in the 
`infrastructure/scripts/_env` files, under the variables:
`APPLICATION_STACK_<env>` and `PIPELIME_STACK_<env>` 

Update the a stack:

    ./infrastructure/scripts/stack-update <env> <component>
