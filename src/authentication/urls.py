from django.urls import path, re_path
from .views import Login, Registeration, home

urlpatterns = [
    re_path(r"login/$", Login.as_view(), name='login'),
    re_path(r"register/$", Registeration.as_view(), name="register"),
]