from django.urls import path
from .views import TeamAPIView, TeamDetailAPIView
from .views import PersonAPIView, PersonDetailAPIView

urlpatterns = [
    path("team/", TeamAPIView.as_view(), name="list_create_team"),
    path("team/<int:pk>", TeamDetailAPIView.as_view(), name="detail_update_destroy_team"),
    path("members/", PersonAPIView.as_view(), name="list_create_person"),
    path("members/<int:pk>", PersonDetailAPIView.as_view(), name="detail_update_destroy_person"),
]
