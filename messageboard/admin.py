from .models import Topic
from django.contrib import admin

from .models import Discussion
admin.site.register(Discussion)

admin.site.register(Topic)
