# encoding: utf-8
#All your base are belong to us

#import cadastro_produto_maior as cadProdMaior
#import cadastro_clientes_maior as cadClientMaior
#import venda_produtos as vendProd
#import vendas_historico as vendHist
#import menu_inicial as menuInicial

from Tkinter import *

def Teste():
    print("Testado")


class Control():

    def __init__(self, root, produto, clientes, vendas, hist, menuInic):
        self.root = root
        self.produto = produto
        self.clientes = clientes
        self.vendas = vendas
        self.hist = hist
        self.menuInic = menuInic

    @staticmethod
    def Application(self, screen):
        for widget in self.root.winfo_children():
           widget.destroy()

        self.root.title('Guts\' Orçamento - Menu Principal')
        self.root.resizable(width=False, height=False)
        self.root.geometry('1120x600')
        self.root.protocol("WM_DELETE_WINDOW", lambda: Control.CloseWindow(self.root))


        if screen == 0:
            self.menuInic.FazTela(self.root, self)
        elif screen == 1:
            self.vendas.FazTela(self.root, self)
        elif screen == 2:
            self.clientes.FazTela(self.root, self)
        elif screen == 3:
            self.hist.FazTela(self.root, self)
        elif screen == 4:
            self.produto.FazTela(self.root, self)
        elif screen == 5:
            self.menuInic.FazTela(self.root, self)

    @staticmethod
    def start(root):
        #a = Menu(root)
        #self.produto = cadProdMaior.TelaMaior()
        #self.clientes = cadClientMaior.TelaMaior()
        #self.vendas = vendProd.TelaMaior()
        #self.hist = vendHist.TelaMaior()
        #self.menuInic = menuInicial.Menu()

        # root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
        '''
        root.title('Guts\' Orçamento - Menu Principal')
        root.resizable(width=False, height=False)
        root.geometry('1120x600')
        root.protocol("WM_DELETE_WINDOW", lambda: Control.CloseWindow(root))
        '''###

        #def ChamaMenuInic(self):
        #    self.menuInic.FazTela(self.root)

    @staticmethod
    def ChamaTela(tela, root):
        tela.FazTela(root)

    @staticmethod
    def CloseWindow(root):
        root.destroy()
