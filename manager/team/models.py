from django.db import models
from django.utils.text import slugify


class TeamModel(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False, unique=True)

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    email = models.EmailField()
    team = models.ForeignKey(TeamModel, on_delete=models.SET_NULL, null=True, related_name="persons")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.first_name} {self.last_name} {self.email}")
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["last_name"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.email}"
