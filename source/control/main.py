# encoding: utf-8

from Tkinter import *

from source.entities import database as db
from source.control import control as ctrl

from source.boundaries import cadastro_produto_maior as cadProdMaior
from source.boundaries import cadastro_clientes_maior as cadClientMaior
from source.boundaries import venda_produtos as vendProd
from source.boundaries import vendas_historico as vendHist
from source.boundaries import menu_inicial as menuInicial

def raw_backup():
    # Funcionalidade de backup
    bd = db.Database(0)
    bd.exportSQL()
    # bd.importSQL()
    bd.close()

"""                                                     Não está sendo usado no momento
#Classe de controle criada para fazer a comunicação entre as telas
class Control(Tkin.Tk):
    def __init__(self):
        #root = Tkin.Tk()

        #Menu(root)

        Tkin.Tk.__init__(self)
        container = Tkin.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        ###Frame stack
        self.frames["StartPage"] = StartPage(parent=container, controller=self)
        self.frames["PageOne"] = PageOne(parent=container, controller=self)
        self.frames["PageTwo"] = PageTwo(parent=container, controller=self)

        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageOne"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageTwo"].grid(row=0, column=0, sticky="nsew")
        ###

        self.show_frame("StartPage")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(Tkin.Frame):

    def __init__(self, parent, controller):
        Tkin.Frame.__init__(self, parent)
        self.controller = controller
        label = Tkin.Label(self, text="This is the start page")
        label.pack(side="top", fill="x", pady=10)

        button1 = Tkin.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = Tkin.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(Tkin.Frame):

    def __init__(self, parent, controller):
        Tkin.Frame.__init__(self, parent)
        self.controller = controller
        label = Tkin.Label(self, text="This is page 1")
        label.pack(side="top", fill="x", pady=10)
        button = Tkin.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(Tkin.Frame):

    def __init__(self, parent, controller):
        Tkin.Frame.__init__(self, parent)
        self.controller = controller
        label = Tkin.Label(self, text="This is page 2")
        label.pack(side="top", fill="x", pady=10)
        button = Tkin.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
"""

def main():
    print 'Gut\'s is running.'
    root = Tk()
                #Instância das classes que existirão durante execução
    #ctrl.Control.start(Control)
    objMenuInic = menuInicial.Menu()
    objControl = ctrl.Control()
    #objCadProdMaiorproduto = cadProdMaior.TelaMaior()
    #objcadClientMaior = cadClientMaior.TelaMaior()
    #objVendProd = vendProd.TelaMaior()
    #objVendHist = vendHist.TelaMaior()

    objControl.start(root)
    objMenuInic.FazTela(root)

    root.mainloop()

    raw_backup()    #Call da função que realiza backup no fim da execução do programa
#fim

if __name__ == "__main__":
    main()