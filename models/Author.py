from models.OpenLibrary import OpenLibrary
from models.Book import Book

class Author:
    def __init__(self, name, birth_date, key, top_work):
        self.name = name
        self.birth_date = birth_date
        self.key = str(key)
        self.top_work = top_work
        self.books = []

    def fetch_books(self):
        ol = OpenLibrary()
        book_data = ol.search_books_by_author(self.name)
        for book in book_data:
            self.books.append(Book(book["title"], self.name, book["key"], book["isbn"][0] if "isbn" in book_data else ""))

    def get_author(self):
        return {"name": self.name, "birth_date": self.birth_date, "key": self.key, "top_work": self.top_work, "books": self.books}