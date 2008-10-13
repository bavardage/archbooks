from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       ('^add/(\w+)/$', 'archbooks.books.views.add'),
                       ('^show/(\w+)/(\d*)/*', 'archbooks.books.views.show'),
                       ('^edit/(\w+)/(\d+)/$', 'archbooks.books.views.edit'),
                       )
