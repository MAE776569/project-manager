from django.db import models
from os.path import splitext
from os import urandom

class Link(models.Model):
    title = models.CharField(blank=False, max_length=100)
    subtitle = models.CharField(blank=False, max_length=250)
    url = models.URLField(blank=False)

    class Meta:
        db_table = 'link'
        verbose_name = 'link'
        verbose_name_plural = 'links'

def document_directory_path(instance, filename):
    document_name, document_ext = splitext(filename)
    document_name += urandom(5).hex()
    return 'documents/{0}{1}'.format(document_name, document_ext)

class Document(models.Model):
    title = models.CharField(blank=False, max_length=100)
    subtitle = models.CharField(blank=False, max_length=250)
    document = models.FileField(blank=False, upload_to=document_directory_path)

    class Meta:
        db_table = 'document'
        verbose_name = 'document'
        verbose_name_plural = 'documents'