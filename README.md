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

Visit `http://localhost/`

To clean up (stop and remove containers, networks, images, and volumes):

        docker-compose down

### Build a Docker image

Docker Compose will automatically build missing images when running the `up`
task. The `build` task is also available when updating or troubleshooting
images:  w

    docker-compose build web


Remote environments
-------------------

The AWS resources that run the remote environments are provisioned by the 
CloudFormation templates in this repository. 

Export AWS credentials to the shell environment:

        export AWS_ACCESS_KEY_ID=...
        export AWS_SECRET_ACCESS_KEY=...
        export AWS_DEFAULT_REGION=us-west-2

Provide required SSM parameters, global and for the desired `<env>`:

- `/ombusite/github_access_token`
- `/ombusite/<env>/database_password`

For example:

    aws ssm put-parameter \
        --name /ombusite/<env>/database_password \
        --type "String" \
        --value "<password>"

Launch a remote environment:

    ./infrastructure/scripts/stack-launch <env> 

Record the stack name in SERVICES_STACK_<env> in file `infrastructure/scripts/_env`.

Update the application stack:

    ./infrastructure/scripts/stack-update <env> 
