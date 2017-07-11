#encoding: utf-8

class tipoEvento(object):

    def __init__(self,id,tipo,rua,numero,bairro,complemento,adultos,criancas,data):
        self.id = id
        self.tipo = tipo
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.complemento = complemento
        self.adultos = adultos
        self.criancas = criancas
        self.data = data

    def getId(self):
        return self.id

    def getTipo(self):
        return self.tipo

    def getRua(self):
        return self.rua

    def getNumero(self):
        return self.numero

    def getBairro(self):
        return self.bairro

    def getComplemento(self):
        return self.complemento

    def getAdultos(self):
        return self.adultos

    def getCriancas(self):
        return self.criancas

    def getData(self):
        return self.data

    def setId(self,id):
        self.id = id

    def setTipo(self,tipo):
        return self.tipo

    def setRua(self,rua):
        self.rua = rua

    def setNumero(self,numero):
        self.numero = numero

    def setBairro(self,bairro):
        self.bairro = bairro

    def setComplemento(self,complemento):
        self.complemento = complemento

    def setAdultos(self,adultos):
        self.adultos = adultos

    def setCriancas(self,criancas):
        self.criancas = criancas

    def setData(self,data):
        self.data = data
