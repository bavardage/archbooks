from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This is the only required field
    user = models.ForeignKey(User, unique=True)
    distro_of_choice = models.CharField(max_length=100, blank=True)
    irc_nickname = models.CharField(max_length=100, blank=True)
    # The rest is completely up to you...
