import os
import logging
from pelican import signals
from pelican.generators import Generator
from pelican.contents import is_valid_content
from contents import Project
from pelican.readers import Readers

"""
This file is the plugin entry point. Use this plugin by registering it in the
Pelican config

    PLUGINS = ['pelican_plugin_ombu_work.plugin', ... ]
"""

logger = logging.getLogger(__name__)


class ProjectsGenerator(Generator):
    """Generate projects"""
    def __init__(self, *args, **kwargs):
        self.projects = []
        self.readers = Readers(kwargs.get('settings'))
        super(ProjectsGenerator, self).__init__(*args, **kwargs)

    def generate_context(self):
        all_projects = []
        hidden_projects = []
        for f in self.get_files(
                os.path.join(self.path, self.settings['PROJECT_DIR'])):
            try:
                project = self.readers.read_file(
                    base_path=self.path, path=f, content_class=Project)
            except Exception, e:
                logger.warning(u'Could not process %s\n%s' % (f, str(e)))
                continue

            if project.status == "published":
                all_projects.append(project)
            elif project.status == "hidden":
                hidden_projects.append(project)
            else:
                logger.warning(u"Unknown status %s for file %s, skipping it." %
                               (repr(unicode.encode(project.status, 'utf-8')),
                                repr(f)))

        self.projects = all_projects
        self.hidden_projects = hidden_projects

        self._update_context(('projects', ))
        self.context['PROJECTS'] = self.projects


def get_generators(generators):
    return ProjectsGenerator


def register():
    signals.get_generators.connect(get_generators)
