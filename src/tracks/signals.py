from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Topic

@receiver(post_save, sender=Topic)
def add_topic(sender, instance, **kwargs):
    instance.track.number_of_topics += 1
    instance.track.save()

@receiver(post_delete, sender=Topic)
def remove_topic(sender, instance, **kwargs):
    instance.track.number_of_topics -= 1
    instance.track.save()