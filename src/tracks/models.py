from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

class Track(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(blank=False)
    number_of_topics = models.PositiveSmallIntegerField(blank=True, default=0)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(blank=False)
    track = models.OneToOneField(Track, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    slug = models.SlugField(blank=True)

    #TODO: add video url

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class CompletedTopics(models.Model):
    topic = models.OneToOneField(Topic, on_delete=models.CASCADE)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "{} completed {}".format(self.user.name, self.topic.title)