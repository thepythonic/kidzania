from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from cms.sitemaps import CMSSitemap

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

handler404 = 'kidzania.site_utils.handler404'
handler500 = 'kidzania.site_utils.handler500'

if settings.DEBUG:
    urlpatterns = patterns('',
    	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       		{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    	url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
   		url(r'', include('django.contrib.staticfiles.urls')),
	) + urlpatterns