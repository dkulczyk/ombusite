#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys
sys.path.append('./lib/local')

BUILD_ENV = 'development'
AUTHOR = u"Martin Rio"
SITENAME = u"OMBU: Web Development in Portland, Oregon"
TIMEZONE = 'US/Pacific'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = True
THEME = 'theme'
PATH = 'src'
STATIC_PATHS = ['images']
FEED_ATOM = None
FEED_ALL_ATOM = None
FEED_RSS = None
PLUGINS = ['pelican.plugins.assets', ]
DIRECT_TEMPLATES = ('index','blog')
PAGINATED_DIRECT_TEMPLATES = ('blog',)
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

from custom_filters import cdn
JINJA_FILTERS = {'cdn': cdn}
