from django.contrib import admin
from .models import Topic, Post

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('content', 'topic', 'parent', 'created_by', 'created_at')
    list_filter = ('topic', 'created_at')