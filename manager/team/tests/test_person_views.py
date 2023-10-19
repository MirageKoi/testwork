import json
from rest_framework import status
from django.urls import reverse
from ..models import Member
from ..serializers import MemberSerializer
from rest_framework.test import APITestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


# Create a test case class for creating and listing members
class CreateListMemberTest(APITestCase):
    """Test Module for Member creating and listing"""

    def setUp(self) -> None:
        # Define valid and invalid payloads for member creation
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
            "first_name": "Bobby",
            "last_name": "Cat",
            "email": "@@",
        }

        # Create some test Member instances for testing
        Member.objects.create(first_name="test1", last_name="test1", email="test1@gmail.com")
        Member.objects.create(first_name="test2", last_name="test2", email="test2@gmail.com")

    # POST REQUEST tests for member creation
    def test_create_valid_member(self):
        # Test creating a valid member
        response = self.client.post(
            reverse("list_member"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_name_invalid_member(self):
        # Test creating a member with an invalid name
        response = self.client.post(
            reverse("list_member"),
            data=json.dumps(self.invalid_name_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_email_invalid_member(self):
        # Test creating a member with an invalid email
        response = self.client.post(
            reverse("list_member"),
            data=json.dumps(self.invalid_email_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # GET REQUEST tests for listing members
    def test_list_member(self):
        factory = APIRequestFactory()
        Members = Member.objects.all()
        request = factory.get(reverse("list_member"))
        serializer_context = {
            "request": Request(request),
        }
        response = self.client.get(reverse("list_member"))
        serializer = MemberSerializer(Members, context=serializer_context, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Create a test case class for retrieving, updating, and deleting single members
class RetrieveUpdateDeleteSingleMember(APITestCase):
    """Test Module for single Member retrieving, updating, deleting"""

    def setUp(self) -> None:
        # Create a test Member instance
        self.member = Member.objects.create(first_name="test1", last_name="test1", email="test1@gmail.com")

        # Define valid and invalid payloads for member updates
        self.valid_payload = {
            "first_name": "updated test1",
            "last_name": "updated test1",
            "email": "updatedtest1@gmail.com",
        }
        self.valid_partial_payload = {"email": "partial@gmail.com"}
        self.invalid_payload = {"email": "11"}

    # GET REQUEST tests for retrieving a single member
    def test_get_valid_single_member(self):
        factory = APIRequestFactory()
        member = Member.objects.get(pk=self.member.pk)
        request = factory.get(reverse("detail_member", kwargs={"pk": self.member.pk}))
        serializer_context = {
            "request": Request(request),
        }
        response = self.client.get(reverse("detail_member", kwargs={"pk": self.member.pk}))
        serializer = MemberSerializer(member, context=serializer_context)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_member(self):
        # Test retrieving an invalid member
        response = self.client.get(reverse("detail_member", kwargs={"pk": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # PUT REQUEST test for updating a member
    def test_valid_update_member(self):
        response = self.client.put(
            reverse("detail_member", kwargs={"pk": self.member.pk}),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # PATCH REQUEST test for partially updating a member
    def test_valid_partial_update_member(self):
        self.object = Member.objects.get(pk=self.member.pk)
        response = self.client.patch(
            reverse("detail_member", kwargs={"pk": self.member.pk}),
            data=json.dumps(self.valid_partial_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_member(self):
        # Test updating a member with an invalid payload
        response = self.client.put(
            reverse("detail_member", kwargs={"pk": self.member.pk}),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # DELETE REQUEST tests for deleting a member
    def test_valid_delete_member(self):
        response = self.client.delete(reverse("detail_member", kwargs={"pk": self.member.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_member(self):
        # Test deleting an invalid member
        response = self.client.delete(reverse("detail_member", kwargs={"pk": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
