from django.contrib import admin
from .models import Blogger, Blog, Comment


class BlogInline(admin.TabularInline):
    model = Blog


class CommetInline(admin.TabularInline):
    model = Comment


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date")
    list_filter = ("name", "create_date")
    inlines = [BlogInline]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "create_date", "blogger")
    list_filter = ("title", "create_date", "blogger")
    inlines = [CommetInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "blog", "create_date", "text")
    list_filter = ("user", "blog", "create_date")

# Register your models here.
