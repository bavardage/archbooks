from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This is the only required field
    user = models.ForeignKey(User, unique=True)
    irc_nickname = models.CharField(max_length=100, blank=True)
    picture = models.ImageField(upload_to='userpictures')
    joined = models.DateField(auto_now_add=True)
    misc_info = models.TextField()
    # The rest is completely up to you...
