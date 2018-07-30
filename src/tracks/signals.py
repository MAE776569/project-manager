from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Topic, Track
from notifications.models import Notification
from django.urls import reverse, reverse_lazy

@receiver(post_save, sender=Topic)
def topic_created(sender, instance, created, **kwargs):
    if created:
        instance.track.number_of_topics += 1
        instance.track.save()
        Notification.objects.create(title="New topic was Added",
            subtitle=instance.title + " - " + instance.track.title,
            admin_only=False, users_only=True,
            callback_url=reverse_lazy("tracks:topics", kwargs={
                'slug': instance.track.slug
            }))

@receiver(post_save, sender=Track)
def track_created(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(title="New track was Added",
            subtitle=instance.title, admin_only=False, users_only=True,
            callback_url=reverse("tracks:tracks-list"))

@receiver(post_delete, sender=Topic)
def topic_removed(sender, instance, **kwargs):
    instance.track.number_of_topics -= 1
    instance.track.save()