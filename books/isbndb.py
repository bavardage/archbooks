#!/usr/bin/env python
import urllib
from xml.dom import minidom

import config


class IsbnDB:
    def __init__(self, api_key=config.ISBNDB_API_KEY):
        self.api_key = api_key
        
    def sanitise(self, string_in):
        return string_in.replace(' ', '+')

    def get_book_data(self, index, value, what_data, results='texts'):
        books = [] 
        url='http://isbndb.com/api/books.xml?access_key=%s\
&index1=%s&value1=%s&results=%s' % (self.api_key, index, self.sanitise(value), results)
        doc = minidom.parse(urllib.urlopen(url))
        for BookData in doc.getElementsByTagName('BookData'):
            data = {}
            data['isbn'] = BookData.getAttribute('isbn13')
            for childNode in BookData.childNodes:
                if childNode.nodeName in what_data:
                    try:
                        data[what_data[childNode.nodeName]] = childNode.firstChild.data
                    except:
                        data[what_data[childNode.nodeName]] = ''

            books.append(data)
        return books
    
    def validate_isbn(self, isbn, title):
        '''loosely validate the isbn - query isbndb, return true if ok, false otherwise'''
        data = self.get_book_data('isbn', isbn, {'AuthorsText': 'authors', 'Title': 'title'})
        print "isbn data is ", data
        if not len(data):
            return False
        elif data[0]['title'].lower().find(title.lower()) == -1:
            if data[0]['title'].lower().find(title.lower().replace('the', '').strip()) == -1:
                return False
            else:
                return True
        else:
            return True

if __name__ == '__main__':
    db = IsbnDB(config.ISBNDB_API_KEY)
    #print db.get_book_data('combined', 'good+omens', {'AuthorsText': 'authors', 'Title': 'title'})
    #print db.get_book_data('isbn', '123', {'Title': 'title'})
    #print db.get_book_data('isbn', '9780517126646', {'Title': 'title'})
    print db.validate_isbn('9780517126646', 'Good Omens') #true
    print db.validate_isbn('978051712664', 'Good Omens') #false
    print db.validate_isbn('9780517126646', 'Eragon') #false
