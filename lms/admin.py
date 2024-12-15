# admin.py
from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'level', 'price', 'created_at')
    search_fields = ('title', 'instructor')
