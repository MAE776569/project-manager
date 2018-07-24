from django.urls import re_path
from .views import (TracksList, CreateTrack, EditTrack, DeleteTrack, TopicsList,
AddTopic, EditTopic, DeleteTopic, TopicDetails)
from .api_views import UserCompletedTopic

urlpatterns = [
    re_path(r"create-track/$", CreateTrack.as_view(), name='create-track'),
    re_path(r"(?P<slug>[-\w]+)/edit/$", EditTrack.as_view(), name="edit-track"),
    re_path(r"(?P<slug>[-\w]+)/delete/$", DeleteTrack.as_view(), name="delete-track"),
    re_path(r"(?P<slug>[-\w]+)/topics/$", TopicsList.as_view(),
        name="topics"),
    re_path(r"(?P<slug>[-\w]+)/add-topic/$", AddTopic.as_view(),
        name="add-topic"),
    #this to is topics
    re_path(r"topics/(?P<slug>[-\w]+)/edit-topic/$", EditTopic.as_view(),
        name='edit-topic'),
    re_path(r"topics/(?P<slug>[-\w]+)/delete-topic/$", DeleteTopic.as_view(),
        name='delete-topic'),
    #API views
    re_path(r"topics/(?P<slug>[-\w]+)/completed/$", UserCompletedTopic.as_view()),
    #end APi views
    re_path(r"topics/(?P<slug>[-\w]+)/$", TopicDetails.as_view(),
        name='topic-details'),
    #end this
    re_path(r"$", TracksList.as_view(), name="tracks-list")
]