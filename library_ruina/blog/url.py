from django.urls import path, re_path, include
from . import views


blog_patterns = [
    re_path(r"^(?P<pk>\d+)$", views.BlogDetailView.as_view(), name="blog-detail"),
    re_path(r"^create$", views.BlogCreateView.as_view(), name="blog-create"),
    re_path(r"^update/(?P<pk>\d+)$", views.BlogUpdateView.as_view(), name="blog-update"),
    re_path(r"^delete/(?P<pk>\d+)$", views.BlogDeleteView.as_view(), name="blog-delete"),
]

comment_patterns = [
    re_path(r"^create/(?P<pk>\d+)$", views.CommentCreateView.as_view(), name="create-comment"),
    re_path(r"^delete/(?P<pk>\d+)$", views.CommentDeleteView.as_view(), name="delete-comment"),
]

urlpatterns = [
    re_path(r"^$", views.index_blog, name="index_blog"),
    re_path(r"^blogs$", views.BlogListViews.as_view(), name="blogs"),
    re_path(r"^bloggers$", views.BloggerListViews.as_view(), name="bloggers"),
    re_path(r"^blogger/(?P<pk>\d+)$", views.BloggerDetailView.as_view(), name="blogger-detail"),
    path("blog/", include(blog_patterns)),
    path("comment/", views.CommentCreateView.as_view(), name="create-comment"),
]

