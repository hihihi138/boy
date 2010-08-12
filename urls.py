from django.conf.urls.defaults import *
from youku.feeds import LatestVideosFeed
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.views import login, logout
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from youku.models import Video

video_dict = {
	'queryset': Video.objects.all(),
	'date_field': 'post_date',
}

sitemaps = {
	'video': GenericSitemap(video_dict, changefreq="weekly", priority=0.6),
}

urlpatterns = patterns('',
    (r'^', include('youku.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    # admin related
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/',  include('registration.backends.default.urls')),
    # static files
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)