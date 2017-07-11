# encoding: utf-8

from source.entities import database as db


class Cliente(object):
    def __init__(self,id, nome, data_insert, endereco, telefone, email):
        self.id = id
        self.nome = nome
        self.data_insert = data_insert
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    @staticmethod
    def selectClienteId(id, bd):
        auxInfo = bd.selectClienteId(id)
        auxClin = Cliente(auxInfo[0][0], auxInfo[0][1], auxInfo[0][2], auxInfo[0][3], auxInfo[0][4],auxInfo[0][5])
        return auxClin

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getData_insert(self):
        return self.data_insert

    def getEndereco(self):
        return self.endereco

    def getTelefone(self):
        return self.telefone

    def getEmail(self):
        return self.email

    #gambiarra
    def setId(self,id):
        self.id = id

