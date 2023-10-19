from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Team, Member
from .serializers import TeamSerializer, MemberSerializer


# Create an API view for listing and creating Team instances
class TeamAPIView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


# Create an API view for retrieving, updating, and deleting Team instances
class TeamDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


# Create an API view for listing and creating Member instances
class MemberAPIView(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


# Create an API view for retrieving, updating, and deleting Member instances
class MemberDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
