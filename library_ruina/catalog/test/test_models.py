from django.test import TestCase
from catalog.models import Autor, Genre, Language, Book, BookInstance

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Autor.objects.create(first_name="Big", last_name="Bob")

    def test_first_name_label(self):
        author = Autor.objects.get(id=1)
        field_label = author._meta.get_field("first_name").verbose_name
        self.assertEquals(field_label, "first name")

    def test_date_of_death_label(self):
        author = Autor.objects.get(id=1)
        field_label = author._meta.get_field("date_of_death").verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        author = Autor.objects.get(id=1)
        max_length = author._meta.get_field("first_name").max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Autor.objects.get(id=1)
        expected_object_name = "%s %s" % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Autor.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), "/catalog/authors/1")

    def test_last_name_label(self):
        author = Autor.objects.get(id=1)
        field_name = author._meta.get_field("last_name").verbose_name
        self.assertEquals(field_name, "last name")

    def test_last_name_max_length(self):
        author = Autor.objects.get(id=1)
        max_length = author._meta.get_field("last_name").max_length
        self.assertEquals(max_length, 200)

    def test_date_of_birth_label(self):
        author = Autor.objects.get(id=1)
        field_name = author._meta.get_field("date_of_birth").verbose_name
        self.assertEquals(field_name, "date of birth")


class GenreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name="classic")

    def test_name_label(self):
        genre = Genre.objects.get(id=1)
        name = genre._meta.get_field('name').verbose_name
        self.assertEqual(name, "name")

    def test_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_str_genre(self):
        genre = Genre.objects.get(id=1)
        object_name = genre.name
        self.assertEqual(object_name, str(genre))


class LanguageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Language.objects.create(name='RU')

    def test_name_label(self):
        language = Language.objects.get(id=1)
        name = language._meta.get_field("name").verbose_name
        self.assertEqual(name, "name")

    def test_name_max_length(self):
        language = Language.objects.get(id=1)
        max_length = language._meta.get_field("name").max_length
        self.assertEqual(max_length, 100)

    def test_object_name_language(self):
        language = Language.objects.get(id=1)
        object_name = language.name
        self.assertEqual(object_name, str(language))



class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        genre = Genre.objects.create(name="classic")
        book = Book.objects.create(title='War', isbn="12345678912", summary='test')
        book.genre.add(genre)

    def test_label_name(self):
        book = Book.objects.get(title='War')
        title = book._meta.get_field("title").verbose_name
        isbn = book._meta.get_field("isbn").verbose_name
        summary = book._meta.get_field("summary").verbose_name
        self.assertEqual(title, "title")
        self.assertEqual(isbn, "ISBN")
        self.assertEqual(summary, 'summary')

    def test_fields_max_length(self):
        book = Book.objects.get(title='War')
        title_max_length = book._meta.get_field("title").max_length
        isbn_max_length = book._meta.get_field("isbn").max_length
        summary_max_length = book._meta.get_field("summary").max_length
        self.assertEqual(title_max_length, 200)
        self.assertEqual(isbn_max_length, 13)
        self.assertEqual(summary_max_length, 2000)

    def test_object_name_book(self):
        book = Book.objects.get(title='War')
        title = book.title
        self.assertEqual(title, str(book))

    def test_get_absolute_url_book(self):
        book = Book.objects.get(title='War')
        self.assertEqual(book.get_absolute_url(), "/catalog/book/1")

    def test_display_genre_book(self):
        book = Book.objects.get(title='War')
        self.assertEqual(book.display_genre(), "classic")


