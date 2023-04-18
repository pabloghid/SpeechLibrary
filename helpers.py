from models.Book import Book
from models.Author import Author

def get_isbn(book):
    if 'isbn' in book[0]:
        isbn = book[0]['isbn']
        return isbn
    return ''


def create_list_books(books):
    books_list = []
    for book_data in books:
        if book_data:
            book = Book(
                title=book_data["title"],
                author=book_data["author_name"][0] if "author_name" in book_data else "",
                isbn=book_data["isbn"] if "isbn" in book_data else "",
                key=book_data["key"] if "key" in book_data else "",
                )
            if "key" in book_data:
                book.fetch_cover()
                book.fetch_description()
        books_list.append(book.get_book())
    return books_list

def create_list_authors(authors):
    authors_list = []
    print(authors)
    for author_data in authors:
        if author_data:
            author = Author(
                name=author_data["name"],
                birth_date=author_data["birth_date"] if "birth_date" in author_data else "",
                key=(author_data["key"]),
                top_work=author_data["top_work"] if "top_work" in author_data else ""
            )
            author.fetch_books()
        authors_list.append(author.get_author())
    return authors_list