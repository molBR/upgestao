# encoding: utf-8

import database as db

class Backup:
    def __init__(self, fileName='dados.sql'):
        self.fileName = fileName

    #Método que salva os dados atuais do sistema em um arquivo com código SQL
    def exportSQL(self):
        stringDados = db.Database(0).selectProduto()
        print stringDados
        # db.insertProduto(prod1)

    #Método que insere dados ao sistema ao ler um arquivo com código SQL
    def insertSQL(self):
        pass

