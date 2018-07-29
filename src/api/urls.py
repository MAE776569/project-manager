from django.urls import re_path
from .views import UserCompletedTopic, GetTopicVideoID, GetTopicNote

urlpatterns = [
    re_path(r"topics/(?P<slug>[-\w]+)/completed/$", UserCompletedTopic.as_view()),
    re_path(r"topics/(?P<slug>[-\w]+)/video-id/$", GetTopicVideoID.as_view()),
    re_path(r"topics/(?P<slug>[-\w]+)/note/$", GetTopicNote.as_view())
]