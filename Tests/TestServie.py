from Domain import Book, Client, Rental
from Service.BookService import BookService
from Service.ClientService import ClientService
from Service.RentalService import RentalService
from Service.Service import Service
import unittest


class TestStatistics(unittest.TestCase):
    def test_most_rented_books(self):
        self.bookS = BookService()
        self.clientS = ClientService()
        self.rentalS = RentalService()
        self._service = Service(self.bookS, self.clientS, self.rentalS)
        self.assertEqual(self._service.most_rented_books()[0], ['Dear John', 3])

    def test_most_active_clients(self):
        self.bookS = BookService()
        self.clientS = ClientService()
        self.rentalS = RentalService()
        self._service = Service(self.bookS, self.clientS, self.rentalS)
        self.assertEqual(self._service.most_active_clients()[0], ['Donna', 3])

    def test_most_rented_author(self):
        self.bookS = BookService()
        self.clientS = ClientService()
        self.rentalS = RentalService()
        self._service = Service(self.bookS, self.clientS, self.rentalS)
        self.assertEqual(self._service.most_rented_author()[0], ['Spark', 3])

    def test_undo(self):
        self.bookS = BookService()
        self.clientS = ClientService()
        self.rentalS = RentalService()
        self.undo_list = []
        self.redo_list = []
        self._service = Service(self.bookS, self.clientS, self.rentalS)
        book = self.bookS.add('121', 'Nope', 'John')
        self._service.append_for_undo([self.bookS.add, book])
        self._service.undo()
        self.assertEqual(len(self.bookS.display()), 10)

    def test_redo(self):
        self.bookS = BookService()
        self.clientS = ClientService()
        self.rentalS = RentalService()
        self.undo_list = []
        self.redo_list = []
        self._service = Service(self.bookS, self.clientS, self.rentalS)
        book = self.bookS.add('121', 'Nope', 'John')
        self._service.append_for_undo([self.bookS.add, book])
        self._service.undo()
        self._service.redo()

    def test_functions_undo_redo(self):
            self.bookS = BookService()
            self.clientS = ClientService()
            self.rentalS = RentalService()
            self.undo_list = []
            self.redo_list = []
            self._service = Service(self.bookS, self.clientS, self.rentalS)
            book = Book('121', 'Nope', 'John')
            client = Client('223', 'Poppy')
            self._service.book_add(book)
            self.assertEqual(len(self.bookS.display()), 11)
            self._service.book_remove(book)
            self.assertEqual(len(self.bookS.display()), 10)
            self._service.client_add(client)
            self.assertEqual(len(self.clientS.display()), 11)
            self._service.client_remove(client)
            self.assertEqual(len(self.clientS.display()), 10)
            rental = Rental('212', '121', '223', ['14', '1', '2018'], ['29', '5', '2019'])
            rentals = [Rental('212', '121', '223', ['14', '1', '2018'], ['29', '5', '2019']),
                       Rental('002', '121', '223', ['18', '3', '2014'], ['29', '7', '2019'])]
            self._service.rental_add(rental)
            self.assertEqual(len(self.rentalS.display()), 11)
            self._service.rental_remove(rental)
            self.assertEqual(len(self.rentalS.display()), 10)
            self._service.add_books_rentals(book, rentals)
            self.assertEqual(len(self.bookS.display()), 11)
            self.assertEqual(len(self.rentalS.display()), 12)
            self._service.remove_books_rentals(book, rentals)
            self.assertEqual(len(self.bookS.display()), 10)
            self.assertEqual(len(self.rentalS.display()), 10)
            self._service.add_client_rentals(client, rentals)
            self.assertEqual(len(self.clientS.display()), 11)
            self.assertEqual(len(self.rentalS.display()), 12)
            self._service.remove_client_rentals(client, rentals)
            self.assertEqual(len(self.clientS.display()), 10)
            self.assertEqual(len(self.rentalS.display()), 10)
            b1 = ['121', 'Nope', 'John']
            c1 = ['223', 'Poppy']
            b = ['121', 'Mommy', 'Lilly']
            c = ['223', 'Mark']
            self.assertEqual(self._service.book_update_undo(b1, b), b)
            self.assertEqual(self._service.book_update_redo(b1, b), b1)
            self.assertEqual(self._service.client_update_undo(c1, c), c)
            self.assertEqual(self._service.client_update_redo(c1, c), c1)


