from rest_framework import serializers
from .models import TeamModel, Person


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
