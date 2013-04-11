import sys
sys.path.append('./lib/local')

# General
AUTHOR = u"Martin Rio"
SITENAME = u"OMBU: Web Development in Portland, Oregon"
TIMEZONE = 'US/Pacific'
DEFAULT_LANG = 'en'
DELETE_OUTPUT_DIRECTORY = True
DEFAULT_PAGINATION = False
THEME = 'theme'
PATH = 'src'
ARTICLE_DIR = 'null'
STATIC_PATHS = ['images']
PLUGINS = ['pelican.plugins.assets', ]
DIRECT_TEMPLATES = ('index',)
PAGINATED_DIRECT_TEMPLATES = ()

# Blog
BLOG_ENABLED = False
FEED_RSS = False
FEED_ATOM = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
USE_FOLDER_AS_CATEGORY = False

if BLOG_ENABLED == True:
    ARTICLE_DIR = 'posts'
    FEED_RSS = 'feeds/rss.xml'
    DEFAULT_PAGINATION = 10
    DIRECT_TEMPLATES = ('index','blog')
    PAGINATED_DIRECT_TEMPLATES = ('blog',)
    ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
    ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

from custom_filters import cdn
JINJA_FILTERS = {'cdn': cdn}
