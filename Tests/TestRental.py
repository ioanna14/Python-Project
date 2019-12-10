from Domain import Rental, DomainError
from Service.RentalService import RentalService
import unittest


class TestRental(unittest.TestCase):
    def test_Rental_class(self):
        r = Rental('92', '12', '7', [12, 1, 2012], [23, 9, 2019])
        with self.assertRaises(DomainError):
            Rental('8', '2', '15', ['1', '30', '2015'], ['35', '1', '2017'])
        with self.assertRaises(DomainError):
            Rental('8', '2', '15', ['1', '3', '2017'], ['35', '1', '2019'])
        with self.assertRaises(DomainError):
            Rental(None, '2', '15', ['1', '3', '2017'], ['30', '1', '2019'])
        self.assertEqual(r.bookId, '12')
        self.assertEqual(r.clientId, '7')
        self.assertEqual(r.rentalId, '92')
        self.assertEqual(r.rentedDate, [12, 1, 2012])
        self.assertEqual(r.returnedDate, [23, 9, 2019])
        self.assertEqual(str(r), 'RentalId = 92, bookId = 12, clientId = 7, rented date:12-1-2012, returned date:'
                                 '23-9-2019')
        r1 = Rental('72', '12', '18', [1, 1, 2012], [3, 9, 2019])
        r2 = Rental('92', '12', '7', [12, 1, 2012], [23, 9, 2019])
        self.assertEqual(r == r1, False)
        self.assertEqual(r == r2, True)


class TestFunctions(unittest.TestCase):
    def test_add(self):
        from Service.RentalService import RentalService
        self._RentalService = RentalService()
        self._RentalService.add('21', '1', '11', ['14', '1', '2018'], ['29', '5', '2019'])
        self.assertEqual(self._RentalService.display()[-1],
                         Rental('21', '1', '11', ['14', '1', '2018'], ['29', '5', '2019']))

    def test_remove(self):
        from Service.RentalService import RentalService
        self._RentalService = RentalService()
        self._RentalService.remove('22')
        self.assertEqual(len(self._RentalService.display()), 9)

    def test_remove_book(self):
        from Service.RentalService import RentalService
        self._RentalService = RentalService()
        self._RentalService.remove_book('1')
        self.assertEqual(len(self._RentalService.display()), 7)

    def test_remove_client(self):
        from Service.RentalService import RentalService
        self._RentalService = RentalService()
        self._RentalService.remove_client('12')
        self.assertEqual(len(self._RentalService.display()), 7)

    def test_update(self):
        from Service.RentalService import RentalService
        self._RentalService = RentalService()
        self._RentalService.update(0, ['30', '11', '2019'])
        self.assertEqual(self._RentalService.display()[0],
                         Rental('21', '1', '11', ['14', '1', '2018'], ['30', '11', '2019']))
