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

admin.site.register(Discussion, DiscussionAdmin)

admin.site.register(Topic)

admin.site.register(Comment)