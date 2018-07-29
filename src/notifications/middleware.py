from .models import NotificationManager

class NotificationMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        if request.user.is_authenticated:
            query = '''select case when notification_manager.notification_id
            is null then false else true end seen,
            notification.* from notification_manager
            right outer join notification
            on notification_manager.notification_id=notification.id
            and notification_manager.user_id={0}
            where notification.admin_only={1}
            and notification.users_only={2}'''
            if request.user.is_admin:
                query = query.format(request.user.id, True, False)
            else:
                query = query.format(request.user.id, False, True)
            request.notifications = list(NotificationManager.objects.raw(query))
