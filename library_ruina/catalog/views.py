from django.shortcuts import render
from .models import Book, Autor, Genre, Language, BookInstance
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


#@login_required()
def index(request):
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    num_authors = Autor.objects.all().count()
    num_genre = Genre.objects.all().count()
    num_language = Language.objects.all().count()
    classic_books = Book.objects.filter(genre__name="Classic").count()
    classic_book = Book.objects.filter(genre__name="Classic")
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visit'] = num_visits + 1

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


class BookListView(LoginRequiredMixin, generic.ListView):
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"
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


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class AllBorrowedListView(PermissionRequiredMixin, generic.ListView):
    permission_required = ('catalog.can_mark_returned', 'catalog.can_edit')
    model = BookInstance
    context_object_name = "allborrowed"
    template_name = "catalog/list_borrowed_user.html"
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact="o").order_by("due_back")
