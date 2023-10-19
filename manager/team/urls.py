from django.urls import path
from .views import TeamAPIView, TeamDetailAPIView
from .views import MemberAPIView, MemberDetailAPIView

urlpatterns = [
    path("teams/", TeamAPIView.as_view(), name="list_team"),
    path("teams/<int:pk>", TeamDetailAPIView.as_view(), name="detail_team"),
    path("members/", MemberAPIView.as_view(), name="list_member"),
    path("members/<int:pk>", MemberDetailAPIView.as_view(), name="detail_member"),
]
