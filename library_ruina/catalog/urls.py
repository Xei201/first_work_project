from . import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    re_path(r"^books$", views.BookListView.as_view(), name="books"),
    re_path(r"^authors$", views.AutorListView.as_view(), name="authors"),
    re_path(r"^book/(?P<pk>\d+)$", views.BookDetailView.as_view(), name="book-detail"),
    re_path(r"^authors/(?P<pk>\d+)$", views.AutorDetailView.as_view(), name="author-detail"),
]