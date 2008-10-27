from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url('^add/(\w+)/$', 'archbooks.books.views.add'),
                       url('^show/(\w+)/(\d*)/*', 'archbooks.books.views.show'),
                       url('^edit/(\w+)/(\d+)/$', 'archbooks.books.views.edit'),
                       url('^ratebook/(?P<id>\d+)/(?P<up_or_down>[\+-])/$', 
                           'archbooks.books.views.rate_book', name='rate_book'),
                       url('^get_isbn/$', 'archbooks.books.views.get_isbn'),
                       )
