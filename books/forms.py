from django.forms import ModelForm

from models import *

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
    class Meta:
        model = Book
        exclude = ['created_by', 'positive_ratings', 'negative_ratings', 'rated_by']
        get_autofill = []


class ReviewForm(BookObjectForm):
    class Meta:
        model = Review
        exclude = ['created_by',]
        get_autofill = [('for_book', int),]
