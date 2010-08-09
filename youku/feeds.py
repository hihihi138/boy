# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from youku.models import Video

class LatestVideosFeed(Feed):
	title = "优酷视频精选"
	link = "/rss/"
	description = "优酷精选的最新更新."
	
	def items(self):
		return Video.objects.all()
		
	def item_title(self, item):
		return item.title
		
	def item_link(self, item):
		return "/video/" + item.vid
		
	def item_description(self, item):
		return item.title
	
	def item_pubdate(self, item):
		return item.post_date
		
	def item_author_name(self, item):
		return item.posted_by
		
	item_copyright = "版权所有 (c) 2010, Muer"