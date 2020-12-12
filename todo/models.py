from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime

class Category(models.Model): 
    name = models.CharField(max_length=100)
    member = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    
    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    member = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,)
    category = models.ForeignKey(
        Category, related_name="todos", on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["-created"]

    def get_absolute_url(self):
        return reverse('todo_detail', args=[str(self.id)])

    def __str__(self):
        return self.title  