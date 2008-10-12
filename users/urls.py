from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       ('^login/$', 'django.contrib.auth.views.login'),
                       ('^logout/$', 'django.contrib.auth.views.logout'),
                       ('^profile/$', 'archbooks.users.views.user_profile'),
                       ('^profile/(\d+)/$', 'archbooks.users.views.user_profile'),
                       ('^profile/edit/(\w+)/$', 'archbooks.users.views.edit_profile'),
                       ('^profile/get_user_picture/(\d+)/$', 'archbooks.users.views.get_user_picture'),
                       )
