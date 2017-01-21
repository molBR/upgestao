# encoding: utf-8

import database.database as db

import cadastro_produto_maior

def main():
    print 'Gut\'s is running.'

    #menu = TelaMaior()


    #Funcionalidade de backup
    bd = db.Database(0)
    bd.exportSQL()
    #bd.importSQL()
    bd.close()

if __name__ == "__main__":
    main()