# encoding: utf-8
#All your base are belong to us

import source.boundaries.cadastro_produto_maior as cadProdMaior
import source.boundaries.cadastro_clientes_maior as cadClientMaior
import source.boundaries.venda_produtos as vendProd
import source.boundaries.vendas_historico as vendHist
import source.boundaries.menu_inicial as menuInicial

import Tkinter as tk

class Control(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.tela = {}
        container = tk.Frame(self)

        #self.title('Guts\' Orçamento - Menu Principal')
        self.resizable(width=False, height=False)
        self.geometry('1120x600')
        self.protocol("WM_DELETE_WINDOW", lambda: quit())

        #self.tela["menuInicial"] = menuInicial.Menu(parent=container, controller=self)
        #self.tela["cadProdMaior"] = cadProdMaior.CadProd(parent=container, controller=self)
        #self.tela["cadClientMaior"] = cadClientMaior.CadClient(parent=container, controller=self)
        #self.tela["vendHist"] = vendHist.VendHist(parent=container, controller=self)
        self.tela["vendProd"] = vendProd.VendProd(parent=container, controller=self)

        #Não sei ao certo o que é essa configuração de grid
        #self.tela["menuInicial"].grid(row=0, column=0, sticky="nsew")
        # self.tela["cadProdMaior"].grid(row=0, column=0, sticky="nsew")
        # self.tela["cadClientMaior"].grid(row=0, column=0, sticky="nsew")
        # self.tela["vendHist"].grid(row=0, column=0, sticky="nsew")
        self.tela["vendProd"].grid(row=0, column=0, sticky="nsew")

        #self.show_frame("menuInicial")
        self.show_frame("vendProd")

    #Mostra a tela desejada, que é mandada por parametro
    def show_frame(self, page_name):
        frame = self.tela[page_name]
        frame.tkraise()

    """
    @staticmethod
    def Application(self, screen):

            self.screen = screen
            #for widget in self.root.winfo_children():
            #   widget.destroy()


            #while TRUE:
            if self.screen == 0:
                self.menuInic.FazTela(self.root, self)
            elif self.screen == 1:
                self.vendas.FazTela(self.root, self)
            elif self.screen == 2:
                self.clientes.FazTela(self.root, self)
            elif self.screen == 3:
                self.hist.FazTela(self.root, self)
            elif self.screen == 4:
                self.produto.FazTela(self.root, self)
            elif self.screen == 5:
                self.menuInic.FazTela(self.root, self)
            #self.root.update()
                # execução do tinker por .quit()

            return

    """

    """
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

    def CloseWindow():
        quit()
"""