# encoding: utf-8

class Venda(object):
    def __init__(self, id, nome_cliente, nome_contato, tipo_festa, num_pessoas, endereco_nome, telefone, \
                    email, data_evento, data_insert, custo_local, custo_diversos, subtrair, valor_total):
        self.id = id
        self.nome_contato = nome_contato
        self.nome_cliente = nome_cliente
        self.tipo_festa = tipo_festa
        self.num_pessoas = num_pessoas
        self.endereco_nome = endereco_nome
        self.telefone = telefone
        self.email = email
        self.data_evento = data_evento
        self.data_insert = data_insert
        self.custo_local = custo_local
        self.custo_diversos = custo_diversos
        self.subtrair = subtrair
        self.valor_total = valor_total

    def getId(self):
        return self.id

    def getNome_contato(self):
        return self.nome_contato

    def getNome_cliente(self):
        return self.nome_cliente

    def getTipo_festa(self):
        return self.tipo_festa

    def getNum_pessoas(self):
        return self.num_pessoas

    def getEndereco_nome(self):
        return self.endereco_nome

    def getTelefone(self):
        return self.telefone

    def getEmail(self):
        return self.email

    def getData_evento(self):
        return self.data_evento

    def getData_insert(self):
        return self.data_insert

    def getCusto_local(self):
        return self.custo_local

    def getCusto_diversos(self):
        return self.custo_diversos

    def getSubtrair(self):
        return self.subtrair

    def getValor_total(self):
        return self.valor_total