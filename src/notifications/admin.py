from django.contrib import admin
from .models import Notification, NotificationManager

admin.site.register(Notification)
admin.site.register(NotificationManager)