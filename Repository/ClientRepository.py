from Domain import *


class ClientRepository:
    def __init__(self):
        self._data = [
            Client('11', 'Arthur'),
            Client('12', 'Donna'),
            Client('13', 'Joanna'),
            Client('14', 'Tutti'),
            Client('15', 'Lissa'),
            Client('16', 'Louis'),
            Client('17', 'Michael'),
            Client('18', 'Rachel'),
            Client('19', 'Alicia'),
            Client('20', 'Mommy')
        ]

    def add(self, client):
        """
        Adds an element to the list.
        :param client: the element we are adding tot the list
        """
        self._data.append(client)

    def remove(self, index):
        """
        Removes an element from the list.
        :param index: the index of the element
        """
        self._data.pop(index)

    def update(self, index, name):
        """
        Sets the name of a client to a new one.
        :param index: the index of the client
        :param name: the name of the client
        """
        self._data[index].name = name

    def getAll(self):
        """
        Returns the list of all the elements from the list.
        :return: the list of clients
        """
        return self._data[:]
