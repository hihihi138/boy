from django.conf.urls.defaults import *
from feeds import LatestVideosFeed

site_feeds = {
	'video': LatestVideosFeed,
}

urlpatterns = patterns('youku.views',
    (r'^$', 'video_list_page'),
    (r'^video/(\d{4})-(\d{2})-(\d{2})-(\d{6})/$', 'video_page'),
    (r'^video/(\d{4})/(\d{2})/(\d{2})/(\d{6})/$', 'video_page'),
    (r'^log/$', 'log_page'),
    (r'^category/([^/]+)/$', 'category_page'),
    (r'^tag/([^/]+)/$', 'tag_page'),
    (r'^post/$', 'post_video'),
    (r'^post/thanks/$', 'post_thanks'),
    (r'^suggestion/$', 'suggestion'),
    (r'^suggestion/thanks/$', 'suggestion_thanks'),
    (r'^toplist/(?P<type>.*)/$', 'toplist'),
    # Ajax
    (r'^ajax/rating/(?P<amnt>\d)/$', 'rating'),
    (r'^ajax/post/$', 'super_page'),
    (r'^ajax/comment/(?P<vid>\d+)/$', 'comment'),
	# Admin operations
	(r'^super/$', 'super_page'),
)

urlpatterns += patterns('',
	(r'^comments/', include('django.contrib.comments.urls')),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': site_feeds}),
)