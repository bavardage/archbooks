from django.db import models
from django.contrib.auth.models import User

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
        ordering = ["name"]

class Author(BookModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    class Meta:
        ordering = ["last_name"]

class Series(BookModel):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return u'The %s Series' % (self.name)
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Series"

class Book(BookModel):
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    series = models.ForeignKey(Series, blank=True, null=True)
    genre = models.ForeignKey(Genre, blank=True)
    blurb = models.TextField()
    positive_ratings = models.IntegerField(default=0)
    negative_ratings = models.IntegerField(default=0)
    ISBN = models.CharField(max_length=20) #should be an isbn field
    amazon_link = models.URLField(blank=True)
    bookchan_link = models.URLField(blank=True)
    rated_by = models.ManyToManyField(User, blank=True)
    
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ["title"]

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
