from fabric.api import task, env, local, run, cd, execute
from fabric.contrib.project import rsync_project

@task
def dev():
    """
    The dev server definition
    """
    env.config_file = 'config_development.py'

@task
def qa():
    """
    The qa server definition
    """
    env.config_file = 'config_development.py'
    env.hosts = ['pepe']
    env.host_type = 'qa'
    env.host_webserver_user = 'www-data'
    env.host_site_path = '/var/www/qa14/current'


@task
def production():
    """
    The production server definition
    """
    env.config_file = 'config_production.py'
    env.hosts = ['ombu@shared1.ombuweb.com']
    env.host_type = 'production'
    env.user = 'ombu'
    env.host_webserver_user = 'nginx'
    env.host_site_path = '/home/ombu/webapps/ombuweb'


@task
def deploy():
    """
    Deploy a commit to a host
    """
    execute(build)
    rsync_project(
        remote_dir=env.host_site_path,
        local_dir='output/',
        delete=True
    )
    if env.host_type == 'production':
        run("cd %(host_site_path)s && find -type d -exec chmod 0755 {} \; && find -type f -exec chmod 0644 {} \;" % env)

@task
def build():
    """
    Build the site
    """
    local('pelican -s %s -d' % env.config_file)
