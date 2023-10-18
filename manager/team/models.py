from django.db import models


class TeamModel(models.Model):
    title = models.CharField(max_length=128)


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()