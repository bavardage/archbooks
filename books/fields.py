from django import forms

from isbndb import IsbnDB


class ISBNFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
#        self.book_title = kwargs.get('book_title_field', None)
#        del kwargs['book_title_field']
        super(ISBNFormField, self).__init__(*args, **kwargs)

    def clean(self, value):
        """
        A poor attempt at cleaning the ISBN
        """
        db = IsbnDB()
        value = value.replace('-', '')
        value = value.replace(' ', '')
        if not value:
            raise forms.ValidationError('Please enter an isbn consisting only of numbers, spaces and dashes.') 
        # Always return the cleaned data.
        return value
