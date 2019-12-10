from Service.BookService import BookService
from Service.ClientService import ClientService
from UI import *

bookS = BookService()
clientS = ClientService()
rentalS = RentalService()
ui = UserInterface(bookS, clientS, rentalS)
ui.start()
