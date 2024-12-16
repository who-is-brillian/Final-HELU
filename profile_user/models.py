
# models.py
from django.db import models
# models.py
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    # Menambahkan related_name untuk menghindari konflik dengan model User dari auth
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)

    def __str__(self):
        return self.username
    
# class Userprofile(models.model):
#     userid =
#     phone = models.CharField(max_length=15, null=True, blank=True)
#     address = models.TextField(null=True, blank=True)
