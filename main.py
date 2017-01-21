# encoding: utf-8

import database.backup as backupFile

import cadastro_produto_maior


def main():
    print 'Gut\'s is running.'
    #bd = Database()

        #menu = TelaMaior()
    #Criacao do BD
        #bd.createDB()


    #Funcionalidade de criação de um arquivo sql para backup
    #"""
    backup = backupFile.Backup()
    backup.exportSQL()
    #"""

if __name__ == "__main__":
    main()