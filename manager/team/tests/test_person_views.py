import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Person
from ..serializers import PersonSerializer


client = Client()


class CreateListPersonTest(TestCase):
    """Test Modulo for person creating and listing"""

    def setUp(self) -> None:
        self.valid_payload = {
            "first_name": "John",
            "last_name": "Wick",
            "email": "johnwick@gmail.com",
        }
        self.invalid_name_payload = {
            "first_name": "",
            "last_name": "Richard",
            "email": "bobrichard@gmail.com",
        }
        self.invalid_email_payload = {
            "person_name": "Bobby",
            "last_name": "Cat",
            "email": "@@",
        }
        Person.objects.create(first_name="test1", last_name="test1", email="test1@gmail.com")
        Person.objects.create(first_name="test2", last_name="test2", email="test2@gmail.com")

    # POST REQUEST
    def test_create_valid_person(self):
        response = client.post(
            reverse("list_create_person"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_name_invalid_person(self):
        response = client.post(
            reverse("list_create_person"),
            data=json.dumps(self.invalid_name_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_email_invalid_person(self):
        response = client.post(
            reverse("list_create_person"),
            data=json.dumps(self.invalid_email_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # GET REQUEST
    def test_list_person(self):
        response = client.get(reverse("list_create_person"))
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RetriveUpdateDeleteSinglePerson(TestCase):
    """Test Modulo for single person retriving updating deleting"""

    def setUp(self) -> None:
        self.person = Person.objects.create(first_name="test1", last_name="test1", email="test1@gmail.com")
        self.valid_payload = {
            "first_name": "updated test1",
            "last_name": "updated test1",
            "email": "updatedtes1@gmail.com",
        }
        self.valid_partial_payload = {"email": "partial@gmail.com"}
        self.invalid_payload = {"email": "11"}

    # GET REQUEST
    def test_get_valid_single_person(self):
        response = client.get(reverse("detail_update_destroy_person", kwargs={"pk": self.person.pk}))
        person = Person.objects.get(pk=self.person.pk)
        serializer = PersonSerializer(person)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_person(self):
        response = client.get(reverse("detail_update_destroy_person", kwargs={"pk": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # PUT REQUEST
    def test_valid_update_person(self):
        response = client.put(
            reverse("detail_update_destroy_person", kwargs={"pk": self.person.pk}),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # PATCH REQUEST
    def test_valid_partial_update_person(self):
        self.object = Person.objects.get(pk=self.person.pk)
        response = client.patch(
            reverse("detail_update_destroy_person", kwargs={"pk": self.person.pk}),
            data=json.dumps(self.valid_partial_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_person(self):
        response = client.put(
            reverse("detail_update_destroy_person", kwargs={"pk": self.person.pk}),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # DELETE REQUEST
    def test_valid_delete_person(self):
        response = client.delete(reverse("detail_update_destroy_person", kwargs={"pk": self.person.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_person(self):
        response = client.delete(reverse("detail_update_destroy_person", kwargs={"pk": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
