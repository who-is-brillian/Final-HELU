from django.contrib import admin
from .models import LMSPermission, Course, Material


class MaterialInline(admin.TabularInline):
    model = Material
    extra = 1  # Menambahkan satu form kosong untuk input material baru

# Menggunakan dekorator untuk mendaftarkan Course
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'level', 'price', 'created_at')
    search_fields = ('title', 'instructor')
    inlines = [MaterialInline]  # Menambahkan inline untuk Material

# Mendaftarkan LMSPermission
@admin.register(LMSPermission)
class LMSPermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_allowed')
    list_filter = ('is_allowed',)
    search_fields = ('user__username',)
    filter_horizontal = ('courses',)

# Mendaftarkan Material
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'file')  # Tampilkan kolom course, title dan file
    search_fields = ('course__title', 'title')  # Pencarian berdasarkan judul kursus dan material
