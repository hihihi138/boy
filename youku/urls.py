from django.conf.urls.defaults import *
from feeds import LatestVideosFeed

site_feeds = {
	'video': LatestVideosFeed,
}

urlpatterns = patterns('',
    (r'^$', 'youku.views.video_list_page'),
    (r'^video/(\d{4})-(\d{2})-(\d{2})-(\d{6})/$', 'youku.views.video_page'),
    (r'^video/(\d{4})/(\d{2})/(\d{2})/(\d{6})/$', 'youku.views.video_page'),
    (r'^log/$', 'youku.views.log_page'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^category/([^/]+)/$', 'youku.views.category_page'),
    (r'^tag/([^/]+)/$', 'youku.views.tag_page'),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': site_feeds}),
    (r'^post/$', 'youku.views.post_video'),
    (r'^post/thanks/$', 'youku.views.post_thanks'),
    (r'^suggestion/$', 'youku.views.suggestion'),
    (r'^suggestion/thanks/$', 'youku.views.suggestion_thanks'),
    # Ajax
    (r'^ajax/rating/(?P<amnt>\d)/$', 'youku.views.rating'),
    (r'^ajax/post/$', 'youku.views.super_page'),
    (r'^ajax/comment/(?P<vid>\d+)/$', 'youku.views.comment'),
	# Admin operations
	(r'^super/$', 'youku.views.super_page'),
)