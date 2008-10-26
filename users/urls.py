from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url('^login/$', 'django.contrib.auth.views.login'),
                       url('^logout/$', 'django.contrib.auth.views.logout'),
                       url('^profile/$', 'archbooks.users.views.user_profile'),
                       url('^profile/(?P<whichuser>\d+)/$', 'archbooks.users.views.user_profile', name='user_profile_id'),
                       url('^profile/edit/(\w+)/$', 'archbooks.users.views.edit_profile'),
                       url('^profile/get_user_picture/(\d+)/$', 'archbooks.users.views.get_user_picture'),
                       )
