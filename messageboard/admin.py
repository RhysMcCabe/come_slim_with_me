from .models import Topic, Discussion, Comment
from django.contrib import admin

from .models import Discussion

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class DiscussionAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

class DiscussionInLine(admin.TabularInline):
    model = Discussion
    extra = 0

class TopicAdmin(admin.ModelAdmin):
    inlines = [
        DiscussionInLine
    ]

admin.site.register(Discussion, DiscussionAdmin)

admin.site.register(Topic, TopicAdmin)

admin.site.register(Comment)