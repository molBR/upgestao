# encoding: utf-8

from Tkinter import *

import cadastro_produto_maior as cadProdMaior

import venda_produtos as vendProd
import vendas_historico as vendHist
from source.boundaries import cadastro_clientes_maior as cadClientMaior

from source.control import control as ctrl


class Menu(Frame):

    def __init__(self):
        Frame.__init__(self)            #Necessário? Parece correto

    def FazTela(self, root):
        produto = cadProdMaior.TelaMaior()
        clientes = cadClientMaior.TelaMaior()
        vendas = vendProd.TelaMaior()
        hist = vendHist.TelaMaior()

        ctrl.Control.start(root)

        # barra de 'status'
        status = Label(root, text="Estado: Executando", bg="white", bd=1, relief=SUNKEN, anchor=W)
        status.grid(row=1, column=0, sticky=S + W + E, columnspan=2)
        # fim

        cor1 = '#ffffff'
        cor2 = '#d32f2f'

        # comeco titulo e imagem
        frame1 = Frame(root, background=cor1)
        frame1.grid(row=0, column=0)

        salto1 = Label(frame1, text="                ", bg=cor1)
        salto1.grid(row=0, column=0)

        salto2 = Label(frame1, text="", bg=cor1)
        salto2.grid(row=1, column=0)

        titulo = Label(frame1, text="Guts' Orçamento", bg=cor1, fg=cor2)
        titulo["font"] = ("Arial", "44", "bold")
        titulo.grid(row=2, column=1)

        salto3 = Label(frame1, text="                ", bg=cor1)
        salto3.grid(row=3, column=2)


        ###
        #self.photo = PhotoImage(file="../../menu.gif")
        self.photo = PhotoImage(file="menu.gif")
        logo = Label(frame1, image=self.photo, bg=cor1)
        logo.grid(row=4, column=1)
        ###


        salto4 = Label(frame1, text="", bg=cor1)
        salto4.grid(row=5, column=0)
        # fim

        # comeco botoes
        frame2 = Frame(root, background=cor1)
        frame2.grid(row=0, column=1)

        salto1 = Label(frame2, text="                       ", bg=cor1)
        salto1.grid(row=0, column=0)
        salto2 = Label(frame2, text="", bg=cor1)
        salto2.grid(row=1, column=0)
        salto3 = Label(frame2, text="", bg=cor1)
        salto3.grid(row=2, column=0)
        salto4 = Label(frame2, text="", bg=cor1)
        salto4.grid(row=3, column=0)
        salto5 = Label(frame2, text="", bg=cor1)
        salto5.grid(row=4, column=0)
        salto6 = Label(frame2, text="", bg=cor1)
        salto6.grid(row=5, column=0)
        salto7 = Label(frame2, text="", bg=cor1)
        salto7.grid(row=6, column=0)

        venda = Button(frame2, text="        Nova Venda        ", bg=cor2, fg=cor1, bd=2,
                       command=lambda : ctrl.Control.ChamaTela(vendas, root))
        venda["font"] = ("Arial", "16", "bold")
        venda.grid(row=7, column=1, pady=5)

        salto8 = Label(frame2, text="                       ", bg=cor1)
        salto8.grid(row=8, column=2)

        cadastro = Button(frame2, text="    Cadastrar Cliente    ", bg=cor2, fg=cor1, bd=2,
                          command=lambda: ctrl.Control.ChamaTela(clientes, root))
        cadastro["font"] = ("Arial", "16", "bold")
        cadastro.grid(row=9, column=1, pady=5)

        salto9 = Label(frame2, text="", bg=cor1)
        salto9.grid(row=10, column=1)

        historico = Button(frame2, text="  Histórico de Vendas  ", bg=cor2, fg=cor1, bd=2,
                           command=lambda: ctrl.Control.ChamaTela(hist, root))
        historico["font"] = ("Arial", "16", "bold")
        historico.grid(row=11, column=1, pady=5)

        salto10 = Label(frame2, text="", bg=cor1)
        salto10.grid(row=12, column=2)

        inserirproduto = Button(frame2, text="      Inserir Produto      ", bg=cor2, fg=cor1, bd=2,
                         command=lambda: ctrl.Control.ChamaTela(produto, root))
        inserirproduto["font"] = ("Arial", "16", "bold")
        inserirproduto.grid(row=13, column=1, pady=5)

        salto11 = Label(frame2, text="", bg=cor1)
        salto11.grid(row=14, column=0)

        inserirtipo = Button(frame2, text="         Inserir Tipo         ", bg=cor2, fg=cor1, bd=2)
        inserirtipo["font"] = ("Arial", "16", "bold")
        inserirtipo.grid(row=15, column=1, pady=5)

        salto12 = Label(frame2, text="", bg=cor1)
        salto12.grid(row=16, column=2)
        salto13 = Label(frame2, text="", bg=cor1)
        salto13.grid(row=17, column=2)
        salto14 = Label(frame2, text="", bg=cor1)
        salto14.grid(row=18, column=0)
        salto15 = Label(frame2, text="", bg=cor1)
        salto15.grid(row=19, column=2)
        # fim
