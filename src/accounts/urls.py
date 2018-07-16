from django.urls import re_path
from .views import UserProfile, PasswordChange

urlpatterns = [
    re_path(r"(?P<slug>[-\w]+)/change-password/$", PasswordChange.as_view(),
        name="password-change"),
    re_path(r"(?P<slug>[-\w]+)/$", UserProfile.as_view(), name="profile"),
] 