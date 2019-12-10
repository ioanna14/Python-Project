"""
 Book: <bookId>, <title>, <author>.
 Client: <clientId>, <name>.
 Rental: <rentalID>, <bookId>, <clientId>, <rented date>, <returned date>.
"""


class DomainError(Exception):
    pass


class Book:
    def __init__(self, bookId, title, author):
        if bookId is None:
            raise DomainError("Books ID can't be None.")
        self._bookId = bookId
        self.title = title
        self.author = author

    @property
    def bookId(self):
        return self._bookId

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, newTitle):
        if newTitle is None or len(newTitle) < 3:
            raise DomainError("The name of the title is not long enough.")
        self._title = newTitle

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, newAuthor):
        if newAuthor is None or len(newAuthor) < 3:
            raise DomainError("Name of the author is not long enough.")
        self._author = newAuthor

    def __str__(self):
        return 'ID = ' + str(self.bookId) + ', title = ' + self.title + ', author = ' + self.author

    def __eq__(self, other):
        if self.bookId == other.bookId and self.title == other.title and self.author == other.author:
            return True
        else:
            return False


class Client:
    def __init__(self, clientId, name):
        if clientId is None:
            raise DomainError("Client ID can't be None.")
        self._clientId = clientId
        self.name = name

    @property
    def clientId(self):
        return self._clientId

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        if newName is None or len(newName) < 3:
            raise DomainError("Name is not long enough.")
        self._name = newName

    def __str__(self):
        return 'ID = ' + self.clientId + ', name = ' + self.name

    def __eq__(self, other):
        if self.clientId == other.clientId and self.name == other.name:
            return True
        else:
            return False


class Rental:
    def __init__(self, rentalId, bookId, clientId, rentedDate, returnedDate):
        if rentalId is None or bookId is None or clientId is None:
            raise DomainError("You forgot to put the ID.")
        self._rentalId = rentalId
        self._bookId = bookId
        self._clientId = clientId
        self.rentedDate = rentedDate
        self.returnedDate = returnedDate

    @property
    def rentalId(self):
        return self._rentalId

    @property
    def bookId(self):
        return self._bookId

    @property
    def clientId(self):
        return self._clientId

    @property
    def rentedDate(self):
        return self._rentedDate

    @rentedDate.setter
    def rentedDate(self, newDate):
        if len(newDate) < 3 or int(newDate[0]) > 31 or int(newDate[0]) < 1 \
                or int(newDate[1]) > 12 or int(newDate[1]) < 1:
            raise DomainError("Incorrect date!")
        self._rentedDate = newDate

    @property
    def returnedDate(self):
        return self._returnedDate

    @returnedDate.setter
    def returnedDate(self, newDate):
        if len(newDate) < 3 or int(newDate[0]) > 31 or int(newDate[0]) < 1 \
                or int(newDate[1]) > 12 or int(newDate[1]) < 1:
            raise DomainError("Incorrect date!")
        self._returnedDate = newDate

    def __str__(self):
        return 'RentalId = ' + self.rentalId + ', bookId = ' + self.bookId + ', clientId = ' + self.clientId \
               + ', rented date:' + str(self.rentedDate[0]) + '-' \
               + str(self.rentedDate[1]) + '-' + str(self.rentedDate[2]) \
               + ', returned date:' + str(self.returnedDate[0]) \
               + '-' + str(self.returnedDate[1]) + '-' + str(self.returnedDate[2])

    def __eq__(self, other):
        if self.rentalId == other.rentalId and self.bookId == other.bookId and self.clientId == other.clientId \
                and self.rentedDate == other.rentedDate and self.returnedDate == other.returnedDate:
            return True
        else:
            return False
