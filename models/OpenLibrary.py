import requests

class OpenLibrary:
    def __init__(self):
        self.base_url = "https://openlibrary.org"

    def search_books_by_title(self, title, limit="20"):
        url = f"{self.base_url}/search.json?q=title%3A+{title}&limit={limit}"
        response = requests.get(url)
        return response.json()["docs"]

    def search_books_by_author(self, author):
        url = f"{self.base_url}/search.json?author={author}"
        response = requests.get(url)
        return response.json()["docs"]

    def search_books_by_subject(self, subject):
        url = f"{self.base_url}/subjects/{subject}.json"
        response = requests.get(url)
        return response.json()
    
    def search_books_by_similar_subject(self, subjects):
        url = f"{self.base_url}/subjects/{subjects}.json"
        response = requests.get(url)
        return response.json
    
    def search_books_by_isbn(self, isbn):
        url = f"{self.base_url}/isbn/{isbn}.json"
        response = requests.get(url)
        return response.json()
    
    def search_books_by_key(self, key):
        url = f"{self.base_url}{key}.json"
        response = requests.get(url)
        return response.json()
    
    def get_similar_books(self, book_key):
        url = f"{self.base_url}/books{book_key}/similar.json"
        response = requests.get(url)
        return response.json()
    
    def search_author(self, author):
        url = f"{self.base_url}/search/authors.json?q={author}"
        print(url)
        response = requests.get(url)
        return response.json()["docs"]