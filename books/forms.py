from django.forms import ModelForm
from django.forms.util import ErrorList

from isbndb import IsbnDB
from models import *

db = IsbnDB()

class BookObjectForm(ModelForm):
    class Media:
        js = ('form_functions.js',)


class GenreForm(BookObjectForm):
    class Meta:
        model = Genre
        exclude = ['created_by',]
        get_autofill = []


class AuthorForm(BookObjectForm):
    class Meta:
        model = Author
        exclude = ['created_by',]
        get_autofill = []


class SeriesForm(BookObjectForm):
    class Meta:
        model = Series
        exclude = ['created_by',]
        get_autofill = []


class BookForm(BookObjectForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get("title")
        isbn = cleaned_data.get("ISBN")

        if title and isbn:
            if not db.validate_isbn(isbn, title):
                error_message = "That isbn doesn't correspond \
                        with the title of the book, or is invalid."
                self._errors['ISBN'] = ErrorList([error_message])
                del cleaned_data['ISBN']
        # Always return the full collection of cleaned data.
        return cleaned_data

    class Meta:
        model = Book
        exclude = ['created_by', 'positive_ratings', 'negative_ratings', 'rated_by', 'cover_image_authenticated']
        get_autofill = []


class ReviewForm(BookObjectForm):
    class Meta:
        model = Review
        exclude = ['created_by',]
        get_autofill = [('for_book', int),]
