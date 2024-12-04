from django.urls import path
from .import views

urlpatterns = [
    path('', views.topic_list, name='topic_list'),
    path('<int:pk>/', views.topic_detail, name='topic_detail'),
    path('new/', views.new_topic, name='new_topic'),
    path('<int:pk>/new_post/', views.new_post, name='new_post'),
]
