from django.contrib import admin
from youku.models import Video, Log, PostedVideo, Suggestion

class VideoAdmin(admin.ModelAdmin):
	list_display = ('title', 'posted_by', 'post_date', 'slug', 'url')
	search_fields = ('title',)
	list_filter = ('post_date', 'category')
	date_hierarchy = 'post_date'
	raw_id_fields = ('posted_by',)

admin.site.register(Video, VideoAdmin)
admin.site.register(Log)
admin.site.register(PostedVideo)
admin.site.register(Suggestion)