class Produto(object):
    def __init__(self):
        self.id = -1
        self.nome = "NULL"
        self.valor_inic = -1.0
        self.data_inser = -1
        self.foreign_key = -1

    def __init__(self, id, nome, valor_inic, data_inser,foreign_key):
        self.id = id
        self.nome = nome
        self.valor_inic = valor_inic
        self.data_inser = data_inser
        self.foreign_key = foreign_key

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getValor_inic(self):
        return self.valor_inic

    def getData_inser(self):
        return self.data_inser

    def getForeign_key(self):
        return self.foreign_key

    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setValor_inic(self, valor_inic):
        self.valor_inic = valor_inic

    def setData_inser(self, data_inser):
        self.data_inser = data_inser

    def setForeign_key(self,foreign_key):
        self.foreign_key = foreign_key


class Categoria(object):
    def __init__(self):
        self.id = -1
        self.nome = "NULL"
        self.data_inser = -1

    def __init__(self, id, nome, data_inser):
        self.id = id
        self.nome = nome
        self.data_inser = data_inser

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getData_inser(self):
        return self.data_inser

    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setData_inser(self, data_inser):
        self.data_inser = data_inser
