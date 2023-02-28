from . import views
from django.urls import re_path, path, include

books_patterns = [
    path("", views.BookListView.as_view(), name="books"),
    re_path(r"^create/$", views.BookCreateView.as_view(), name="book-create"),
    re_path(r"^(?P<pk>\d+)/update/$", views.BookUpdate.as_view(), name="book-update"),
    re_path(r"^(?P<pk>\d+)/delete/$", views.BookDelete.as_view(), name="book-delete"),
]

author_patterns = [
    re_path(r"^create/$", views.AutorCreateView.as_view(), name="author-create"),
    re_path(r"^(?P<pk>\d+)/update/$", views.AutorUpdate.as_view(), name="author-update"),
    re_path(r"^(?P<pk>\d+)/delete/$", views.AutorDelete.as_view(), name="author-delete"),
]

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    re_path(r"^authors$", views.AutorListView.as_view(), name="authors"),
    re_path(r"^mybooks/$", views.LoanedBooksByUserListView.as_view(), name="my-borrowed"),
    re_path(r"^book/(?P<pk>\d+)$", views.BookDetailView.as_view(), name="book-detail"),
    re_path(r"^authors/(?P<pk>\d+)$", views.AutorDetailView.as_view(), name="author-detail"),
    re_path(r"^allborrowed/$", views.AllBorrowedListView.as_view(), name="all-borrowed"),
    re_path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name="renew-book-librarian"),
    path("author/", include(author_patterns)),
    path("books/", include(books_patterns)),
]