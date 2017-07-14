# encoding: utf-8

import source.boundaries.cadastro_clientes_maior as cadClientMaior
import source.boundaries.venda_produtos as vendProd
import source.boundaries.vendas_evento as vendas_evento

"""
        Classe que coordenaas telas relacionadas ao processo de vendas: Cadastro de Clientes,
    Cadastro de Evento e Venda de Produto.
"""

class ProcessVend:
    def __init__(self, controller):
        self.tela = {}
        self.controller = controller

        self.tela["cadClientMaior"] = cadClientMaior.CadClient(parent=self.controller.container, controller=self)
        self.tela["cadClientMaior"].grid(row=0, column=0, sticky="nsew")
        self.tela["vendEvent"] = vendas_evento.VendEvent(parent=self.controller.container, controller=self,Cliente=self.tela["cadClientMaior"].getClienteSelec())
        self.tela["vendEvent"].grid(row=0, column=0, sticky="nsew")
        #self.tela["vendProd"] = vendProd.VendProd(parent=self.controller.container, controller=self,
        #                                          Cliente=self.tela["cadClientMaior"].getClienteSelec(),TipoEvento=self.tela["vendEvent"].getTipoEvento())
        self.tela["vendProd"] = vendProd.VendProd(parent=self.controller.container, controller=self,
                                                  Cliente=self.tela["cadClientMaior"].getClienteSelec(),
                                                  Venda=self.tela["vendEvent"].getTipoEvento())
        self.tela["vendProd"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("cadClientMaior")
        #self.show_frame("vendEvent")

    # Mostra a tela desejada, que é mandada por parametro
    def show_frame(self, page_name):
        if (page_name == 'cadClientMaior'):
            self.controller.title('Guts\' Orçamento - Cadastro de Clientes')
        elif (page_name == 'vendProd'):
            self.controller.title('Gut\'s Orçamento - Nova Venda')

        self.Setter()
        frame = self.tela[page_name]
        frame.tkraise()

    def Setter(self):
        self.tela["vendEvent"].setCliente(self.tela["cadClientMaior"].getClienteSelec())
        self.tela["vendProd"].setCE(self.tela["cadClientMaior"].getClienteSelec(),self.tela["vendEvent"].getTipoEvento())

    def terminate(self):
        self.tela = None
        self.controller.show_frame("menuInicial")