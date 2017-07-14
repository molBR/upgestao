# encoding: utf-8
#All your base are belong to us

import Tkinter as tk

import source.boundaries.cadastro_produto_maior as cadProdMaior
import source.boundaries.menu_inicial as menuInicial
import source.boundaries.processoVenda as procVenda
import source.boundaries.vendas_evento as vendas_evento
import source.boundaries.vendas_historico as vendHist

class Control(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.tela = {}
        self.processVendIsOn = False
        self.processVend  = None
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        #self.title('Guts\' Orçamento - Menu Principal')
        self.resizable(width=False, height=False)
        self.geometry('1500x600')
        self.protocol("WM_DELETE_WINDOW", lambda: quit())


        self.tela["menuInicial"] = menuInicial.Menu(parent=self.container, controller=self)
        self.tela["menuInicial"].grid(row=0, column=0, sticky="nsew")
        self.tela["cadProdMaior"] = cadProdMaior.CadProd(parent=self.container, controller=self)
        self.tela["cadProdMaior"].grid(row=0, column=0, sticky="nsew")
        #self.tela["cadClientMaior"] = cadClientMaior.CadClient(parent=self.container, controller=self)
        #self.tela["cadClientMaior"].grid(row=0, column=0, sticky="nsew")
        self.tela["vendHist"] = vendHist.VendHist(parent=self.container, controller=self)
        self.tela["vendHist"].grid(row=0, column=0, sticky="nsew")
        #self.tela["vendProd"] = vendProd.VendProd(parent=self.container, controller=self)
        #self.tela["vendProd"].grid(row=0, column=0, sticky="nsew")
        #self.tela["vendEvent"] = vendas_evento.VendEvent(parent=self.container, controller=self)
        #self.tela["vendEvent"].grid(row=0, column=0, sticky="nsew")

        #self.show_frame("vendProd")

        self.show_frame("menuInicial")
        #self.show_frame("vendEvent")

    #Mostra a tela desejada, que é mandada por parametro
    def show_frame(self, page_name):
        if(self.processVendIsOn):
            self.processVend = None
            self.processVendIsOn = False

        if(page_name == 'menuInicial'):
            self.title('Gut\'s Orçamento - Menu Inicial')
        elif (page_name == 'cadProdMaior'):
            self.title('Guts\' Orçamento - Cadastro de Produtos')
        elif(page_name == 'vendHist'):
            self.title('Guts\' Orçamento - Histórico de Vendas')
        #elif(page_name == 'vendProd'):
        #    self.title('Gut\'s Orçamento - Nova Venda')
        elif (page_name == 'cadClientMaior'):
            self.title('Guts\' Orçamento - Cadastro de Clientes')
            self.processVendIsOn = True
            self.processVend = procVenda.ProcessVend(controller=self)
            return
        frame = self.tela[page_name]
        frame.tkraise()
