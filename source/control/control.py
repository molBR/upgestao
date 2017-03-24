# encoding: utf-8
#All your base are belong to us


from Tkinter import *
#import cadastro_produto_maior as cadProdMaior
#import cadastro_clientes_maior as cadClientMaior
#import venda_produtos as vendProd
#import vendas_historico as vendHist
#import menu_inicial as menuInicial

def Teste():
    print("Testado")


class Control():

    #def __init__(self):

    @staticmethod
    def start(root):
        #a = Menu(root)
        #self.produto = cadProdMaior.TelaMaior()
        #self.clientes = cadClientMaior.TelaMaior()
        #self.vendas = vendProd.TelaMaior()
        #self.hist = vendHist.TelaMaior()
        #self.menuInic = menuInicial.Menu()

        ###
        root = root
        menu = Menu(root)
        root.config(menu=menu)

        subMenu1 = Menu(menu)
        menu.add_cascade(label="Menu", menu=subMenu1)
        subMenu1.add_command(label="Recarregar", command=Teste)
        subMenu1.add_separator()
        subMenu1.add_command(label="Sair", command=root.destroy)

        subMenu2 = Menu(menu)
        menu.add_cascade(label="Arquivo", menu=subMenu2)
        subMenu2.add_command(label="Historico de Vendas", command=Teste)
        subMenu2.add_command(label="Clientes", command=Teste)
        subMenu2.add_command(label="Produtos", command=Teste)

        subMenu3 = Menu(menu)
        menu.add_cascade(label="...", menu=subMenu3)
        ###


        ###
        # root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
        root.title('Guts\' Orçamento - Menu Principal')
        root.resizable(width=False, height=False)
        root.geometry('1061x581')
        root.protocol("WM_DELETE_WINDOW", lambda: Control.CloseWindow(root))
        ###

        #def ChamaMenuInic(self):
        #    self.menuInic.FazTela(self.root)

    @staticmethod
    def ChamaTela(tela, root):
        tela.FazTela(root)

    @staticmethod
    def CloseWindow(root):
        root.destroy()
