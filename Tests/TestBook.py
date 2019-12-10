from Domain import Book, DomainError
import unittest


class TestBook(unittest.TestCase):
    def test_Book_class(self):
        b = Book(12, 'Ion', 'L. Rebreanu')
        with self.assertRaises(DomainError):
            Book(None, 'gica', 'Hagi')
        with self.assertRaises(DomainError):
            Book(123, None, 'Hagi')
        with self.assertRaises(DomainError):
            Book(123, 'Hagi', None)
        self.assertEqual(b.bookId, 12)
        self.assertEqual(b.title, 'Ion')
        self.assertEqual(b.author, 'L. Rebreanu')
        self.assertEqual(str(b), 'ID = 12, title = Ion, author = L. Rebreanu')
        b1 = Book(12, 'John', 'Zummy')
        b2 = Book(12, 'Ion', 'L. Rebreanu')
        self.assertEqual(b == b1, False)
        self.assertEqual(b == b2, True)


class TestFunctions(unittest.TestCase):

    def test_add(self):
        from Service.BookService import BookService
        self._BookService = BookService()
        self._BookService.add('121', 'I an Joe', 'Bobby')
        self.assertEqual(self._BookService.display()[-1], Book('121', 'I an Joe', 'Bobby'))

    def test_remove(self):
        from Service.BookService import BookService
        self._BookService = BookService()
        self._BookService.remove('1')
        self.assertEqual(len(self._BookService.display()), 9)

    def test_update(self):
        from Service.BookService import BookService
        self._BookService = BookService()
        self._BookService.update('1', 'Mummy', 'Helena')
        self.assertEqual(self._BookService.display()[0], Book('1', 'Mummy', 'Helena'))

    def test_search(self):
        from Service.BookService import BookService
        self._BookService = BookService()
        self.assertEqual(self._BookService.search('1', '1'),
                         [Book('1', 'Dear John', 'Spark'),
                          Book('10', 'The Nanny', 'Berry')])
        self.assertEqual(self._BookService.search('2', 'D'),
                         [Book('1', 'Dear John', 'Spark')])
        self.assertEqual(self._BookService.search('3', 'S'),
                         [Book('1', 'Dear John', 'Spark')])
