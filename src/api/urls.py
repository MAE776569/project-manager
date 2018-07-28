from django.urls import re_path
from .views import UserCompletedTopic

urlpatterns = [
    re_path(r"topics/(?P<slug>[-\w]+)/completed/$", UserCompletedTopic.as_view()),
]