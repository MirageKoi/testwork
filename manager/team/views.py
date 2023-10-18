from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import TeamModel, Person
from .serializers import TeamSerializer, PersonSerializer


class TeamAPIView(ListCreateAPIView):
    queryset = TeamModel.objects.all()
    serializer_class = TeamSerializer


class TeamDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TeamModel.objects.all()
    serializer_class = TeamSerializer


class PersonAPIView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
