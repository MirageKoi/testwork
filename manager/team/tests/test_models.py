from django.test import TestCase
from ..models import TeamModel, Person


class TeamModelTest(TestCase):
    """Test module for TeamModel"""

    def setUp(self) -> None:
        TeamModel.objects.create(title="First team")

    def test_team_title(self):
        team_1 = TeamModel.objects.get(title="First team")
        self.assertEqual(team_1.title, "First team")


class PersonModelTest(TestCase):
    """Test module for PersonModel"""

    def setUp(self) -> None:
        Person.objects.create(
            first_name="Bob", last_name="Cat", email="bobcat@gmail.com"
        )
        Person.objects.create(
            first_name="Jack", last_name="Rich", email="jackrich@gmail.com"
        )

    def test_person_first_and_last_names(self):
        person_1 = Person.objects.get(id=1)
        person_2 = Person.objects.get(id=2)
        self.assertEqual((person_1.first_name), "Bob")
        self.assertEqual((person_1.last_name), "Cat")
        self.assertEqual((person_2.first_name), "Jack")
        self.assertNotEqual((person_2.last_name), "Wick")
