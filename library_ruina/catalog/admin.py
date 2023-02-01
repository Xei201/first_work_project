from django.contrib import admin
from .models import Autor, Language, Genre, Book, BookInstance

admin.site.register(Autor)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookInstance)
