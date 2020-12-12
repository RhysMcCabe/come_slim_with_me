from django.contrib.auth.models import AbstractUser
from django.db import models
import birthday

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    