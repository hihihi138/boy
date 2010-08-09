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
from youku.forms import PostVideoForm, SuggestionForm

def video_list_page(request):
    videos = Video.objects.all()
    comments = Comment.objects.order_by("-submit_date")[0:6]
    categories = Video.CATEGORY_CHOICES
    return object_list(request, template_name = 'index.html', queryset = videos, paginate_by=5, extra_context={'comments': comments, 'categories': categories})

def video_page(request, year, month, day, time):
    dt = datetime.strptime(year+month+day+time, "%Y%m%d%H%M%S")
    video = Video.objects.get(post_date=dt)
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

def posted_videos(request):
    videos = PostedVideo.objects.all()
    return object_list(request, template_name='posted_videos.html', queryset=videos, paginate_by=10)
	
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