from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path("", views.user_login, name="user_login"),
    path('logout/', views.user_logout, name='user_logout'),
    path('special/', views.special, name='special'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
