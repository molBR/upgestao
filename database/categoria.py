# encoding: utf-8

class Categoria(object):
    def __init__(self):
        self.id = -1
        self.nome = "NULL"
        self.data_insert = -1

    def __init__(self, id, nome, data_insert):
        self.id = id
        self.nome = nome
        self.data_insert = data_insert

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getData_insert(self):
        return self.data_insert

    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setData_insert(self, data_insert):
        self.data_insert = data_insert
