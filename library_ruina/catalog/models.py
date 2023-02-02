from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date

class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter a book genre (e.g. Science Fiction")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Enter a language")

    def __str__(self):
        return self.name


class Autor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True,
                                     blank=True)
    date_of_death = models.DateField("death",
                                     null=True,
                                     blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Autor,
                               on_delete=models.SET_NULL,
                               null=True)
    genre = models.ManyToManyField(Genre,
                                   help_text="Select a genre")
    isbn = models.CharField("ISBN",
                            max_length=13,
                            help_text="ISBN number")
    summary = models.TextField(max_length=2000,
                               help_text="Enter a brief description of the book")
    language = models.ForeignKey(Language,
                                 on_delete=models.SET_NULL,
                                 null=True)
    class Meta:
        ordering = ["isbn"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ", ".join([genre.name for genre in self.genre.all()[:3]])
    display_genre.short_description = "Genre"




class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4(),
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey(Book,
                             on_delete=models.SET_NULL,
                             null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,
                                blank=True)
    borrower = models.ForeignKey(User,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)

    LOAD_STATUS = (
        ("m", "Maitenance"),
        ("o", "On load"),
        ("a", "Available"),
        ("r", "Reserved")
    )

    status = models.CharField(max_length=1,
                              choices=LOAD_STATUS,
                              default='m',
                              blank=True,
                              help_text="Book availability")

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return "%s: (%s)" % (self.id, self.book.title)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False





