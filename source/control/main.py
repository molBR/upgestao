# encoding: utf-8

import Tkinter as tk
import os


os.chdir("C:\Users\Comedia\PycharmProjects\upgestao\ ")
print os.getcwd()

from source.entities import database as db
from source.control import control as ctrl

from source.boundaries import cadastro_produto_maior as cadProdMaior
from source.boundaries import cadastro_clientes_maior as cadClientMaior
from source.boundaries import venda_produtos as vendProd
from source.boundaries import vendas_historico as vendHist
from source.boundaries import menu_inicial as menuInicial
#from source.boundaries import menu_inicial as menuInicial


# Funcionalidade de backup
def raw_backup():
    bd = db.Database()
    bd.exportSQL()
    # bd.importSQL()
    bd.close()


def main():
    print "Gut\'s is running."


    #Insert cliente pra rodar
    #bd = db.Database(0)
    #bd.exportSQL()
    # bd.importSQL()
    #bd.close()
    #bd.dbCursor.execute("INSERT INTO Cliente VALUES (('0'), ('Carlos'), ('dia'), (''), (1));");
    #tables = ['''INSERT INTO Cliente VALUES ((), ('Faf'), ('20,00'), ('09:30:56'), (1));'''}


    control = ctrl.Control()
    control.mainloop()

    #control.Application(control, 0)

    #root.mainloop()

    # Depois que o loop for terminado pelo usuário é que termina a
    #root.quit()
    #objMenuInic = menuInicial.Menu()

    #objMenuInic.FazTela(root)


    raw_backup()    #Call da função que realiza backup no fim da execução do programa
#fim

if __name__ == "__main__":
    main()