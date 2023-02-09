from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^$", views.index_blog, name="index_blog"),
    re_path(r"^blogs$", views.BlogListViews.as_view(), name="blogs"),
    re_path(r"^bloggers$", views.BloggerListViews.as_view(), name="bloggers"),
    re_path(r"^blogger/(?P<pk>\d+)$", views.BloggerDetailView.as_view(), name="blogger-detail"),
    re_path(r"^blog/(?P<pk>\d+)$", views.BlogDetailView.as_view(), name="blog-detail"),
    re_path(r"^comment/create/(?P<pk>\d+)$", views.CommentCreateView.as_view(), name="create-comment"),
    re_path(r"^comment/delete/(?P<pk>\d+)$", views.CommentDeleteView.as_view(), name="delete-comment"),
    re_path(r"^blog/create$", views.BlogCreateView.as_view(), name="blog-create"),
    re_path(r"^blog/update/(?P<pk>\d+)$", views.BlogUpdateView.as_view(), name="blog-update"),
    re_path(r"^blog/delete/(?P<pk>\d+)$", views.BlogDeleteView.as_view(), name="blog-delete"),
]

