from django.forms import ModelForm

from models import *

class BookObjectForm(ModelForm):
    class Media:
        js = ('form_functions.js',)

class GenreForm(BookObjectForm):
    class Meta:
        model = Genre
        exclude = ['created_by',]

class AuthorForm(BookObjectForm):
    class Meta:
        model = Author
        exclude = ['created_by',]

class SeriesForm(BookObjectForm):
    class Meta:
        model = Series
        exclude = ['created_by',]

class BookForm(BookObjectForm):
    class Meta:
        model = Book
        exclude = ['created_by', 'positive_ratings', 'negative_ratings', 'rated_by']

class ReviewForm(BookObjectForm):
    class Meta:
        model = Review
        exclude = ['created_by',]
