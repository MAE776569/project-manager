from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from authentication.models import AccountVerification
from notifications.models import Notification
from django.urls import reverse

@receiver(post_save, sender=get_user_model())
def account_verification_registered(sender, instance, created, **kwargs):
    if created and not instance.is_admin:
        account = AccountVerification.objects.get(email=instance.email)
        account.is_registered = True
        account.save()
        Notification.objects.create(title="New user was registered",
            subtitle=instance.name, admin_only=True, users_only=False,
            callback_url=reverse("accounts:users-list"))