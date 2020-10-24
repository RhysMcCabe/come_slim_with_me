from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=140)
    member = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    description = models.TextField(max_length=400)

    def __str__(self):
        return self.name


class Discussion(models.Model):
    title = models.CharField(max_length=140)
    member = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    body = models.TextField(max_length=400)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('discussion', args=[str(self.id)])

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
