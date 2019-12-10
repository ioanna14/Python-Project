from Service.RentalService import *
import datetime
from Service.Service import Service


class UserError(Exception):
    pass


class UserInterface:
    def __init__(self, bookS, clientS, rentalS):
        self._BookService = bookS
        self._ClientService = clientS
        self._RentalService = rentalS
        self._Service = Service(bookS, clientS, rentalS)

    @staticmethod
    def print_menu():
        print('1. List.')
        print('2. Add.')
        print('3. Remove.')
        print('4. Update.')
        print('5. Rent.')
        print('6. Return.')
        print('7. Search')
        print('8. Statistics.')
        print('9. Undo.')
        print('10. Redo.')
        print('0. Exit.')

    @staticmethod
    def read_command():
        command = input('>')
        return command

    def add_menu(self):
        print('1. Book.')
        print('2. Client.')
        choice = input('>')
        if choice == '1':
            bookId = input('ID: ')
            c = 0
            for book in self._BookService.display():
                if book.bookId == bookId:
                    c += 1
            if c != 0:
                raise UserError('The book already exist!')
            title = input('Title: ')
            author = input('Author: ')
            book = self._BookService.add(bookId, title, author)
            self._Service.append_for_undo([self._BookService.add, book])
        elif choice == '2':
            c = 0
            clientId = input('ID: ')
            for client in self._ClientService.display():
                if client.clientId == clientId:
                    c += 1
            if c != 0:
                raise UserError('The client already exists!')
            name = input('Name: ')
            client = self._ClientService.add(clientId, name)
            self._Service.append_for_undo([self._ClientService.add, client])
        else:
            raise UserError('Bad choice!')

    def list_menu(self):
        print('1. Books.')
        print('2. Clients.')
        print('3. Rentals.')
        choice = input('>')
        if choice == '1':
            self.print_list(self._BookService.display())
        elif choice == '2':
            self.print_list(self._ClientService.display())
        elif choice == '3':
            self.print_list(self._RentalService.display())
        else:
            raise UserError('Bad choice!')

    def remove_menu(self):
        print('1. Books.')
        print('2. Clients.')
        choice = input('>')
        if choice == '1':
            bookId = input('ID: ')
            c = 0
            for book in self._BookService.display():
                if book.bookId == bookId:
                    c += 1
            if c == 0:
                raise UserError('The book does not exist!')
            else:
                b = self._BookService.remove(bookId)
                r = self._RentalService.remove_book(bookId)
                self._Service.append_for_undo([self._BookService.remove, b, r])
        elif choice == '2':
            c = 0
            clientId = input('ID: ')
            for client in self._ClientService.display():
                if client.clientId == clientId:
                    c += 1
            if c == 0:
                raise UserError('The client does not exist!')
            else:
                c = self._ClientService.remove(clientId)
                r = self._RentalService.remove_client(clientId)
                self._Service.append_for_undo([self._ClientService.remove, c, r])
        else:
            raise UserError('Bad choice!')

    def update_menu(self):
        print('1. Books.')
        print('2. Clients.')
        choice = input('>')
        if choice == '1':
            bookId = input('ID: ')
            c = 0
            for book in self._BookService.display():
                if book.bookId == bookId:
                    c += 1
            if c == 0:
                raise UserError('The book does not exist!')
            title = input('Title: ')
            author = input('Author: ')
            be, ba = self._BookService.update(bookId, title, author)
            self._Service.append_for_undo([self._BookService.update, ba, be])
        elif choice == '2':
            c = 0
            clientId = input('ID: ')
            for client in self._ClientService.display():
                if client.clientId == clientId:
                    c += 1
            if c == 0:
                raise UserError('The client does not exist!')
            name = input('Name: ')
            ce, ca = self._ClientService.update(clientId, name)
            self._Service.append_for_undo([self._ClientService.update, ca, ce])
        else:
            raise UserError('Bad choice!')

    def rent_menu(self):
        bookId = input('Book ID: ')
        c = 0
        for book in self._BookService.display():
            if book.bookId == bookId:
                c += 1
        if c == 0:
            raise UserError('The book does not exist!')
        c = 0
        clientId = input('Client ID: ')
        for client in self._ClientService.display():
            if client.clientId == clientId:
                c += 1
        if c == 0:
            raise UserError('The client does not exist!')
        for rental in self._RentalService.display():
            if rental.bookId == bookId:
                print('pass')
                date = rental.returnedDate
                x = datetime.datetime.now()
                if int(date[2]) <= x.year:
                    print('pass_year')
                    if int(date[1]) <= x.month:
                        print('pass_month')
                        if int(date[0]) < x.day:
                            rentalId = input('ID: ')
                            rentedDate = [x.strftime("%d"), x.strftime("%m"), x.strftime("%Y")]
                            y = x + datetime.timedelta(days=30)
                            returnedDate = [y.strftime("%d"), y.strftime("%m"), y.strftime("%Y")]
                            r = self._RentalService.add(rentalId, bookId, clientId, rentedDate, returnedDate)
                            self._Service.append_for_undo([self._RentalService.add, r])
                            return
                        else:
                            raise UserError('The book is already rented!')
                    else:
                        raise UserError('The book is already rented!')
                else:
                    raise UserError('The book is already rented!')
            else:
                x = datetime.datetime.now()
                rentalId = input('ID: ')
                rentedDate = [x.strftime("%d"), x.strftime("%m"), x.strftime("%Y")]
                y = x + datetime.timedelta(days=30)
                returnedDate = [y.strftime("%d"), y.strftime("%m"), y.strftime("%Y")]
                r = self._RentalService.add(rentalId, bookId, clientId, rentedDate, returnedDate)
                self._Service.append_for_undo([self._RentalService.add, r])
                return

    def return_menu(self):
        bookId = input('Book ID: ')
        c = 0
        for book in self._BookService.display():
            if book.bookId == bookId:
                c += 1
        if c == 0:
            raise UserError('The book does not exist!')
        c = 0
        clientId = input('Client ID: ')
        for client in self._ClientService.display():
            if client.clientId == clientId:
                c += 1
        if c == 0:
            raise UserError('The client does not exist!')
        for index, rental in enumerate(self._RentalService.display()):
            if rental.bookId == bookId and rental.clientId == clientId:
                x = datetime.datetime.now()
                returnedDate = [x.strftime("%d"), x.strftime("%m"), x.strftime("%Y")]
                self._RentalService.update(index, returnedDate)

    def search_menu(self):
        print('1. Books.')
        print('2. Clients.')
        choice = input('>')
        if choice == '1':
            print('1. By ID.')
            print('2. By Title.')
            print('3. By Author.')
            book_choice = input('>')
            if book_choice in ('1', '2', '3'):
                match = input('>')
                findings = self._BookService.search(book_choice, match)
                self.print_list(findings)
            else:
                raise UserError('Bad input!')
        elif choice == '2':
            print('1. By ID.')
            print('2. By name.')
            client_choice = input('>')
            if client_choice in ('1', '2'):
                match = input('>')
                findings = self._ClientService.search(client_choice, match)
                self.print_list(findings)
        else:
            raise UserError('Bad choice!')

    def statistics_menu(self):
        print('1. Most rented books.')
        print('2. Most active clients.')
        print('3. Most rented authors.')
        choice = input('>')
        if choice == '1':
            print(self._Service.most_rented_books())
        elif choice == '2':
            print(self._Service.most_active_clients())
        elif choice == '3':
            print(self._Service.most_rented_author())
        else:
            raise UserError('Bad choice!')

    def undo_menu(self):
        self._Service.undo()

    def redo_menu(self):
        self._Service.redo()

    @staticmethod
    def print_list(_list):
        for element in _list:
            print(element)

    def start(self):
        while True:
            self.print_menu()
            try:
                cmd = self.read_command()
                if cmd == '0':
                    return
                elif cmd == '1':
                    self.list_menu()
                elif cmd == '2':
                    self.add_menu()
                elif cmd == '3':
                    self.remove_menu()
                elif cmd == '4':
                    self.update_menu()
                elif cmd == '5':
                    self.rent_menu()
                elif cmd == '6':
                    self.return_menu()
                elif cmd == '7':
                    self.search_menu()
                elif cmd == '8':
                    self.statistics_menu()
                elif cmd == '9':
                    self.undo_menu()
                elif cmd == '10':
                    self.redo_menu()
                else:
                    raise UserError('Bad command!')
            except UserError as exception:
                print(exception.args[0])
            except DomainError as exception:
                print(exception.args[0])
            except ValueError as exception:
                print(exception.args[0])

