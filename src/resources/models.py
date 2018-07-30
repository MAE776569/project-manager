from django.db import models

class Link(models.Model):
    title = models.CharField(blank=False, max_length=100)
    subtitle = models.CharField(blank=False, max_length=250)
    url = models.URLField(blank=False)

    class Meta:
        db_table = 'link'
        verbose_name = 'link'
        verbose_name_plural = 'links'

class Document(models.Model):
    title = models.CharField(blank=False, max_length=100)
    subtitle = models.CharField(blank=False, max_length=250)
    document = models.FileField(blank=False, upload_to='documents')

    class Meta:
        db_table = 'document'
        verbose_name = 'document'
        verbose_name_plural = 'documents'