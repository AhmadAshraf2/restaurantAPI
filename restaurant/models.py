from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# class model for restaurant object
class Restaurant(models.Model):
    name = models.TextField()
    opens_at = models.TimeField()
    closes_at = models.TimeField()
