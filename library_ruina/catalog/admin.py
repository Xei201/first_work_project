from django.contrib import admin
from .models import Autor, Language, Genre, Book, BookInstance

admin.site.register(Language)
admin.site.register(Genre)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


class BooksInline(admin.TabularInline):
    model = Book

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_of_birth", "date_of_death")
    fields = ("first_name", "last_name", ("date_of_birth", "date_of_death"))
    inlines = [BooksInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", 'author', "display_genre", "language")
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "status", "due_back")
    list_filter = ("status", "due_back")
    fieldsets = (
        (None, {
            "fields": ("book", "imprint", 'id')
        }),
        ("Availability", {
            "fields": ("status", "due_back")
        }),
    )