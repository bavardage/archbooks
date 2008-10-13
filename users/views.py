import mimetypes

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from forms import UserForm, ProfileForm
from models import UserProfile


@login_required
def user_profile(request, whichuser = None):
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
	formdict = {'profile': (ProfileForm, request.user.get_profile()),
	            'user': (UserForm, request.user)
                   }
	if edit_what not in formdict:
		raise Http404
	formClass, formInstance = formdict[edit_what]
	if request.method == 'POST': # If the form has been submitted...
		form = formClass(request.POST,
				 request.FILES,
				 instance=formInstance
				 )
		if form.is_valid():
			form.save()
			request.user.message_set.create(
				message='Profile Successfully Updated'
				)
			return HttpResponseRedirect('../..')
	else:
		form = formClass(instance=formInstance)
	return render_to_response("users/profile_edit.html",
				  RequestContext(request, 
						 {'form': form }
						 )
				  )


@login_required
def get_user_picture(request, userid):
	try:
		picture = UserProfile.objects.get(id=userid).picture
	except:
		raise Http404
	mimetype = mimetypes.guess_type(picture.path)[0]
	image_data = picture.file.read()
	return HttpResponse(image_data, mimetype=mimetype)
