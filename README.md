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
images:

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


## Static asset building with Gulp

### Docker

The `docker-compose.yml` file includes a container that runs node and does the
Gulp compilation of front-end assets. If for some reason the container isn't
building correctly, shut the container down and remove the `node_modules`
directory and `package-lock.json` file (if it exists) and start the container
again.

    rm -rf application/website/static/website/node_modules
    rm application/website/static/website/package-lock.json

**Don't commit the `package-lock.json` file.** The contents of it can change
depending on where `npm install` was run and can cause problems on other
machines.

### Local

If you'd rather not run the asset compilaiton in a docker container you can
run it locally as long as you have node >= 8 and npm >= 5.

    cd application/website/static/website/
    npm install
    npm run start

If you have trouble with the install or compilation, do the same as above and
remove the `node_modules` directory and `package-lock.json` file and run
`npm install` again. **Don't commit the `package-lock.json` file.**
