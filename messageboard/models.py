from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime
from django.utils.text import slugify

#Topic model :  Each discussion is associated with a topic
#               A topic can have many discussions
class Topic(models.Model):
    name = models.CharField(max_length=140)
    member = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    description = models.TextField(max_length=400)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField(null=True, unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super (Topic, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


    def get_date_created(self):
        return self.date_created.strftime('created: %d/%m/%y at %H:%M')

#Discussion Model : A discussion can have only one topic
class Discussion(models.Model):
    topic = models.ForeignKey(
        Topic, related_name="discussions", on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    body = models.TextField(max_length=400)
    member = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='media/imageuploads/', blank=True)
    slug = models.SlugField(null=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super (Discussion, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('discussion_detail', args=[str(self.slug)])
    
    def get_date_created(self):
        return self.date_created.strftime('created: %d/%m/%y at %H:%M')

#Comment model :    A comment is associated with one discussion
#                   A discussion can have multiple comments
class Comment(models.Model):
    discussion = models.ForeignKey(
        Discussion,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.CharField(max_length=140)
    image = models.ImageField(upload_to='media/imageuploads/', blank=True)
    member = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('discussion_detail', args=[str(self.discussion.slug)])