# coding=utf-8

from classes import *
from database import *
from cadastro_produto_maior import *

def main():
    bd = Database()
    print 'Gut\'s is running.'

        #Criacao do BD
    #bd.createDB()

        #Criacao de classes e sua insercao
    #cat1 = Categoria(1,'Salgados', 01122016) #[id, nome, data_inser]
    #bd.insertCategoria(cat1)
    #prod1 = Produto(4,'Empada', 5.0, 123123, 1, 'Salgados') #[id, nome, valor_inic, data_inser, id_Categoria, nome_Categoria]
    #bd.insertProduto(prod1)

    texto = bd.selectProdutoId(4)
    print texto

    #theBigProdMenu() #Chamada da janela grande

if __name__ == "__main__":
    main()