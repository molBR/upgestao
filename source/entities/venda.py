# encoding: utf-8

class Venda(object):
    def __init__(self, id, cliente, nome_contato, tipo_festa, num_adultos, num_criancas, endereco,  \
                 telefone, email, data_evento, data_insert, custo_local, custo_diversos, subtrair, valor_total):
        self.id = id
        self.cliente = cliente
        self.nome_contato = nome_contato
        self.tipo_festa = tipo_festa
        self.num_adultos = num_adultos
        self.num_criancas = num_criancas
        self.endereco = endereco
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

    def getCliente(self):
        return self.cliente

    def getTipo_festa(self):
        return self.tipo_festa

    def getNum_adultos(self):
        return self.num_adultos

    def getNum_criancas(self):
        return self.num_criancas

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

    def setId(self,id):
        self.id = id

    def setNome_contato(self,nome_contato):
        self.nome_contato = nome_contato

    def setCliente(self,Cliente):
        self.cliente = Cliente

    def setTipo_festa(self,tipo_festa):
        self.tipo_festa = tipo_festa

    def setNum_adultos(self,num_adultos):
        self.num_adultos = num_adultos

    def setNum_criancas(self,num_criancas):
        self.num_criancas = num_criancas

    def setEndereco_nome(self,endereco_nome):
        self.endereco_nome = endereco_nome

    def setTelefone(self,telefone):
        self.telefone = telefone

    def setEmail(self,email):
        self.email = email

    def setData_evento(self,data_evento):
        self.data_evento = data_evento

    def setData_insert(self,data_insert):
        self.data_insert = data_insert

    def setCusto_local(self,custo_local):
        self.custo_local = custo_local

    def setCusto_diversos(self,custo_diversos):
        self.custo_diversos = custo_diversos

    def setSubtrair(self,subtrair):
        self.subtrair = subtrair

    def setValor_total(self,valor_total):
        self.valor_total = valor_total