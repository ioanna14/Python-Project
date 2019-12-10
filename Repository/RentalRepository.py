from Domain import *


class RentalRepository:
    def __init__(self):
        self._data = [
            Rental('21', '1', '11', ['14', '1', '2018'], ['29', '5', '2019']),
            Rental('22', '2', '12', ['25', '7', '2016'], ['5', '10', '2018']),
            Rental('23', '3', '13', ['17', '10', '2015'], ['21', '3', '2017']),
            Rental('24', '1', '14', ['22', '6', '2018'], ['1', '10', '2019']),
            Rental('25', '5', '15', ['28', '3', '2016'], ['12', '11', '2017']),
            Rental('26', '9', '12', ['6', '1', '2017'], ['2', '12', '2017']),
            Rental('27', '3', '14', ['18', '9', '2018'], ['15', '3', '2019']),
            Rental('28', '7', '18', ['30', '5', '2014'], ['22', '4', '2016']),
            Rental('29', '9', '12', ['9', '8', '2018'], ['29', '10', '2018']),
            Rental('30', '1', '20', ['20', '11', '2017'], ['19', '8', '2019'])
        ]

    def add(self, rental):
        """
        Adds an element to the list.
        :param rental: the element we are adding tot the list
        """
        self._data.append(rental)

    def remove(self, index):
        """
        Removes an element from the list.
        :param index: the index of the element
        """
        self._data.pop(index)

    def update(self, index, returnedDate):
        """
        Sets the returned date.
        :param index: the index of the element we return
        :param returnedDate: the date of returns
        """
        self._data[index].returnedDate = returnedDate

    def getAll(self):
        """
        Returns the list of all the elements from the list.
        :return: the list of rentals
        """
        return self._data[:]
