from django.shortcuts import render
from .models import Blogger, Blog, Comment
from django.contrib.auth.decorators import login_required, permission_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

import logging

from integration.exception import BaseExceptions, base_exception

logger = logging.getLogger(__name__)


@base_exception
@login_required()
def index_blog(request):
    """Представление, выводящая статистику блога"""

    num_blogs = Blog.objects.all().count()
    num_bloggers = Blogger.objects.all().count()
    return render(request, 'index_blog.html', context={
        "num_blogs": num_blogs,
        "num_bloggers": num_bloggers,
    })


class BloggerListViews(LoginRequiredMixin, BaseExceptions, generic.ListView):
    """Список блогеров в блоге"""

    model = Blogger
    template_name = "blog/blogger_list.html"
    context_object_name = "bloggers_list"
    paginate_by = 5


class BlogListViews(LoginRequiredMixin, BaseExceptions, generic.ListView):
    """Список всех блогов"""

    model = Blog
    template_name = "blog/blog_list.html"
    paginate_by = 5
    context_object_name = "blog_list"


class BlogDetailView(LoginRequiredMixin, BaseExceptions, generic.DetailView):
    """Представление заметки в блоге"""

    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"


class BloggerDetailView(LoginRequiredMixin, BaseExceptions, generic.DetailView):
    """Представление блогера"""

    model = Blogger
    template_name = "blog/blogger_detail.html"
    context_object_name = "blogger"


class CommentCreateView(LoginRequiredMixin, BaseExceptions, CreateView):
    """Представление создания комментария"""

    model = Comment
    fields = ["text"]
    template_name = "blog/create_comment.html"

    def get_success_url(self):
        return reverse_lazy("blog-detail", args=self.kwargs.get('pk'))

    def form_valid(self, form):
        user = self.request.user
        blog = Blog.objects.get(id=self.kwargs.get('pk'))
        form.instance.user = user
        form.instance.blog = blog
        return super(CommentCreateView, self).form_valid(form)


class CommentDeleteView(PermissionRequiredMixin, BaseExceptions, DeleteView):
    """Представление удаления комментария"""

    permission_required = ("catalog.can_delete_comment",)
    model = Comment
    template_name = "blog/comment_delete.html"
    context_object_name = "comment"

    def get_success_url(self):
        comment = Comment.objects.get(id=self.kwargs.get('pk'))
        pk = comment.blog.pk
        return reverse_lazy("blog-detail", kwargs={"pk": pk})


class BlogCreateView(LoginRequiredMixin, BaseExceptions, CreateView):
    """Создание заметки в блоге"""

    model = Blog
    template_name = "blog/blog_form.html"
    fields = ["title", "context", "blogger"]


class BlogUpdateView(LoginRequiredMixin, BaseExceptions, UpdateView):
    """Обновление заметки в блоге"""

    model = Blog
    template_name = "blog/blog_form.html"
    fields = ["title", "context"]


class BlogDeleteView(LoginRequiredMixin, BaseExceptions, DeleteView):
    """Удаление заметки из блога"""

    model = Blog
    template_name = "blog/blog_delete.html"
    context_object_name = 'blog'
    success_url = reverse_lazy("blogs")

