from django.contrib import admin

from .models import Category, Todo

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','member')

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('title', 'description', 'created', 'date_completed', 'member', 'category',)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Todo, TodoAdmin)