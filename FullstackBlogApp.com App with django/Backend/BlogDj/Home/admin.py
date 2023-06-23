from django.contrib import admin
from .models import *

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_on', 'updated_on']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'added_on']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date']
