from django.db import models
from .piece import Piece
from .style import Style

class PieceStyle(models.Model):
    piece = models.ForeignKey(Piece, on_delete = models.CASCADE)
    style = models.ForeignKey(Style, on_delete = models.CASCADE)
