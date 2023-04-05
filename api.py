import requests
from config import *

class Search:
    def __init__(self, input):
        self.name = input
        self.endpoint = '/search.json?'
        self.sort = '&sort='
        self.limit = '&limit='

    def searchBook(self, order='', limit=''):
        type = 'title='
        url = BASE_URL + self.endpoint + type + self.name
        url = BASE_URL + self.endpoint + type + self.name + self.sort + order + self.limit + limit
        response = requests.get(url)
        return response.json()
    
    def searchAuthor(self, order=''):
        type = 'author='
        url = BASE_URL + self.endpoint + type + self.name
        response = requests.get(url)
        return response.json()
    
    def searchBySubject(self, order=''):
        type = 'subject='    
        if order == '':
            url = BASE_URL + self.endpoint + type + self.name
        else:
            url = BASE_URL + self.endpoint + type + self.name + self.sort + order + '&limit=1'
        response = requests.get(url)
        return response.json()
    
    def searchByPlace(self, order=''):
        type = 'place='    
        if order == '':
            url = BASE_URL + self.endpoint + type + self.name
        else:
            url = BASE_URL + self.endpoint + type + self.name + self.sort + order
        response = requests.get(url)
        return response.json()
    
    def searchSimilarBooks(self, order=''):
        bookData = self.searchBook(limit='1')
        bookSubject = bookData['docs']['title']
        print(bookSubject)
    
    
test = Search('O senhor dos aneis')
#print(test.searchBook(limit='1'))
test.searchSimilarBooks()
#print(test.searchBook(limit='1'))


