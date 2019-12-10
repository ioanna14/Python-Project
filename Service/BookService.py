from Repository.BookRepository import *
import re


class BookService:
    def __init__(self):
        self._repo = BookRepository()

    def add(self, ID, title, author):
        book = Book(ID, title, author)
        self._repo.add(book)
        return book

    def display(self):
        return self._repo.getAll()

    def remove(self, bookId):
        for index, book in enumerate(self.display()):
            if book.bookId == bookId:
                self._repo.remove(index)
                return book

    def update(self, ID, title, author):
        be = []
        for index, book in enumerate(self.display()):
            if book.bookId == ID:
                be.append(book.bookId)
                be.append(book.title)
                be.append(book.author)
                self._repo.update(index, title, author)
                return be, [book.bookId, book.title, book.author]

    def search(self, choice, match):
        returnable = []
        match = '^' + match
        list_ = self.display()
        for book in list_:
            if choice == '1':
                if re.search(match, book.bookId, re.IGNORECASE):
                    returnable.append(book)
            if choice == '2':
                if re.search(match, book.title, re.IGNORECASE):
                    returnable.append(book)
            if choice == '3':
                if re.search(match, book.author, re.IGNORECASE):
                    returnable.append(book)
        return returnable
