from classes import *
from database import *

def main():

    bd = Database(1)
    bd.createDB()

    cat1 = Categoria(1,'Salgados',123123)
    prod1 = Produto(1,'Empada', '5,20', 123123,5)
    bd.insertCategoria(cat1)
    bd.insertProduto(prod1)
if __name__ == "__main__": main()
