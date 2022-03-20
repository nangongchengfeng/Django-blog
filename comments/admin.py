from django.contrib import admin


# Register your models here.

from django.contrib import admin
from django.contrib.admin import helpers
from django.contrib.admin.checks import ModelAdminChecks

from .models import Comment
admin.site.site_header = "Blog博客-Joker"
admin.site.index_title = "Blog博客-Joker"

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'post']
    search_fields = ['name','text',]
    list_filter = ['created_time',]
    ordering = ['created_time']


admin.site.register(Comment, CommentAdmin)