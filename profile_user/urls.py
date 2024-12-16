from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='profile'),
    path('user_profile', views.edit_profile, name='user_profile'),

    
]
