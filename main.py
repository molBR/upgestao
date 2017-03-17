# encoding: utf-8

import Tkinter as Tkin
from menu_inicial import Menu
from database import database as db
#import cadastro_produto_menor as cpm
from cadastro_produto_maior import TelaMaior
#import tkMessageBox

def raw_backup():
    # Funcionalidade de backup
    bd = db.Database(0)
    bd.exportSQL()
    # bd.importSQL()
    bd.close()

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

def main():
    print 'Gut\'s is running.'

### Tela do menu inicial
    #root = Tkin.tk()
    app = Control()         #Magia ta rolando aqui

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

    raw_backup()    #Call da função que realiza backup no fim da execução do programa
#fim

if __name__ == "__main__":
    main()