import requests
from models.OpenLibrary import OpenLibrary

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.cover_url = None
        self.description = None

    def fetch_cover(self):
        ol = OpenLibrary()
        book_data = ol.search_books_by_isbn(self.isbn)
        if "cover" in book_data:
            self.cover_url = f"{ol.base_url}{book_data['cover']['large']}"

    def fetch_description(self):
        ol = OpenLibrary()
        book_data = ol.search_books_by_isbn(self.isbn)
        if "description" in book_data:
            self.description = book_data["description"]["value"]

    def get_book(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn}