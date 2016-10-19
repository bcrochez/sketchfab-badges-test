from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.


class SketchfabUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_signin = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return "User " + self.user.username


class Model3D(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " by " + self.user.username


class Badge(models.Model):
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return "Badge " + self.title
