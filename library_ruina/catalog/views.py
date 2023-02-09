from django.shortcuts import render, get_object_or_404
from .models import Book, Autor, Genre, Language, BookInstance
from .forms import RenewBookForm
from django.contrib.auth.decorators import login_required, permission_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
import datetime


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
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

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
    paginate_by = 4


class AutorDetailView(generic.DetailView):
    model = Autor
    context_object_name = "author"


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    context_object_name = "bookinstance_list"
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


@permission_required("catalog.can_mark_returned")
def renew_book_librarian(request, pk):
    book_inst = get_object_or_404(BookInstance, pk=pk)

    if request.method == "POST":
        form = RenewBookForm(request.POST)

        if form.is_valid():
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()

            return HttpResponseRedirect(reverse("all-borrowed"))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={"renewal_date": proposed_renewal_date,})

    return render(request, "catalog/book_renew_librarian.html", {"form": form,
                                                                 "bookinst": book_inst})


class AutorCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("catalog.can_mark_returned",)
    model = Autor
    fields = "__all__"
    initial = {"date_of_death": "12/10/2022",}
    template_name = "catalog/author_form.html"


class AutorUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ("catalog.can_mark_returned",)
    model = Autor
    fields = ["first_name", "last_name", "date_of_birth", "date_of_death"]
    template_name = "catalog/author_form.html"


class AutorDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ("catalog.can_mark_returned",)
    model = Autor
    success_url = reverse_lazy('authors')
    template_name = "catalog/author_confirm_delete.html"


class BookCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("catalog.can_mark_returned",)
    model = Book
    fields = "__all__"
    template_name = "catalog/book_form.html"


class BookUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ("catalog.can_mark_returned",)
    model = Book
    fields = "__all__"
    template_name = "catalog/book_form.html"


class BookDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ("catalog.can_mark_returned",)
    model = Book
    success_url = reverse_lazy('books')
    template_name = "catalog/book_confirm_delete.html"


def test(request):
    genre = Genre.objects.create(name="Army")
    book = Book.objects.create(title='War', genre=genre, isbn="12385678912", summary='test2')
    book.genre.add(genre)
    return HttpResponse("<h1>TEST</h1>")