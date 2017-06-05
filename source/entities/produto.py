# encoding: utf-8

from source.entities import database as db

class Produto(object):
    def __init__(self):
        self.id = -1
        self.nome = "NULL"
        self.valor_inic = -1.0
        self.data_insert = -1
        self.id_categoria = -1

    def __init__(self, id, nome, valor_inic, data_insert, id_categoria):
        self.id = id
        self.nome = nome
        self.valor_inic = valor_inic
        self.data_insert = data_insert
        self.id_categoria = id_categoria

    @staticmethod
    def selectProdId(id, bd):
        auxInfo = bd.selectProdutoId(id)
        auxProd = Produto(auxInfo[0], auxInfo[1], auxInfo[2], auxInfo[3], auxInfo[4])
        return auxProd

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getValor_inic(self):
        return self.valor_inic

    def getData_insert(self):
        return self.data_insert

    def getId_categoria(self):
        return self.id_categoria

    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setValor_inic(self, valor_inic):
        self.valor_inic = valor_inic

    def setData_insert(self, data_insert):
        self.data_insert = data_insert

    def setId_categoria(self, id_categoria):
        self.id_categoria = id_categoria