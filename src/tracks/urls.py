from django.urls import re_path
from .views import TracksList, CreateTrack, EditTrack, DeleteTrack, TopicsList

urlpatterns = [
    re_path(r"create-track/$", CreateTrack.as_view(), name='create-track'),
    re_path(r"(?P<slug>[-\w]+)/edit/$", EditTrack.as_view(), name="edit-track"),
    re_path(r"(?P<slug>[-\w]+)/delete/$", DeleteTrack.as_view(), name="delete-track"),
    re_path(r"(?P<slug>[-\w]+)/topics/$", TopicsList.as_view(),
        name="topics"),
    re_path(r"$", TracksList.as_view(), name="tracks-list")
]