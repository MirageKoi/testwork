import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import TeamModel
from ..serializers import TeamSerializer


# Initialize the APIClient app
client = Client()


class CreateListTeamsTest(TestCase):
    """Test Module for list create Team View"""

    def setUp(self) -> None:
        self.valid_payload = {"title": "red team"}
        self.invalid_payload = {"title": ""}
        TeamModel.objects.create(title="first team")
        TeamModel.objects.create(title="second team")
        TeamModel.objects.create(title="third team")
        TeamModel.objects.create(title="best team")

    # POST REQUEST
    def test_create_valid_team(self):
        response = client.post(
            reverse("list_create_team"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_team(self):
        response = client.post(
            reverse("list_create_team"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # GET REQUEST
    def test_get_all_teams(self):
        response = client.get(reverse("list_create_team"))
        teams = TeamModel.objects.all()
        serializer = TeamSerializer(teams, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RetrieveUpdateDestroyTeamTest(TestCase):
    """Test Module for retrieve update delete single team"""

    def setUp(self) -> None:
        self.first = TeamModel.objects.create(title="first team")
        self.valid_payload = {"title": "renew team name"}
        self.invalid_payload = {"title": ""}

    # GET REQUEST
    def test_get_valid_single_team(self):
        response = client.get(reverse("detail_update_destroy_team", kwargs={"pk": self.first.pk}))
        team = TeamModel.objects.get(pk=self.first.pk)
        serializer = TeamSerializer(team)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_team(self):
        response = client.get(reverse("detail_update_destroy_team", kwargs={"pk": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # PUT REQUEST
    def test_valid_update_team(self):
        response = client.put(
            reverse("detail_update_destroy_team", kwargs={"pk": self.first.pk}),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_team(self):
        response = client.put(
            reverse("detail_update_destroy_team", kwargs={"pk": self.first.pk}),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # DELETE REQUEST
    def test_valid_delete_team(self):
        response = client.delete(reverse("detail_update_destroy_team", kwargs={"pk": self.first.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_team(self):
        response = client.delete(reverse("detail_update_destroy_team", kwargs={"pk": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
