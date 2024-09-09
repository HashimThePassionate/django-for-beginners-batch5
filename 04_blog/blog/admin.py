from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'body')
    ordering = ('id',)


admin.site.register(Blog, BlogAdmin)
# Register your models here.
