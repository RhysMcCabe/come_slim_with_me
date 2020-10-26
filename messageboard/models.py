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

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])


class Discussion(models.Model):
    topic = models.ForeignKey(
        Topic, related_name="discussion", on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    body = models.TextField(max_length=400)
    member = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('discussion_list', args=[str(self.id)])


class Comment(models.Model):
    discussion = models.ForeignKey(
        Discussion,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.CharField(max_length=140)
    member = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('discussion_detail', args=[str(self.discussion.pk)])
