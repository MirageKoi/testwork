from django.db import models

class TeamModel(models.Model):
    title = models.CharField(max_length=128)
    