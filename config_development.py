#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys
sys.path.append('./lib/local')

BUILD_ENV = 'development'
AUTHOR = u"Martin Rio"
SITENAME = u"OMBU: Web Development in Portland, Oregon"
TIMEZONE = 'US/Pacific'
DELETE_OUTPUT_DIRECTORY = True
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
THEME = 'theme'
PATH = 'src'
STATIC_PATHS = ['images']
FEED_RSS = 'feeds/rss.xml'
FEED_ATOM = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
PLUGINS = ['pelican.plugins.assets', ]
DIRECT_TEMPLATES = ('index','blog')
PAGINATED_DIRECT_TEMPLATES = ('blog')
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
USE_FOLDER_AS_CATEGORY = False

from custom_filters import cdn
JINJA_FILTERS = {'cdn': cdn}
