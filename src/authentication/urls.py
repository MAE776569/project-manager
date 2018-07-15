from django.urls import re_path
from .views import Login, Registration, VerifyAccount, Logout

urlpatterns = [
    re_path(r"login/$", Login.as_view(), name='login'),
    re_path(r"register/$", Registration.as_view(), name="register"),
    re_path(r"verify/$", VerifyAccount.as_view(), name='verify'),
    re_path(r"logout/$", Logout.as_view(), name="logout")
]