'''
TODO LIST
Books are a collection of ISBNs
 - what is cached locally, and what happens when local clashes with ISBN?
 - what happens when another ISBN is added - is this just added ad-hoc, is it checked to make sure title and author match the other ISBN(s), what if there are subtle spelling differences, or e.g. The Golden Compass vs Northern Lights - probably better to make it creator-controlled
 - who has ultimate control over books - the creator, the users, mods?
 - things like cover images, maybe should be multiple submissions, the top voted one is shown with something like 'view others' below it
 - should links for books be creator or users?
 - maybe like the add a review mechanism, an add-a-link?
 - should there be comments too? comments being less than a review
 - should reviews be approved first?

Series
 - series are a collection of books









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
