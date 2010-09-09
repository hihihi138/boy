# Django settings for bestyouku project.
import os
import socket

ROOT_PATH = os.path.dirname(__file__)

if socket.gethostname() == 'harness-test.bej.corp.google.com':
	DEBUG = True
	TEMPLATE_DEBUG = DEBUG
	
	DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
	DATABASE_NAME = ROOT_PATH+'/bestyouku.db'             # Or path to database file if using sqlite3.
	DATABASE_USER = ''             # Not used with sqlite3.
	DATABASE_PASSWORD = ''         # Not used with sqlite3.
	DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
	DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.
	
	# Email Host
	EMAIL_HOST = 'smtp.gmail.com'
	EMAIL_HOST_USER = 'bestyouku520@gmail.com'
	EMAIL_HOST_PASSWORD = 'youkujingxuan'
	EMAIL_PORT = 587
	EMAIL_USE_TLS = True
else:
	DEBUG =	TEMPLATE_DEBUG = Flase
	
	DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
	DATABASE_NAME = 'bestyouku_mydata'             # Or path to database file if using sqlite3.
	DATABASE_USER = 'bestyouku'             # Not used with sqlite3.
	DATABASE_PASSWORD = '3351808'         # Not used with sqlite3.
	DATABASE_HOST = 'mysql.alwaysdata.com'             # Set to empty string for localhost. Not used with sqlite3.
	DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.
	
	EMAIL_HOST = 'smtp.alwaysdata.com'
	EMAIL_HOST_USER = 'bestyouku@alwaysdata.net'
	EMAIL_HOST_PASSWORD = '3351808'
	EMAIL_PORT = 587
	EMAIL_USE_TLS = True
	DEFAULT_FROM_EMAIL = 'no-reply@bestyouku.com'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('Muer', 'hihihi138@gmail.com'),
)
SEND_BROKEN_LINK_EMAILS = True
MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-CN'

SITE_ID = 3

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(ROOT_PATH, 'public/site_media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '10u5%x8a4#q97s$tst+)t_a=1*a+90q@wdch4ew1fs!wjxi)#3'

ACCOUNT_ACTIVATION_DAYS = 7

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    #'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'boy.urls'

TEMPLATE_DIRS = os.path.join(ROOT_PATH, 'templates')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.comments',
    'django.contrib.sitemaps',
    'youku',
    'tagging',
    'registration',
    'djangoratings',
)

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
MINIMUM_VOTES_FOR_TOPLIST = 3
MEAN_VOTE_FOR_TOPLIST = 3.44
