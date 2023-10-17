from django.test import TestCase
from ..models import TeamModel

class TeamTest(TestCase):
    """ Test module for Team """

    def setUp(self) -> None:
        TeamModel.objects.create(title="First team")

    def test_team_title(self):
        team_1 = TeamModel.objects.get(title="First team")
        self.assertEqual(team_1.title, "First team")