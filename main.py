# encoding: utf-8

import database.backup as backupFile

#import cadastro_produto_maior


def main():
    #bd = Database()
    print 'Gut\'s is running.'

    #menu = TelaMaior()
        #Criacao do BD
    #bd.createDB()

        #Criacao de classes e sua insercao
    #cat1 = Categoria(1,'Salgados', 01122016) #[id, nome, data_inser]
    #bd.insertCategoria(cat1)
    #prod1 = Produto(4,'Empada', 5.0, 123123, 1, 'Salgados') #[id, nome, valor_inic, data_inser, id_Categoria, nome_Categoria]
    #bd.insertProduto(prod1)

    #texto = bd.selectProdutoId(4)
    #print texto

    backup = backupFile.Backup()
    backup.exportSQL()


if __name__ == "__main__":
    main()