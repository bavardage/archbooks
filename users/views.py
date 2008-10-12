from forms import UserForm, ProfileForm

from models import UserProfile
from django.contrib.auth.models import User

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect

import mimetypes

@login_required
def user_profile(request, whichuser = None):
	print request.user.is_authenticated()
	try:
		profile = request.user.get_profile()
	except:
		profile = UserProfile(user=request.user)
		profile.save()
	if whichuser is not None:
		user = get_object_or_404(User, id=whichuser)
	else:
		user = request.user
	c = RequestContext(request, {'for_user': user})
	return render_to_response('users/profile.html', c)
@login_required
def edit_profile(request, edit_what):
	if edit_what not in ('profile', 'user'):
		raise Http404
	elif edit_what == 'user':
		formClass = UserForm
		formInstance = request.user
	else:
		formClass = ProfileForm
		formInstance = request.user.get_profile()
			
	if request.method == 'POST': # If the form has been submitted...
		form = formClass(request.POST,request.FILES,instance=formInstance) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			form.save()
			request.user.message_set.create(message='Profile Successfully Updated')
			return HttpResponseRedirect('../..')
	else:
		form = formClass(instance=formInstance)
	return render_to_response("users/profile_edit.html", RequestContext(request, {'form': form }))

@login_required
def get_user_picture(request, userid):
	try:
		picture = UserProfile.objects.get(id=userid).picture
	except:
		raise Http404
	mimetype = mimetypes.guess_type(picture.path)[0]
	image_data = picture.file.read()
	return HttpResponse(image_data, mimetype=mimetype)
