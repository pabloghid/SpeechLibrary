from models.Book import Book

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
                isbn=book_data["isbn"] if "isbn" in book_data else "" 
                )
        books_list.append(book.get_book())
    return books_list