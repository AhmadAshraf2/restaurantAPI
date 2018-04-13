from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.TextField()
    opens_at = models.TimeField()
    closes_at = models.TimeField()
