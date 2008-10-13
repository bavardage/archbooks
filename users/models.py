from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    irc_nickname = models.CharField(max_length=100, blank=True)
    picture = models.ImageField(upload_to='userpictures')
    joined = models.DateField(auto_now_add=True)
    misc_info = models.TextField(blank=True)
