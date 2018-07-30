"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path, path
from decouple import config
from authentication import urls as auth_urls
from accounts import urls as accounts_urls
from tracks import urls as tracks_urls
from authentication.views import IndexView
from django.conf import settings
from django.conf.urls.static import static
from api import urls as api_urls
from resources import urls as resources_urls

urlpatterns = [
    re_path(r"^$", IndexView.as_view(), name="index"),
    re_path(r"^auth/", include((auth_urls, 'authentication'), namespace="auth")),
    re_path(r"^accounts/", include((accounts_urls, 'accounts'), namespace="accounts")),
    re_path(r"^tracks/", include((tracks_urls, 'tracks'), namespace="tracks")),
    re_path(r"^api/", include((api_urls, 'api'), namespace="api")),
    re_path(r"^resources/", include((resources_urls, 'resources'), namespace="resources"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls)
    ]
