from django.urls import re_path
from .views import (ResourcesList, AddLink, UpdateLink, DeleteLink,
AddDocument, UpdateDocument, DeleteDocument)
from django_downloadview import ObjectDownloadView
from .models import Document

urlpatterns = [
    re_path(r"add-link/$", AddLink.as_view(), name='add-link'),
    re_path(r"add-document/$", AddDocument.as_view(), name='add-document'),
    re_path(r"links/(?P<pk>[1-9]+)/edit-link/$", UpdateLink.as_view(),
        name="edit-link"),
    re_path(r"links/(?P<pk>[1-9]+)/delete-link/$", DeleteLink.as_view(),
        name="delete-link"),
    re_path(r"documents/(?P<pk>[1-9]+)/edit-document/$", UpdateDocument.as_view(),
        name="edit-document"),
    re_path(r"documents/(?P<pk>[1-9]+)/delete-document/$", DeleteDocument.as_view(),
        name="delete-document"),
    re_path(r"documents/(?P<pk>[1-9]+)/download-document/$",
        ObjectDownloadView.as_view(model=Document, file_field='document'),
        name="download-document"),
    re_path(r"$", ResourcesList.as_view(), name='resources-list')
]