from django.forms import ModelForm

from django.contrib.auth.models import User
from models import UserProfile
class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name')
	
class ProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('distro_of_choice', 'irc_nickname')