from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import list_detail

from forms import GenreForm, AuthorForm, SeriesForm, BookForm, ReviewForm
from isbndb import IsbnDB
from models import Genre, Author, Series, Book, Review


modeldict = {'book': (Book, BookForm),
             'author': (Author, AuthorForm),
             'genre': (Genre, GenreForm),
             'series': (Series, SeriesForm),
             'review': (Review, ReviewForm)
             }
linkedfields = {'authors': 'author',
                 'series': 'series',
                 'genre': 'genre',
                 'for_book': 'book',
                 }
specialfields = {'ISBN': ('archbooks.books.views.get_isbn', 
                          [], 
                          "?book_title=' + document.getElementById('id_title').value + '&author=' + getTextOfSelectedOption(\'id_authors\') + '")}

isbn_db = IsbnDB()

@login_required
def add(request, add_what = None):
    if add_what not in modeldict:
        raise Http404
    model, modelform = modeldict[add_what]
    popup = request.GET.get('popup', None)
    if request.method == 'POST':
        form = modelform(request.POST, request.FILES)
        if form.is_valid():
            saved = form.save(commit=False)
            saved.created_by = request.user
            saved.save()
            try:
                form.save_m2m()
            except AttributeError:
                pass #Not all forms need, and hence have, a save_m2m() method
            if popup:
                return render_to_response('books/popup_close.html',
                                          RequestContext(request,
                                                         {'added_what': saved,
                                                          'popup': popup
                                                          }
                                                         )
                                          )
            else:
                request.user.message_set.create(message='%s Added Successfully' % add_what.title())
                return render_to_response('books/done.html',
                                          RequestContext(request,
                                                         {'added_what': saved,
                                                          'what_is_it': add_what
                                                          }
                                                         )
                                          )
    else: #form not already created - make one!
        initial_values = {}
        for autofill, function in modelform.Meta.get_autofill:
            if callable(function):
                try:
                    initial_values[autofill] = function(request.GET.get(autofill, ''))
                except TypeError:
                    pass #if value doesn't go with the function passed, then 'taint so ignore
                except ValueError:
                    pass
        #print "initial values are", initial_values
        form = modelform(initial=initial_values)
    return render_to_response('books/add.html',
                              RequestContext(request,
                                             {'adding_what': add_what.title(),
                                              'form': form,
                                              'linked': linkedfields,
                                              'specials': specialfields,
                                              }
                                             )
                              )


def show(request, show_what, id=None):
    if show_what not in modeldict:
        raise Http404
    model = modeldict[show_what][0]
    if not id:
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


@login_required
def edit(request, edit_what, id):
    if edit_what not in modeldict:
        raise Http404
    model,modelform = modeldict[edit_what]
    modelinstance = get_object_or_404(model, id=id)
    if request.method == 'POST':
        form = modelform(request.POST, request.FILES,instance=modelinstance)
        if form.is_valid():
            if edit_what == 'book':
                if modelinstance.cover_image:
                    modelinstance.cover_image.delete()
            added_what = form.save()
            return render_to_response('books/done.html',
                                      RequestContext(request, 
                                                     {'added_what': added_what,
                                                      'what_is_it': edit_what
                                                      }
                                                     )
                                      )
    else:
        form = modelform(instance=modelinstance)
    return render_to_response("books/add.html", 
                              RequestContext(request,
                                             {'form': form,
                                              'specials': specialfields,
                                              'linked': linkedfields,
                                              }
                                             )
                              )


@login_required
def rate_book(request, id, up_or_down):
    try:
        book = Book.objects.get(id=id)
    except DoesNotExist:
        raise
    if book.rated_by.filter(id=request.user.id).count():
        request.user.message_set.create(message='You have already rated this')
        return HttpResponseRedirect(reverse(show, args=['book', id]))
    if up_or_down == '+':
        book.positive_ratings += 1
    else:
        book.negative_ratings += 1
    book.rated_by.add(request.user)
    book.save()
    request.user.message_set.create(message='Your rating was taken into consideration')
    return show(request, 'book', id)
        

def get_isbn(request):
    title = request.GET.get('book_title', None)
    if title is None:
        raise Http404
    author = request.GET.get('author', None)
    if author is None:
        index = 'title'
        value = title
    else:
        index = 'combined'
        value = '%s by %s' % (title, author)
    BookData = isbn_db.get_book_data(index, value, {'Title': 'title', 'AuthorsText': 'authors', 'Summary': 'summary'})
    return render_to_response('books/get_isbn.html',
                              RequestContext(request,
                                             {'bookdata': BookData }
                                             )
                              )
