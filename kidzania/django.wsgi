import os
import sys

sys.path.append('/home/dalia/Envs/Kidzania/lib/python2.7/site-packages')
sys.path.append('/home/dalia/projects/kidzania/kidzania/')
sys.path.append('/home/dalia/projects/kidzania/kidzania/apps/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'kidzania.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
