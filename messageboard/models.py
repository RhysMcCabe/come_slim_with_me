from django.db import models


class Discussion(models.Model):
    title = models.CharField(max_length=140)
    member = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    body = models.TextField(max_length=400)

    def __str__(self):
        return self.title
