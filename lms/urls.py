from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    # URL untuk halaman utama course dengan proteksi akses
    path('page/', views.course_page, name='course_page'),  # Proteksi dengan izin
    
    # URL untuk daftar semua kursus
    path('', views.course_list, name='course_list'),
    
    # URL untuk detail kursus berdasarkan ID
    path('<int:course_id>/', views.course_detail, name='course_detail'),

    # URL untuk halaman writing dengan testimonial
    path('writing/', views.writing, name='writing'),
    
]
