from Domain import Client, DomainError
from Service.ClientService import ClientService
import unittest


class TestClient(unittest.TestCase):
    def test_Client_class(self):
        c = Client('1', 'George')
        with self.assertRaises(DomainError):
            Client(None, 'Hagi')
        with self.assertRaises(DomainError):
            Client('12', None)
        self.assertEqual(c.clientId, '1')
        self.assertEqual(c.name, 'George')
        self.assertEqual(str(c), 'ID = 1, name = George')
        c1 = Client('20', 'Geo')
        c2 = Client('1', 'George')
        self.assertEqual(c == c1, False)
        self.assertEqual(c == c2, True)


class TestFunctions(unittest.TestCase):
    def test_add(self):
        from Service.ClientService import ClientService
        self._ClientService = ClientService()
        self._ClientService.add('121', 'Johnny')
        self.assertEqual(self._ClientService.display()[-1], Client('121', 'Johnny'))

    def test_remove(self):
        from Service.ClientService import ClientService
        self._ClientService = ClientService()
        self._ClientService.remove('12')
        self.assertEqual(len(self._ClientService.display()), 9)

    def test_update(self):
        from Service.ClientService import ClientService
        self._ClientService = ClientService()
        self._ClientService.update('11', 'Lilly')
        self.assertEqual(self._ClientService.display()[0], Client('11', 'Lilly'))

    def test_search(self):
        from Service.ClientService import ClientService
        self._ClientService = ClientService()
        self.assertEqual(self._ClientService.search('1', '2'), [Client('20', 'Mommy')])
        self.assertEqual(self._ClientService.search('2', 'M'), [Client('17', 'Michael'),
                                                                Client('20', 'Mommy')])
