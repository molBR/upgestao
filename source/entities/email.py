# encoding: utf-8

class Email(object):
    def __init__(self, id, email, id_cliente):
        self.id = id
        self.email = email
        self.id_cliente = id_cliente

    def getId(self):
        return self.id

    def getEmail(self):
        return self.email

    def getId_cliente(self):
        return self.id_cliente