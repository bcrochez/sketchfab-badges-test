from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.


class SketchfabUser(models.Model):

    def __str__(self):
        return "User " + self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_signin = models.DateTimeField(default=datetime.now)


class Model3D(models.Model):

    def __str__(self):
        return self.name + " by " + self.user.username

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    views = models.IntegerField(default=0)
