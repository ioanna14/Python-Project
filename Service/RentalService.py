from Repository.RentalRepository import *


class RentalService:
    def __init__(self):
        self._repo = RentalRepository()

    def add(self, ID, bookId, clientId, rentedDate, returnedDate):
        rental = Rental(ID, bookId, clientId, rentedDate, returnedDate)
        self._repo.add(Rental(ID, bookId, clientId, rentedDate, returnedDate))
        return rental

    def remove(self, rentalId):
        for index, rental in enumerate(self.display()):
            if rental.rentalId == rentalId:
                self._repo.remove(index)

    def remove_client(self, clientId):
        delete_client = []
        rentals = []
        for index, rental in enumerate(self.display()):
            if rental.clientId == clientId:
                delete_client.append(index)
                rentals.append(rental)
        for offset, idx in enumerate(delete_client):
            idx -= offset
            self._repo.remove(idx)
        return rentals

    def remove_book(self, bookId):
        delete_book = []
        rentals =[]
        for index, rental in enumerate(self.display()):
            if rental.bookId == bookId:
                delete_book.append(index)
                rentals.append(rental)
        for offset, idx in enumerate(delete_book):
            idx -= offset
            self._repo.remove(idx)
        return rentals

    def update(self, index, returnedDate):
        self._repo.update(index, returnedDate)

    def display(self):
        return self._repo.getAll()
