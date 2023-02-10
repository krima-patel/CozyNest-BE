from django.db import models

class Style(models.Model):
    style = models.CharField(max_length=50)
