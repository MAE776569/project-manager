from .models import NotificationManager
from django.utils.deprecation import MiddlewareMixin

class NotificationMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.user.is_authenticated:
            notif_id = request.GET.get('notif_id', None)
            ref = request.GET.get('ref', None)

            if notif_id and ref == 'notif':
                NotificationManager.objects.get_or_create(notification_id=notif_id,
                    user=request.user)

            query = '''select case when notification_manager.notification_id
            is null then false else true end seen,
            notification.* from notification_manager
            right outer join notification
            on notification_manager.notification_id=notification.id
            and notification_manager.user_id={0}
            where notification.admin_only={1}
            and notification.users_only={2}
            order by notification.created_at desc
            limit 5;'''

            if request.user.is_admin:
                query = query.format(request.user.id, True, False)
            else:
                query = query.format(request.user.id, False, True)
            request.notifications = list(NotificationManager.objects.raw(query))
            count = 0
            for notif in request.notifications:
                count += int(not notif.seen)
            request.notifications_count = count
