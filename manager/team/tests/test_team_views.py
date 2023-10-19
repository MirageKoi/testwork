import json
from rest_framework import status
from django.urls import reverse
from ..models import Team
from ..serializers import TeamSerializer
from rest_framework.test import APITestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

# Create a test case class for listing and creating teams
class CreateListTeamsTest(APITestCase):
    """Test Module for list create Team View"""

    def setUp(self) -> None:
        # Define valid and invalid payloads for team creation
        self.valid_payload = {"title": "red team"}
        self.invalid_payload = {"title": ""}
        
        # Create some test Team instances for testing
        Team.objects.create(title="first team")
        Team.objects.create(title="second team")
        Team.objects.create(title="third team")
        Team.objects.create(title="best team")

    # POST REQUEST tests for team creation
    def test_create_valid_team(self):
        # Test creating a valid team
        response = self.client.post(reverse("list_team"), (self.valid_payload), format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_team(self):
        # Test creating a team with an invalid title
        response = self.client.post(
            reverse("list_team"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # GET REQUEST tests for listing teams
    def test_get_all_teams(self):
        url = reverse("list_team")
        factory = APIRequestFactory()
        teams = Team.objects.all()
        request = factory.get(url)
        serializer_context = {
            "request": Request(request),
        }
        serializer = TeamSerializer(teams, context=serializer_context, many=True)
        response = self.client.get(reverse("list_team"))
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Create a test case class for retrieving, updating, and deleting single teams
class RetrieveUpdateDestroyTeamTest(APITestCase):
    """Test Module for retrieve update delete single team"""

    def setUp(self) -> None:
        # Create a test Team instance
        self.first = Team.objects.create(title="first team")
        
        # Define valid and invalid payloads for team updates
        self.valid_payload = {"title": "renew team name"}
        self.invalid_payload = {"title": ""}

    # GET REQUEST tests for retrieving a single team
    def test_get_valid_single_team(self):
        url = reverse("detail_team", kwargs={"pk": self.first.pk})
        factory = APIRequestFactory()
        team = Team.objects.get(pk=self.first.pk)
        request = factory.get(url)
        serializer_context = {
            "request": Request(request),
        }
        response = self.client.get(url)
        serializer = TeamSerializer(team, context=serializer_context)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_team(self):
        # Test retrieving an invalid team
        response = self.client.get(reverse("detail_team", kwargs={"pk": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # PUT REQUEST tests for updating a team
    def test_valid_update_team(self):
        response = self.client.put(
            reverse("detail_team", kwargs={"pk": self.first.pk}),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_team(self):
        # Test updating a team with an invalid payload
        response = self.client.put(
            reverse("detail_team", kwargs={"pk": self.first.pk}),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # DELETE REQUEST tests for deleting a team
    def test_valid_delete_team(self):
        response = self.client.delete(reverse("detail_team", kwargs={"pk": self.first.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_team(self):
        # Test deleting an invalid team
        response = self.client.delete(reverse("detail_team", kwargs={"pk": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
