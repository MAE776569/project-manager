from django.urls import re_path, path
from .views import UserProfile, PasswordChange, ProfilePictureUpload
from administrator.views import (AccountVerificationsList,
    AddAccountVerification, VerificationLink, UsersList)

urlpatterns = [
    re_path(r"account-verifications/$", AccountVerificationsList.as_view(),
        name="account-verifications"),
    re_path(r"add-account-verification/$", AddAccountVerification.as_view(),
        name="add-account-verification"),
    re_path(r"users-list/$", UsersList.as_view(), name='users-list'),
    path(r"verify-link/<slug>/", VerificationLink.as_view(),
        name="verification-link"),
    re_path(r"(?P<slug>[-\w]+)/change-password/$", PasswordChange.as_view(),
        name="password-change"),
    re_path(r"(?P<slug>[-\w]+)/profile-picture-upload/$",
        ProfilePictureUpload.as_view(),
        name="profile-picture-upload"),
    re_path(r"(?P<slug>[-\w]+)/$", UserProfile.as_view(), name="profile")
]