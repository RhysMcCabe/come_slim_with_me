from django.contrib import admin

from .models import Category, Todo


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Category)

admin.site.register(Todo)