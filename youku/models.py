# -*-coding:utf-8 -*-
from __future__ import division
from django.db import models
from datetime import datetime
from tagging.fields import TagField
from tagging.models import Tag
from django.contrib.auth.models import User
from djangoratings.fields import RatingField
from djangoratings.models import Vote
from django.conf import settings

class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name='视频名称')
    url = models.URLField(verbose_name='优酷网址')
    flash_url = models.URLField(verbose_name='Flash地址')
    posted_by = models.ForeignKey(User, verbose_name='发布人')
    post_date = models.DateTimeField(default=datetime.now(), verbose_name='发布时间')
 #   tag = models.CharField(max_length=100, verbose_name='标签')
    CATEGORY_CHOICES = (
	('animal', '动物世界'),
	('funny', '轻松搞笑'),
	('animation', '动画短片'),
	('amazing', '不可思议'),
	('emotional', '真情感人'),
	('other', '其它'),
    )
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name='分类')
    tags = TagField(verbose_name='标签')
    intro = models.TextField(max_length=4096, blank=True, verbose_name='视频简介')
    rating = RatingField(range=5, weight=0, can_change_vote=True, allow_anonymous=True)
    slug = models.SlugField(max_length=40, default=datetime.now().strftime("%Y-%m-%d-%H%M%S"))
    
    def get_star_length(self):
    	return self.rating.get_rating()*25
    	
    def get_weighted_rating(self):
    	all_votes = Vote.objects.count()
    	average_rating = self.rating.get_rating()
    	minimum_votes = settings.MINIMUM_VOTES_FOR_TOPLIST
    	mean_vote = settings.MEAN_VOTE_FOR_TOPLIST
    	weighted_rating = (all_votes/(all_votes+minimum_votes))*average_rating+(minimum_votes/(all_votes+minimum_votes))*mean_vote
    	return weighted_rating
    
    def get_tags(self):
		return Tag.objects.get_for_object(self)
	
    def get_absolute_url(self):
        return '/video/%s' % self.slug

    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-post_date']

class Log(models.Model):
    log_title = models.CharField(max_length=100)
    log_content = models.TextField(max_length=4096)
    log_time = models.DateTimeField(default=datetime.now())
    
    def __unicode__(self):
		return self.log_title
    class Meta:
		ordering = ['-log_time']

class PostedVideo(models.Model):
	title = models.CharField(max_length=100, verbose_name='题目')
	url = models.URLField(verbose_name='优酷网址')
	post_date = models.DateTimeField(default=datetime.now(), verbose_name='发布时间')
	tags = models.CharField(max_length=100, verbose_name='标签')
	reason = models.TextField(verbose_name='推荐语')
	
	def __unicode__(self):
		return self.title
		
	class Meta:
		ordering = ['-post_date']
		
class Suggestion(models.Model):
	name = models.CharField(max_length=100, verbose_name='昵称')
	email = models.EmailField(verbose_name='电子邮箱')
	content = models.TextField(max_length=4096)
	time = models.DateTimeField(default=datetime.now())
	
	def __unicode__(self):
		return self.name