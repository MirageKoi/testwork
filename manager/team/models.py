from django.db import models


# Define a Django model called Team
class Team(models.Model):
    # A field for the title of the team
    title = models.CharField(max_length=128, blank=False, null=False, unique=True)

    class Meta:
        # Specify the default ordering for queries on this model
        ordering = ["title"]

    def __str__(self) -> str:
        # Define a human-readable string representation for instances of this model
        return self.title


# Define a Django model called Member
class Member(models.Model):
    # Fields for first name, last name, and email
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    email = models.EmailField()

    # Create a foreign key relationship with the Team model.
    # When a team is deleted, set the team field to NULL.
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name="members")

    class Meta:
        # Specify the default ordering for queries on this model
        ordering = ["last_name"]

        # Create a unique constraint that enforces the uniqueness of the combination of
        # first_name, last_name, and email fields.
        unique_together = ["first_name", "last_name", "email"]

    def __str__(self) -> str:
        # Define a human-readable string representation for instances of this model
        return f"{self.first_name} {self.last_name} {self.email}"
