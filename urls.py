from django.conf.urls.defaults import *
from youku.feeds import LatestVideosFeed
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    (r'^', include('youku.urls')),
    # admin related
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/',  include('registration.backends.default.urls')),
    # static files
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
