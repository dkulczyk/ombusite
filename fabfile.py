from fabric.api import task, local, execute


@task
def build(config='config_development.py'):
    """
    Build the site (uses the development configuration by default)
    """
    local('pelican -s %s -d' % config)


@task
def deploy():
    """
    Deploy to production
    """
    bucket = 's3://ombuweb.com'
    max_age = 864000

    # Build for production
    execute('build', 'config_production.py')

    # Delete old files
    local('aws --quiet --region us-west-2 s3 rm --recursive %s' % bucket)

    # Upload new files
    local('aws --quiet --region=us-west-2 s3 sync --cache-control '
          '"max-age=%s" --acl '
          'public-read output %s' % (max_age, bucket, ))
