from models.OpenLibrary import OpenLibrary

class Book:
    def __init__(self, title, author, key, isbn):
        self.title = title
        self.author = author
        self.key = key
        self.isbn = isbn
        self.cover = None
        self.description = None

    def fetch_cover(self):
        ol = OpenLibrary()
        book_data = ol.search_books_by_key(self.key)
        if "covers" in book_data:
            self.cover = book_data['covers'][0]


    def fetch_description(self):
        ol = OpenLibrary()
        book_data = ol.search_books_by_key(self.key)
        if "description" in book_data:
            self.description = book_data["description"]

    def get_book(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn, "key": self.key, "cover": self.cover, "description": self.description}