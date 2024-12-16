# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_view, name='base_view'),
    path('success/', views.pembayaran_sukses_view, name='pembayaran_sukses'),  # Halaman sukses pembayaran
    path('pendaftaran/', views.pendaftaran_view, name='pendaftaran'),
    path('target/', views.target_view, name='target_view'),

]