'''
TODO LIST
---------------------------
DEFINE WHAT'S WHAT
---------------------------
Books are a collection of ISBNs
 - what is cached locally, and what happens when local clashes with ISBN?
 - what happens when another ISBN is added - is this just added ad-hoc, is it checked to make sure title and author match the other ISBN(s), what if there are subtle spelling differences, or e.g. The Golden Compass vs Northern Lights - probably better to make it creator-controlled
 - who has ultimate control over books - the creator, the users, mods?
 - things like cover images, maybe should be multiple submissions, the top voted one is shown with something like 'view others' below it
 - should links for books be creator or users?
 - maybe like the add a review mechanism, an add-a-link?
 - should there be comments too? comments being less than a review
 - should reviews be approved first?

   to summarise - perhaps a 'Book' object in the database should be mainly metadata - ratings, who owns this, reviews, comments, views, suggestions, etc, with some cached info derived from the ISBNs.

Series
 - series are a collection of books
 nothing too fancy there


DEFINE HOW THE ACTION OF CREATING A BOOK GOES
 - user enters title and author, searches for an isbn, chooses an isbn, and confirms
 - book object is created in the database, fields filled from ISBN data but not initially 'VISIBLE' <-- define a term, like wordpress 'published' vs 'unpublished' but this would be confusing for a book - need another term
 - user is taken to an 'edit book' page, where they can add to/amend the cached isbn data, checks a box to make VISIBLE
    - this page is the same as that used generally to edit a book object
 - book is now viewable by the general public


HOW ARE BOOKS CONTRIBUTED TO BY USERS (NOT CREATORS)
 - users view the book
 - they make suggestions somehow which are approved by the creator/admins/etc
  - how are suggestions done
  - maybe the book object is cloned in the database, with the user as the 'creator' of this, the user taken to the edit-book page, they change what they want to, and submit, but this cloned book has some field is_suggestion marked positive
  - the original creator logs in, sees a suggestion has been made, views it
     - how is it merged
  - maybe suggestions are made per-field? GenreSuggestion SummarySuggestion TitleSuggestion - what do we need to make 'suggestable' - should they be able to change title, or is this just stupid
          - what title do we go with when there are multiple titles? i.e. Golden Compass Northern Lights edit wars
  - links and such - should these be vetted first, vetted by whom? vetted by contributor I'd think
    - users want to add a link, they click add-new-link and are taken to an add-new-link page (or perhaps a form pops up in the page, but again, UI)
    - they enter the url and a title for the url i.e. Amazon Link, Bookchan Link, Picture of yo momma naked
    - links are approved by the creator/admins











------------------
MOSTLY OBSELETE
---------------

- frontpage
- navigation
- set pagination to be sane, make it configable
- approve book picture backend
- show book after creation?
- change book creation form field order
- valid html
    -onClick onclick

- some way of editing author names etc if incorrect, or make people confirm beforehand, or something
 - also figure out a way of stopping books written by Ass Face or w/e - maybe again use isbn for this
- make a genre hierarchy
- make activated have login form already autofilled

- make genre description optional
----------------------------------------------------
DONE - make other info for user profile accept null/blank

DONE - only allow people who made stuff able to edit stuff!!!
DONE - put links for editing if user created the content
- make frontpage sane
DONE - enable display of reviews, etc
DONE - do add/review/?forbook = some id
DONE - register page
DONE - I HAVE EDITED SOME STUFF- edit stuff - WTF DOES THAT MEAN - write some decent TODOS nublar
DOEN in DATABASE- book pictures?
DONE - add pictures to book_detail
- MOAR/tidy css
DONE FAIRLY COMPLETELY - isbn auto fill
CANCELLED - let ISBN be optional 
DONE - add voting for books
DONE - in users.views use get or create for profile
DONE - paginate book display
   -set pagination to a sane value, and make it configable
DONE- make pictures have to be approved by someone with permissions
 - add in capablitiy to approve book picture 
- maybe redirect to showing book after creation
- order form fields when adding a book
- make valid html
- replace onClick with onclick
DONE - add isbn to book detail
DONE - add favicon(is that correct, no) add little image to thingy
- some way of editing author names etc if incorrect, or make people confirm beforehand, or something
 - also figure out a way of stopping books written by Ass Face or w/e - maybe again use isbn for this
- make a genre hierarchy
IDONE - update GIT say last.fm for books
DONE - replace HTTP_ROOT with {{site}}
DONE - make login form have registration form built in - fancy javascript showy hidey etc
- make activated have login form already autofilled
'''
