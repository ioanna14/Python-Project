from Domain import Book


class BookRepository:
    def __init__(self):
        self._data = [
            Book('1', 'Dear John', 'Spark'),
            Book('2', 'Ion', 'Lewis'),
            Book('3', 'Othilia', 'Petr'),
            Book('4', 'Twins', 'Mozes'),
            Book('5', 'After you', 'Niki'),
            Book('6', 'Lilly', 'Poppy'),
            Book('7', 'Billy', 'Tracy'),
            Book('8', 'Mary', 'Many'),
            Book('9', 'Harry', 'Peter'),
            Book('10', 'The Nanny', 'Berry')
        ]

    def add(self, book):
        """
        Adds an element to the list.
        :param book: the element we are adding tot the list
        """
        self._data.append(book)

    def remove(self, index):
        """
        Removes an element from the list.
        :param index: the index of the element
        """
        self._data.pop(index)

    def update(self, index, title, author):
        """
        Sets the title and author of a book to new ones.
        :param index: the index of the book
        :param title: the title of the book
        :param author: the author of the book
        """
        self._data[index].title = title
        self._data[index].author = author

    def getAll(self):
        """
        Returns the list of all the elements from the list.
        :return: the list of books
        """
        return self._data[:]
