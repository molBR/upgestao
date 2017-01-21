# encoding: utf-8

import database as db

class Backup:
    #Pode ser mandado para o construtor o nome desejado para o arquivo sql, caso contrário o nome deste será dados.sql
    def __init__(self, fileName='dados.sql'):
        self.fileName = fileName

    #Método que salva os dados atuais do sistema em um arquivo com código SQL
    def exportSQL(self):
        bd = db.Database(0)
        dadosProduto = bd.selectProduto()

        file = open(self.fileName, 'w')
        ##Talvez escrever um cabeçalho no arquivo? Talvez?

        #Create table
        buffer = bd.tables[0] + "\n"+ bd.tables[1] + "\n\n"

        #Insert Produto
        sizeProduto = len(dadosProduto)
        for i in range(0, sizeProduto):
            buffer = buffer + 'INSERT INTO Produto VALUES ((' + str(dadosProduto[i][0]) + '), (' + dadosProduto[i][2] +\
                     '), (' + str(dadosProduto[i][3]) + '), (' + str(dadosProduto[i][4]) + '))' + '\n'
        buffer = buffer + '\n'

        ##Insert Categoria
        dadosCategoria = bd.selectCategoria()

        sizeCategoria = len(dadosCategoria)
        for i in range(0, sizeCategoria):
            buffer = buffer + 'INSERT INTO Categoria VALUES ((' + str(dadosCategoria[i][0]) + '), (' + dadosCategoria[i][1] + \
                     '), (' + str(dadosCategoria[i][2]) + '))' + '\n'
        buffer = buffer + '\n'

        #A escrita da string criada e o fechamento do arquivo
        file.write(buffer)
        file.close()

    #Método que insere dados ao sistema ao ler um arquivo com código SQL
    def insertSQL(self):
        pass

