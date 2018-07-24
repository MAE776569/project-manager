from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from re import findall

class Track(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(blank=False)
    number_of_topics = models.PositiveSmallIntegerField(blank=True, default=0)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'track'
        verbose_name = 'track'
        verbose_name_plural = 'tracks'

class Topic(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(blank=False)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    slug = models.SlugField(blank=True, unique=True)
    video_url = models.URLField(blank=True)
    note = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_video_id(self):
        youtube_regex = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
        if self.video_url:
            matches = findall(youtube_regex, self.video_url)
            id = matches[0][-1]
            if len(id) == 11:
                return id
        return None
    
    class Meta:
        db_table = 'topic'
        verbose_name = 'topic'
        verbose_name_plural = 'topics'

class CompletedTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "{} completed {}".format(self.user.name, self.topic.title)

    class Meta:
        db_table = 'completed_topic'
        verbose_name = 'completed topic'
        verbose_name_plural = 'completed topics'