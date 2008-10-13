from django.contrib.auth.models import User
from django.forms import ModelForm

from models import UserProfile

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name')


class ProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		exclude = ['user',]
