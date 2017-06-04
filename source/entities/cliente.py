# encoding: utf-8

class Cliente(object):
    def __init__(self, id, nome, data_insert, endereco, telefone, email):
        self.id = id
        self.nome = nome
        self.data_insert = data_insert
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

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
