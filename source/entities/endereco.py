# encoding: utf-8

class Endereco(object):
    def __init__(self, id, nome_local, nome_endereco, id_cliente):
        self.id = id
        self.nome_local = nome_local
        self.nome_endereco = nome_endereco
        self.id_cliente = id_cliente

    def getId(self):
        return self.id

    def getNome_local(self):
        return self.nome_local

    def getNome_endereco(self):
        return self.nome_endereco

    def getId_cliente(self):
        return self.id_cliente