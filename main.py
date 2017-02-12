# encoding: utf-8

import cadastro_produto_maior

import Tkinter as Tkin
import menu_inicial as menu_inicial
from database import database as db
import cadastro_produto_menor as cpm
from cadastro_produto_maior import TelaMaior
import tkMessageBox
import cadastro_produto_deletar as cpd
import cadastro_produto_editar_1 as cpe

def main():
    print 'Gut\'s is running.'

    root = Tkin.Tk()

### Tela do menu inicial
    app = menu_inicial.Menu(root)

### Tela de cadastro de produto
    # detalhes que o luquinha majna
#    TelaMaior(root).pack(side="top", fill="both", expand=True)

    # root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
#    root.title('Programa Guts')
#    root.resizable(width=False, height=True)
#    root.geometry('1061x581')
    # root.attributes("-fullscreen", True)
#    root.mainloop()
    # fim
###

    #Funcionalidade de backup
    bd = db.Database(0)
    bd.exportSQL()
    #bd.importSQL()
    bd.close()

if __name__ == "__main__":
    main()