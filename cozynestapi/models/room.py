from django.db import models
from .user import User

class Room(models.Model):

    name = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    theme = models.CharField(max_length=50)
    mood = models.CharField(max_length=50)
    deadline = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
