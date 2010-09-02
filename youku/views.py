# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from youku.models import Video, Log, User, PostedVideo, Suggestion
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from datetime import datetime
from django.views.generic.list_detail import object_list
from django.template import RequestContext
from django.contrib.comments.models import Comment
from tagging.views import tagged_object_list
from youku.forms import PostVideoForm, SuggestionForm, SubmitVideoForm
from django.conf import settings

def video_list_page(request):
    videos = Video.objects.all()
    comments = Comment.objects.order_by("-submit_date")[0:6]
    categories = Video.CATEGORY_CHOICES
    return object_list(request, template_name = 'index.html', queryset = videos, paginate_by=5, extra_context={'comments': comments, 'categories': categories})

def video_page(request, year, month, day, time):
    slug = year+'-'+month+'-'+day+'-'+time
    video = Video.objects.get(slug=slug)
    return render_to_response('video_page.html', {'video': video}, context_instance=RequestContext(request))

def category_page(request, category):
    videos = Video.objects.filter(category=category)
    comments = Comment.objects.order_by("-submit_date")[0:5]
    categories = Video.CATEGORY_CHOICES
    return object_list(request, template_name = 'index.html', queryset = videos, paginate_by=5, extra_context={'comments': comments, 'categories': categories})

def tag_page(request, tag):
    queryset = Video.objects.all()
    comments = Comment.objects.order_by("-submit_date")[0:5]
    categories = Video.CATEGORY_CHOICES
    return tagged_object_list(request, queryset, tag, paginate_by=5, template_name='index.html', extra_context={'comments': comments, 'categories': categories})

def log_page(request):
    logs = Log.objects.all()
    return object_list(request, template_name='upgrade_log.html', queryset=logs, paginate_by=10)

def post_video(request):
	if request.method == 'POST':
		form = PostVideoForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			pv = PostedVideo(title=cd['title'], url=cd['url'], tags=cd['tags'], reason=cd['reason'],)
			pv.save()
			return HttpResponseRedirect('/post/thanks/')
	else:
		form = PostVideoForm()
	return render_to_response('post_video.html', {'form': form}, context_instance=RequestContext(request))

def super_page(request):
	error = ''
	if request.method == 'POST':
		form = SubmitVideoForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			import urllib, re
			data = urllib.urlopen(cd['url']).read()
			result = re.search('<embed src="([^"]+)"', data)
			if result is None:
				error = "ËØ∑ËæìÂÖ•Ê≠£Á°ÆÁöÑ‰ºòÈÖ∑Âú∞ÂùÄ."
			else:
				sv = Video(title=cd['title'], url=cd['url'], flash_url=result.group(1), posted_by=User.objects.get(username='muer'), post_date=datetime.now(), category=cd['category'], tags=cd['tags'], intro=cd['intro'], slug=request.POST['slug'])
				sv.save()
				return HttpResponseRedirect('/super/')
	else:
		form = SubmitVideoForm()
	videos = PostedVideo.objects.all()
	suggestions = Suggestion.objects.order_by("-time")[0:8]
	return object_list(request, template_name='super_page.html', queryset=videos, paginate_by=30, extra_context={'form': form, 'error': error, 'suggestions':suggestions},)
	
def post_thanks(request):
	return render_to_response('post_thanks.html')
	
def suggestion(request):
	if request.method == 'POST':
		form = SuggestionForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			sug = Suggestion(name=cd['name'], email=cd['email'], content=cd['content'],)
			sug.save()
			return HttpResponseRedirect('/suggestion/thanks/')
	else:
		form = SuggestionForm()
	return render_to_response('suggestion.html', {'form': form}, context_instance=RequestContext(request))
	
def suggestion_thanks(request):
	return render_to_response('suggestion_thanks.html')

from django.core import serializers
from django.utils import simplejson
def rating(request, amnt):
	if request.is_ajax():
		mimetype = 'application/json'
		video = Video.objects.get(id=request.POST['video_id'])
		video.rating.add(amnt, request.user, request.META['REMOTE_ADDR'])
		data = serializers.serialize("json", [video])
		return HttpResponse(data,mimetype)
	else:
		return HttpResponse(status=400)

def comment(request, vid):
	video = Video.objects.get(id=vid)
	user = request.user
	return render_to_response('includes/comment.html', {'video': video, 'user': user})
    
def toplist(request, type):
	comments = Comment.objects.order_by("-submit_date")[0:6]
	categories = Video.CATEGORY_CHOICES
	if type == 'default':
		q = Video.objects.extra(select={'w_rating': 'rating_votes*100/(rating_votes+%s)*100/%s*rating_score/rating_votes/100+%s*100/(rating_votes+%s)*%s/100' % (settings.MINIMUM_VOTES_FOR_TOPLIST, Video.rating.range, settings.MINIMUM_VOTES_FOR_TOPLIST, settings.MINIMUM_VOTES_FOR_TOPLIST, settings.MEAN_VOTE_FOR_TOPLIST)})
		q = q.extra(order_by = ['-w_rating', '-rating_votes'])
		list = 'default'
		return object_list(request, template_name = 'toplist.html', queryset = q, paginate_by=5, extra_context={'comments': comments, 'categories': categories, 'list': list,})
	elif type == 'rating':
		q = Video.objects.extra(select={'a_rating': 'rating_score*100/%s/rating_votes' % (Video.rating.range)})
		q = q.extra(order_by = ['-a_rating', '-rating_votes'])
		list = 'rating'
		return object_list(request, template_name = 'toplist.html', queryset = q, paginate_by=5, extra_context={'comments': comments, 'categories': categories, 'list': list,})
	elif type == 'votes':
		q = Video.objects.extra(select={'a_rating': 'rating_score*100/%s/rating_votes' % (Video.rating.range)})
		q = q.extra(order_by = ['-rating_votes', '-a_rating'])
		list = 'votes'
		return object_list(request, template_name = 'toplist.html', queryset = q, paginate_by=5, extra_context={'comments': comments, 'categories': categories, 'list': list,})
	raise Http404