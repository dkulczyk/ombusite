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
    env.config_file = 'config_production.py'
    env.hosts = ['ombu@d2.ombuweb.com:34165']
    env.host_type = 'qa'
    env.user = 'ombu'
    env.host_webserver_user = 'www-data'
    env.host_site_path = '/mnt/main/qa/qa2/public'


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
def push(ref='origin/master'):
    """
    Deploy a commit to a host
    """
    execute(build)
    rsync_project(
        remote_dir=env.host_site_path,
        local_dir='output/',
        delete=True
    )
    if env.host_type != 'production':
        run("chown -R %(user)s:%(host_webserver_user)s %(host_site_path)s "
            "&& chmod -R 02750 %(host_site_path)s" % env)
    else:
        run("cd %(host_site_path)s && find -type d -exec chmod 0755 {} \; && find -type f -exec chmod 0644 {} \;" % env)

@task
def build():
    """
    Build the site
    """
    local('pelican -s %s -d' % env.config_file)
