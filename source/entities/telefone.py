# encoding: utf-8

class Telefone(object):
    def __init__(self, id, numero, id_cliente):
        self.id = id
        self.numero = numero
        self.id_cliente = id_cliente

    def getId(self):
        return self.id

    def getNumero(self):
        return self.numero

    def getId_cliente(self):
        return self.id_cliente