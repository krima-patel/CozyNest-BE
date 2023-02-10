from django.db import models
from .room import Room
from .user import User

class Piece(models.Model):
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    piece_type = models.CharField(max_length=50)
    image_url = models.CharField(max_length=200)
    source = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    # style = models.Charfield(max_length=50)
    # need to create custom property for style for many to many relationship
