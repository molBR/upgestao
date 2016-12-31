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
