from django.db import models


class TeamModel(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)


class Person(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    email = models.EmailField()
