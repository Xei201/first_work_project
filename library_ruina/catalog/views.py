from django.shortcuts import render
from .models import Book, Autor, Genre, Language, BookInstance
from django.http import HttpResponse
from django.views import generic

def index(request):
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    num_authors = Autor.objects.all().count()
    num_genre = Genre.objects.all().count()
    num_language = Language.objects.all().count()
    classic_books = Book.objects.filter(genre__name="Classic").count()
    classic_book = Book.objects.filter(genre__name="Classic")
    num_visits = request.sessions.get('num_visits', 0)
    request.sessions['num_visit'] = num_visits + 1

    return render(request, 'index.html', context={
        "num_books": num_books,
        "num_instance": num_instance,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_genre": num_genre,
        "num_language": num_language,
        "classic_books": classic_books,
        "classic_book": classic_book,
        "num_visits": num_visits,
    })


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = "book"


class AutorListView(generic.ListView):
    model = Autor
    context_object_name = "list_author"
    paginate_by = 2


class AutorDetailView(generic.DetailView):
    model = Autor
    context_object_name = "author"

