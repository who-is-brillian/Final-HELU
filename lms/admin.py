# admin.py
from django.contrib import admin
from .models import Course, LMSPermission

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'level', 'price', 'created_at')
    search_fields = ('title', 'instructor')

@admin.register(LMSPermission)
class LMSPermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_allowed')  # Tampilkan kolom ini di daftar admin
    list_filter = ('is_allowed',)         # Tambahkan filter berdasarkan izin
    search_fields = ('user__username',)   # Tambahkan pencarian berdasarkan username