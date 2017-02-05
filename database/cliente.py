# encoding: utf-8

class Cliente(object):
    def __init__(self, id, nome, data_insert, tem_endereco, tem_telefone, tem_email):
        self.id = id
        self.nome = nome
        self.data_insert = data_insert
        self.tem_endereco = tem_endereco
        self.tem_telefone = tem_telefone
        self.tem_email = tem_email

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getData_insert(self):
        return self.data_insert

    def getTem_endereco(self):
        return self.tem_endereco

    def getTem_telefone(self):
        return self.tem_telefone

    def getTem_email(self):
        return self.tem_email
