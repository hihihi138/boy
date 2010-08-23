# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from youku.models import Video

class PostVideoForm(forms.Form):
	title = forms.CharField(max_length=100, label='视频名称')
	url = forms.URLField(label='优酷地址')
	tags = forms.CharField(max_length=100, label='标签')
	reason = forms.CharField(widget=forms.Textarea, label='视频看点')
	
class SuggestionForm(forms.Form):
	name = forms.CharField(max_length=100, label='昵称')
	email = forms.EmailField(label='电子邮件')
	content = forms.CharField(widget=forms.Textarea, label='意见/建议')
	
class SubmitVideoForm(ModelForm):
	class Meta:
		model = Video
		fields = ('title', 'url', 'tags', 'category', 'intro', 'slug')
	#title = forms.CharField(max_length=100, label='视频名称')
	#url = forms.URLField(label='优酷地址')
	#tags = forms.CharField(max_length=100, label='标签')
	#category = forms.CharField(max_length=100, label='分类')
	#intro = forms.CharField(widget=forms.Textarea, required=False, label='视频简介')