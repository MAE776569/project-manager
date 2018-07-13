from django.contrib.auth import get_user_model

class UserAuthenticationBackend():

    def authenticate(self, request, email, password):
        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                return user
            return None
        except user.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = get_user_model().objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except user.DoesNotExist:
            return None