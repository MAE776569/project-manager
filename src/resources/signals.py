from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Link, Document
from notifications.models import Notification
from django.urls import reverse

@receiver(post_save, sender=Link)
def link_created(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(title="New link was Added",
            subtitle=instance.title,
            admin_only=False, users_only=True,
            callback_url=reverse("resources:resources-list"))

@receiver(post_save, sender=Document)
def document_created(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(title="New document was Added",
            subtitle=instance.title,
            admin_only=False, users_only=True,
            callback_url=reverse("resources:resources-list"))