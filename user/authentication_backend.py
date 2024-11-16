from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)  # Menggunakan email sebagai username
            if user.check_password(password):  # Memeriksa password yang benar
                return user
            return None
        except User.DoesNotExist:
            return None
