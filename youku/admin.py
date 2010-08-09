from django.contrib import admin
from youku.models import Video, Log, PostedVideo, Suggestion

admin.site.register(Video)
admin.site.register(Log)
admin.site.register(PostedVideo)
admin.site.register(Suggestion)