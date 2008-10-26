from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^accounts/', include('registration.urls')),
                       (r'^accounts/', include('archbooks.users.urls')),
                       (r'^books/', include('archbooks.books.urls')),
                       ('^admin/(.*)$', admin.site.root),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': '/home/ben/Projects/Django/archbooks/media/', 'show_indexes': True}),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
)
