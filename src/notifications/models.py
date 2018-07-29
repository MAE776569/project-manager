from django.db import models
from django.contrib.auth import get_user_model

class Notification(models.Model):
    title = models.CharField(blank=False, max_length=100)
    subtitle = models.CharField(blank=False, max_length=250)
    admin_only = models.BooleanField(blank=False)
    users_only = models.BooleanField(blank=False)
    callback_url = models.URLField(blank=False)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        db_table = 'notification'
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'

class NotificationManager(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)

    class Meta:
        db_table = 'notification_manager'
        verbose_name = 'notification manager'
        verbose_name_plural = 'notifications manager'