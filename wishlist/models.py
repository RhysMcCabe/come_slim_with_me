from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


class Wishlist(models.Model):
    name = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


    def get_date_created(self):
        return self.date_created.strftime('created: %d/%m/%y at %H:%M')
