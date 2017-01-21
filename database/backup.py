# encoding: utf-8

import database as db

class Backup:
    def __init__(self, fileName='dados.sql'):
        self.fileName = fileName

    #Método que salva os dados atuais do sistema em um arquivo com código SQL
    def exportSQL(self):
        stringDados = db.Database(0).selectProduto()
        print stringDados
        print len(stringDados)
        print stringDados[0]
        print stringDados[0][0]
        print stringDados[0][1]
        print stringDados[0][2]
        print stringDados[0][3]
        print stringDados[0][4]

        print stringDados[1]
        print stringDados[84]
        # db.insertProduto(prod1)

    #Método que insere dados ao sistema ao ler um arquivo com código SQL
    def insertSQL(self):
        pass

