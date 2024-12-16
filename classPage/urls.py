from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'classPage' 
urlpatterns = [
    path('', views.class_page, name='class_page'),
    path('<slug:url_slug>/', views.class_detail, name='class_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
