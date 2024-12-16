from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.topic_list, name='topic_list'),
    path('<int:pk>/', views.topic_detail, name='topic_detail'),
    path('new/', views.new_topic, name='new_topic'),
    path('<int:pk>/new_post/', views.new_post, name='new_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('delete_reply/<int:pk>/', views.delete_reply, name='delete_reply'),
    path('topic/delete/<int:pk>/', views.delete_topic, name='delete_topic'),
    path('topic/<int:pk>/like/', views.like_topic, name='like_topic'),
    path('topic/<int:pk>/unlike/', views.unlike_topic, name='unlike_topic'),
    path('topic/edit/<int:pk>/', views.edit_topic, name='edit_topic'),
    path('find/', views.find_topic, name='find_topic'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)