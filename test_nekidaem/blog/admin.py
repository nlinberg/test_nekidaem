from django.contrib import admin
from .models import Blog, Post


class BlogAdmin(admin.ModelAdmin):
    actions = None


class PostAdmin(admin.ModelAdmin):
    actions = None


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
