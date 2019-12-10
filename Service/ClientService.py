from Repository.ClientRepository import *
import re

class ClientService:
    def __init__(self):
        self._repo = ClientRepository()

    def add(self, ID, name):
        client = Client(ID, name)
        self._repo.add(Client(ID, name))
        return client

    def display(self):
        return self._repo.getAll()

    def remove(self, clientId):
        for index, client in enumerate(self.display()):
            if client.clientId == clientId:
                self._repo.remove(index)
                return client

    def update(self, ID, name):
        ce = []
        for index, client in enumerate(self.display()):
            if client.clientId == ID:
                ce.append(client.clientId)
                ce.append(client.name)
                self._repo.update(index, name)
                return ce, [client.clientId, client.name]

    def search(self, choice, match):
        returnable = []
        match = '^' + match
        list_ = self.display()
        for client in list_:
            if choice == '1':
                if re.search(match, client.clientId, re.IGNORECASE):
                    returnable.append(client)
            if choice == '2':
                if re.search(match, client.name, re.IGNORECASE):
                    returnable.append(client)
        return returnable
