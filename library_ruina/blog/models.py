from django.db import models
import datetime
from django.urls import reverse
from django.contrib.auth.models import User


def actual_date():
    return datetime.datetime.now()


class Blogger(models.Model):
    """Модель данных блогера"""

    name = models.CharField(max_length=100, help_text="Enter a name blogger")
    description = models.TextField(max_length=2000, help_text="Enter a description of blogger")
    create_date = models.DateTimeField(default=actual_date, blank=True, null=True)

    class Meta:
        ordering = ["create_date"]
        permissions = (("can_add_blog", "Blogs moder"),)

    def get_absolute_url(self):
        return reverse("blogger-detail", args=[str(self.id)])

    def __str__(self):
        return self.name


class Blog(models.Model):
    """Модель поста в блоге"""

    title = models.CharField(max_length=100)
    context = models.TextField(max_length=2000)
    create_date = models.DateTimeField(default=actual_date, blank=True, null=True)
    blogger = models.ForeignKey(Blogger,
                                on_delete=models.SET_NULL,
                                null=True)

    class Meta:
        ordering = ["create_date"]

    def get_absolute_url(self):
        return reverse("blog-detail", args=[str(self.id)])

    def get_comment_url(self):
        return reverse("create-comment", args=[str(self.id)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Модель хранит комментарий к посту в блоге """

    text = models.TextField(max_length=1000)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField(default=actual_date, blank=True, null=True)

    class Meta:
        ordering = ["create_date"]
        permissions = (("can_delete_comment", "Comment moder"),)


    def __str__(self):
        return "%s, %s" % (self.user, self.create_date)


