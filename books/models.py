from django.db import models
from django.contrib.auth.models import User

from fields import ISBNFormField

class ISBNField(models.CharField):
    def __init__(self, book_title, *args, **kwargs):
        self.book_title = book_title
        kwargs['max_length'] = 13
        super(ISBNField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        #kwargs['book_title_field'] = self.book_title
        defaults = {'form_class': ISBNFormField}
        defaults.update(kwargs)
        return super(ISBNField, self).formfield(**defaults)


class BookModel(models.Model):
    created_by = models.ForeignKey(User, related_name='created_by_user_%(class)s')
    
    class Meta:
        abstract = True


class Genre(BookModel):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    
    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ["name",]


class Author(BookModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ["last_name",]


class Series(BookModel):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return u'The %s Series' % (self.name)

    class Meta:
        ordering = ["name",]
        verbose_name_plural = "Series"


class Book(BookModel):
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    ISBN = ISBNField(title, help_text="Fill in the title and author,\
 then click '...' to autofill isbn and optionally, blurb")
    series = models.ForeignKey(Series, blank=True, null=True)
    genre = models.ForeignKey(Genre)
    blurb = models.TextField()
    positive_ratings = models.IntegerField(default=0)
    negative_ratings = models.IntegerField(default=0)
    #ISBN = models.CharField(max_length=20) #should be an isbn field
    amazon_link = models.URLField(blank=True)
    bookchan_link = models.URLField(blank=True)
    rated_by = models.ManyToManyField(User, blank=True)
    cover_image = models.ImageField(upload_to='book_coverimages', blank=True)
    cover_image_authenticated = models.BooleanField(blank=False)
    
    def __unicode__(self):
        return self.title
    
    def get_rating_percentage(self):
        positive_ratings, negative_ratings = self.positive_ratings, self.negative_ratings
        if positive_ratings == 0 and negative_ratings == 0:
            return u'50%'
        else:
            return u'%i%%' % ((float(positive_ratings) / (positive_ratings + negative_ratings))*100)
    
    def get_authors(self):
        return u', '.join([str(author) for author in self.authors.all()])

    class Meta:
        ordering = ["title",]
        permissions = (
            ("can_authenticate_picture", "Can authenticate picture"),
        )


class Review(BookModel):
    RATING_CHOICES = (
        (0, 'pathetic'),
        (1, 'could have been worse'),
        (2, 'not great'),
        (3, 'mediocre'),
        (4, 'enjoyable'),
        (5, 'best thing evarr')
        )
    for_book = models.ForeignKey(Book)
    rating = models.SmallIntegerField(choices=RATING_CHOICES)
    review_contents = models.TextField()
