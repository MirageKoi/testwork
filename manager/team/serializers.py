from rest_framework import serializers
from .models import Team, Member


# Create a serializer for the Member model
class MemberSerializer(serializers.ModelSerializer):
    # Create a hyperlinked identity field for the Member profile
    # As we use default DRF templates so we going to add HyperLinks for better instances navigating on web page
    profile = serializers.HyperlinkedIdentityField(view_name="detail_member", read_only=True)

    # Create a slug related field for the Team
    team = serializers.SlugRelatedField(
        queryset=Team.objects.all(), required=False, slug_field="title", allow_null=True
    )

    # Create a hyperlinked related field for the Team link
    team_link = serializers.HyperlinkedRelatedField(
        view_name="detail_team",
        read_only=True,
        source="team",
    )

    class Meta:
        model = Member
        # Define the fields to include in the serialized representation
        fields = ["profile", "first_name", "last_name", "email", "team", "team_link"]


# Create a serializer for the Team model
class TeamSerializer(serializers.ModelSerializer):
    # Create a hyperlinked identity field for the Team profile
    team_profile = serializers.HyperlinkedIdentityField(view_name="detail_team", lookup_field="pk")

    # Create a hyperlinked related field for the Members
    members = serializers.HyperlinkedRelatedField(
        queryset=Member.objects.prefetch_related("team"),
        view_name="detail_member",
        many=True,
        lookup_field="pk",
        required=False,
    )

    class Meta:
        model = Team
        # Define the fields to include in the serialized representation
        fields = ["title", "team_profile", "members"]
