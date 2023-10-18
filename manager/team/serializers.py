from rest_framework import serializers
from .models import TeamModel, Person


class TeamSerializer(serializers.ModelSerializer):
    persons = serializers.HyperlinkedRelatedField(
        queryset=Person.objects.prefetch_related("team"),
        view_name="detail_update_destroy_person",
        many=True,
        lookup_field="slug",
    )

    class Meta:
        model = TeamModel
        fields = ["id", "title", "persons"]


class PersonSerializer(serializers.ModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        queryset=TeamModel.objects.all(), view_name="detail_update_destroy_team", lookup_field="title", allow_null=True
    )

    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email", "team"]
