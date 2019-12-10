from Domain import Book, Rental, Client


class Service:
    def __init__(self, bookS, clientS, rentalS):
        self.bookS = bookS
        self.clientS = clientS
        self.rentalS = rentalS
        self.undo_list = []
        self.redo_list = []
        self.action = False

    def most_rented_books(self):
        statistics_books = []
        for book in self.bookS.display():
            counter = 0
            for rental in self.rentalS.display():
                if book.bookId == rental.bookId:
                    counter += 1
            statistics_books.append([book.title, counter])
        return sorted(statistics_books, key=lambda elm: elm[1], reverse=True)

    def most_active_clients(self):
        statistics_clients = []
        for client in self.clientS.display():
            counter = 0
            for rental in self.rentalS.display():
                if client.clientId == rental.clientId:
                    counter += 1
            statistics_clients.append([client.name, counter])
        return sorted(statistics_clients, key=lambda elm: elm[1], reverse=True)

    def most_rented_author(self):
        statistics_authors = []
        authors = []
        for book in self.bookS.display():
            counter = 0
            for author in authors:
                if book.author == author:
                    counter += 1
            if counter == 0:
                authors.append(book.author)
        for book in self.bookS.display():
            number = 0
            for author in authors:
                if book.author == author:
                    for rental in self.rentalS.display():
                        if book.bookId == rental.bookId:
                            number += 1
                    statistics_authors.append([book.author, number])
        return sorted(statistics_authors, key=lambda elm: elm[1], reverse=True)

    def book_remove(self, obj):
        self.bookS.remove(obj.bookId)

    def book_add(self, obj):
        self.bookS.add(obj.bookId, obj.title, obj.author)

    def client_add(self, obj):
        self.clientS.add(obj.clientId, obj.name)

    def client_remove(self, obj):
        self.clientS.remove(obj.clientId)

    def rental_add(self, obj):
        self.rentalS.add(obj.rentalId, obj.bookId, obj.clientId, obj.rentedDate, obj.returnedDate)

    def rental_remove(self, obj):
        self.rentalS.remove(obj.rentalId)

    def remove_books_rentals(self, book, rentals):
        self.book_remove(book)
        for rental in rentals:
            self.rental_remove(rental)

    def add_books_rentals(self, book, rentals):
        self.book_add(book)
        for rental in rentals:
            self.rental_add(rental)

    def remove_client_rentals(self, client, rentals):
        self.client_remove(client)
        for rental in rentals:
            self.rental_remove(rental)

    def add_client_rentals(self, client, rentals):
        self.client_add(client)
        for rental in rentals:
            self.rental_add(rental)

    def book_update_redo(self, obj1, obj2):
        self.bookS.update(obj1[0], obj1[1], obj1[2])
        return obj1

    def client_update_redo(self, obj1, obj2):
        self.clientS.update(obj1[0], obj1[1])

        return obj1

    def book_update_undo(self, obj1, obj2):
        self.bookS.update(obj2[0], obj2[1], obj2[2])
        return obj2

    def client_update_undo(self, obj1, obj2):
        self.clientS.update(obj2[0], obj2[1])
        return obj2

    def append_for_undo(self, obj):
        if self.action:
            self.redo_list.clear()
            self.action = False
        self.undo_list.append(obj)

    def undo(self):
        operation = {
            self.bookS.add: self.book_remove,
            self.clientS.add: self.client_remove,
            self.rentalS.add: self.rental_remove,
            self.bookS.remove: self.add_books_rentals,
            self.clientS.remove: self.add_client_rentals,
            self.bookS.update: self.book_update_undo,
            self.clientS.update: self.client_update_undo,
            self.rentalS.update: self.rentalS.update,
        }
        if len(self.undo_list) == 0:
            raise ValueError('No more undoes!')
        _list = self.undo_list.pop(-1)
        if len(_list) == 2:
            f = operation[_list[0]]
            o = _list[1]
            f(o)
        elif len(_list) == 3:
            f = operation[_list[0]]
            o1 = _list[1]
            o2 = _list[2]
            f(o1, o2)
        self.redo_list.append(_list)
        self.action = True

    def redo(self):
        operation = {self.bookS.add: self.book_add,
                     self.clientS.add: self.client_add,
                     self.rentalS.add: self.rental_add,
                     self.bookS.remove: self.remove_books_rentals,
                     self.clientS.remove: self.remove_client_rentals,
                     self.bookS.update: self.book_update_redo,
                     self.clientS.update: self.client_update_redo,
                     self.rentalS.update: self.rentalS.update
                     }
        if len(self.redo_list) == 0:
            raise ValueError('No more redoes!')
        _list = self.redo_list.pop(-1)
        if len(_list) == 2:
            f = operation[_list[0]]
            o = _list[1]
            f(o)
        elif len(_list) == 3:
            f = operation[_list[0]]
            o1 = _list[1]
            o2 = _list[2]
            f(o1, o2)
        self.undo_list.append(_list)
