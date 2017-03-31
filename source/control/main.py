# encoding: utf-8

from Tkinter import *

from source.entities import database as db
from source.control import control as ctrl

from source.boundaries import cadastro_produto_maior as cadProdMaior
from source.boundaries import cadastro_clientes_maior as cadClientMaior
from source.boundaries import venda_produtos as vendProd
from source.boundaries import vendas_historico as vendHist
from source.boundaries import menu_inicial as menuInicial


# Funcionalidade de backup
def raw_backup():
    bd = db.Database(0)
    bd.exportSQL()
    # bd.importSQL()
    bd.close()


def main():
    print 'Gut\'s is running.'
    root = Tk()

    objMenuInic = menuInicial.Menu()

    objMenuInic.FazTela(root)

    root.mainloop()
                        #Depois que o loop for terminado pelo usuário é que termina a
    root.quit()         #execução do tinker por .quit()

    raw_backup()    #Call da função que realiza backup no fim da execução do programa
#fim

if __name__ == "__main__":
    main()