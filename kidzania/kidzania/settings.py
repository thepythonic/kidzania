# Django settings for kidzania project.

import os

gettext = lambda s: s

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
    ('Dalia Shaaban', 'kidzania@scitecs.com'),
)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = 'scitecs123456'
# TODO YF change email settings
EMAIL_HOST_USER = 'kidzania@scitecs.com'
EMAIL_SUBJECT_PREFIX = 'kidzania - '
EMAIL_USE_TLS = True

SUBJECT_CHOICHES = (
    ('-Choose-', '-Choose-'),
    ('Question', 'Question'),
    ('Business proposal', 'Business proposal'),
    ('Advertising', 'Advertising'),
    ('Complaint', 'Complaint'),
)

CMS_PLUGIN_PROCESSORS = (
    'cmsplugin_wrapper.plugin_processors.wrap_plugin',
)

WRAPPER_PLUGIN_TEMPLATES = (
    ('default.html', 'default'),
    ('activities.html', 'Establishments'),
    ('template_1.txt', 'template_1'),
)

TITLED_PLUGIN_TEMPLATES = (
    ('default.html', 'Default'),
    ('default-without-image.html', 'Without Image Default'),
    ('kids.html', 'kids'),
    ('tab.html', 'Tab'),
    ('side-block-activities.html', 'Activities Side Block'),
    ('title-adjacent-text.html', 'Title adjacent to text'),
    ('plan-sideblock.html', 'Plan your visit Side Block'),
)

TITLED__IMAGE_TEXT_PLUGIN_TEMPLATES = (
    ('default.html', 'Default'),
    ('default-without-image.html', 'Without Image Default'),
    ('kids.html', 'kids'),
    ('tab.html', 'Tab'),
    ('side-block-activities.html', 'Activities Side Block'),
    ('title-adjacent-text.html', 'Title adjacent to text'),
    ('plan-sideblock.html', 'Plan your visit Side Block'),
)





MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'kidzania_dev',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'scitecskidzania',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

LANGUAGES = [
    ('en', 'English'),
    ('ar', 'Arabic'),
]

#SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    #'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0ots!#jf=q22wqv5y04_!+)ovk!q12n18%tg_$w%-ub(4hp7_='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    #'multihost.middleware.MultiHostMiddleware',

    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',

)
#MULTIHOST_AUTO_WWW = False
MULTIHOST_REDIRECT_URL = '/'

ROOT_URLCONF = 'kidzania.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'kidzania.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'cmsplugin_wrapper.context_processors.cmsplugin_wrapper',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.admin',
    
    # our themes
    'bstheme',
    #'bluetheme',

    'cms', 
    'mptt', 
    'menus', 
    'south',
    'sekizai', 
    'slider',
    # 'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    # 'cms.plugins.picture',
    'cms.plugins.snippet',
    # 'cms.plugins.teaser',
    'cms.plugins.text',
    # 'cms.plugins.video',
    'cms.plugins.twitter',
    
    'cmsplugin_text_variable_width',

    'easy_thumbnails',

    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    # Our Custom plugins
    'cmsplugin_bootstrap_carousel',     # CarouselPlugin
    'cmsplugin_titledplugin',           # TitledPlugin
    'cmsplugin_gallery',                # CMSGalleryPlugin
    #'cmsplugin_billybeezgames',         # BillybeezGamePlugin
    'cmsplugin_contact',                # ContactPlugin
    'cmsplugin_wrapper',                # CMSWrapperPlugin
    'cmsplugin_nivoslider',             # CMSSliderPlugin
    'custom_calendar',                  # CustomCalendarPlugin
    'cmsplugin_facebook',               #FacebookLikeBoxPlugin or FacebookLikeBoxPlugin
    'cmsplugin_titledimage',            #TitledImage
    #'cmsplugin_titledimagetext',        #TitledImageTextPlugin
)


CMS_TEMPLATES = (
    ('home.html', 'Home'),
    ('activities.html', 'Activities'),
    ('direction.html', 'Information'),
    ('play.html', 'Playground'),
    ('tabs.html', 'Tab Template'),
    ('404.html', 'Page Not Found Template'),
    ('500.html', 'Internal Server Error Template'),
)

#http://django-filer.readthedocs.org/en/latest/installation.html#subject-location-aware-cropping
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'cmsplugin_nivoslider.thumbnail_processors.pad_image',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

CMS_PAGE_MEDIA_PATH = 'cms_page_media/'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CMS_SEO_FIELDS = True

CMS_PLACEHOLDER_CONF = {
    'content_top': {
        'plugins': ['CMSTextVariableWidth', 'FilerImagePlugin', 'CarouselPlugin','TitledPlugin', 'CMSWrapperPlugin','TitledImagePlugin','TitledImageTextPlugin'],
        'name':gettext("Content Top"),
    },
    'content_center': {
        'plugins': ['CMSTextVariableWidth', 'FilerImagePlugin', 'TitledPlugin', 'CMSGalleryPlugin', 'Custom_Calendar','TitledImageTextPlugin'],
        'name':gettext("Content Center"),
    },
    'content_bottom': {
        'plugins': ['CMSTextVariableWidth', 'FilerImagePlugin', 'TitledPlugin', 'ContactPlugin','TitledImageTextPlugin'],
        'name':gettext("Content Bottom"),
    },
}

try:
    from local_settings import *
except ImportError:
    print "Exception"
