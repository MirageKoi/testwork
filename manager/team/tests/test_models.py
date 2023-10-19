from django.test import TestCase
from ..models import Team, Member


class TeamModelTest(TestCase):
    """Test module for Team"""

    def setUp(self) -> None:
        Team.objects.create(title="First team")

    def test_team_title(self):
        team_1 = Team.objects.get(title="First team")
        self.assertEqual(team_1.title, "First team")


class MemberModelTest(TestCase):
    """Test module for Member Model"""

    def setUp(self) -> None:
        Member.objects.create(first_name="Bob", last_name="Cat", email="bobcat@gmail.com")
        Member.objects.create(first_name="Jack", last_name="Rich", email="jackrich@gmail.com")

    def test_Member_first_and_last_names(self):
        Member_1 = Member.objects.get(id=1)
        Member_2 = Member.objects.get(id=2)
        self.assertEqual((Member_1.first_name), "Bob")
        self.assertEqual((Member_1.last_name), "Cat")
        self.assertEqual((Member_2.first_name), "Jack")
        self.assertNotEqual((Member_2.last_name), "Wick")
