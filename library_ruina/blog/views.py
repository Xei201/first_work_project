from django.shortcuts import render, get_object_or_404
from .models import Blogger, Blog, Comment
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy


def index_blog(request):
    num_blogs = Blog.objects.all().count()
    num_bloggers = Blogger.objects.all().count()
    return render(request, 'index_blog.html', context={
        "num_blogs": num_blogs,
        "num_bloggers": num_bloggers,
    })


class BloggerListViews(generic.ListView):
    model = Blogger
    template_name = "blog/blogger_list.html"
    context_object_name = "bloggers_list"
    paginate_by = 5


class BlogListViews(generic.ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    paginate_by = 5
    context_object_name = "blog_list"


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"


class BloggerDetailView(generic.DetailView):
    model = Blogger
    template_name = "blog/blogger_detail.html"
    context_object_name = "blogger"


class CommentCreateView(CreateView):
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


class CommentDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("catalog.can_delete_comment",)
    model = Comment
    template_name = "blog/comment_delete.html"
    context_object_name = "comment"

    def get_success_url(self):
        comment = Comment.objects.get(id=self.kwargs.get('pk'))
        pk = comment.blog.pk
        return reverse_lazy("blog-detail", kwargs={"pk": pk})


class BlogCreateView(CreateView):
    model = Blog
    template_name = "blog/blog_form.html"
    fields = ["title", "context", "blogger"]


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blog/blog_form.html"
    fields = ["title", "context"]


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/blog_delete.html"
    context_object_name = 'blog'
    success_url = reverse_lazy("blogs")

