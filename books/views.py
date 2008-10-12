from models import Genre, Author, Series, Book, Review
from forms import GenreForm, AuthorForm, SeriesForm, BookForm, ReviewForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import list_detail

modeldict = {'book': (Book, BookForm), 'author': (Author, AuthorForm), 'genre': (Genre, GenreForm), 'series': (Series, SeriesForm), 'review': (Review, ReviewForm)}

@login_required
def add(request, add_what = None):
    if add_what not in modeldict:
        raise Http404

    model, modelform = modeldict[add_what]
    popup = (request.GET['popup'] if 'popup' in request.GET else None)
    print "popup is", popup
    specialfields = {'authors': 'author', 'series': 'series', 'genre': 'genre', 'for_book': 'book'}
    
    if request.method == 'POST':
        form = modelform(request.POST, request.FILES)
        if form.is_valid():
            #print dir(form.fields)
            saved = form.save(commit=False)
            saved.created_by = request.user
            saved.save()
            try:
                form.save_m2m()
            except AttributeError:
                pass
            except:
                print "failed doing save_m2m"
                raise
            if popup:
                return render_to_response('books/popup_close.html', RequestContext(request, {'added_what': saved, 'popup': popup}))
            else:
                return render_to_response('books/done.html', RequestContext(request, {'added_what': saved, 'what_is_it': add_what}))
    else: #form not already created - make one!
        form = modelform()
    return render_to_response('books/add.html', RequestContext(request, {'adding_what': add_what.title(), 'form': form, 'specials': specialfields}))

def show(request, show_what, id=None):
    if show_what not in modeldict:
        raise Http404
    model = modeldict[show_what][0]
    if id is None:
        list_info = {
            'queryset' :   model.objects.all(),
            'allow_empty': True,
            }
        return list_detail.object_list(request,
                                       queryset = model.objects.all(),
                                       allow_empty = True,
                                       )

    else:
        if model.objects.filter(id=id).count():
            return list_detail.object_detail(request,
                                             queryset = model.objects.all(),
                                             object_id = id,
                                             template_object_name = show_what,
                                             )
        else:
            raise Http404
