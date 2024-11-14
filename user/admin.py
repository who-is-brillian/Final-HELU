from django.contrib import admin
from .models import UserProfileInfo

class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'password')

admin.site.register(UserProfileInfo, UserProfileInfoAdmin)
