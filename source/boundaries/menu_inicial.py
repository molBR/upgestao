# encoding: utf-8

import Tkinter as tk
import os as os

#from source.control import control as ctrl

def Teste():
    print("Testado")

class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.FazTela()

    def FazTela(self):

        # barra de 'status'
        status = tk.Label(self, text="Estado: Executando", bg="white", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status.grid(row=1, column=0, sticky=tk.S + tk.W + tk.E, columnspan=2)
        # fim

        cor1 = '#ffffff'
        cor2 = '#d32f2f'

        # comeco titulo e imagem
        frame1 = tk.Frame(self, background=cor1)
        frame1.grid(row=0, column=0)

        salto1 = tk.Label(frame1, text="                ", bg=cor1)
        salto1.grid(row=0, column=0)

        salto2 = tk.Label(frame1, text="", bg=cor1)
        salto2.grid(row=1, column=0)

        titulo = tk.Label(frame1, text="Gut's Orçamento", bg=cor1, fg=cor2)
        titulo["font"] = ("Arial", "44", "bold")
        titulo.grid(row=2, column=1)

        salto3 = tk.Label(frame1, text="                ", bg=cor1)
        salto3.grid(row=3, column=2)

        self.photo = tk.PhotoImage(file=os.getcwd() + "\source\images\menu.gif")
        logo = tk.Label(frame1, image=self.photo, bg=cor1)
        logo.grid(row=4, column=1)

        salto4 = tk.Label(frame1, text="", bg=cor1)
        salto4.grid(row=5, column=0)
        # fim

        # comeco botoes
        frame2 = tk.Frame(self, background=cor1)
        frame2.grid(row=0, column=1)

        salto1 = tk.Label(frame2, text="                       ", bg=cor1)
        salto1.grid(row=0, column=0)
        salto2 = tk.Label(frame2, text="", bg=cor1)
        salto2.grid(row=1, column=0)
        salto3 = tk.Label(frame2, text="", bg=cor1)
        salto3.grid(row=2, column=0)
        salto4 = tk.Label(frame2, text="", bg=cor1)
        salto4.grid(row=3, column=0)
        salto5 = tk.Label(frame2, text="", bg=cor1)
        salto5.grid(row=4, column=0)
        salto6 = tk.Label(frame2, text="", bg=cor1)
        salto6.grid(row=5, column=0)
        salto7 = tk.Label(frame2, text="", bg=cor1)
        salto7.grid(row=6, column=0)

        venda = tk.Button(frame2, text="        Nova Venda        ", bg=cor2, fg=cor1, bd=2,
                          command=lambda: self.controller.show_frame("vendProd"))
        venda["font"] = ("Arial", "16", "bold")
        venda.grid(row=7, column=1, pady=5)

        salto8 = tk.Label(frame2, text="                       ", bg=cor1)
        salto8.grid(row=8, column=2)

        cadastro = tk.Button(frame2, text="    Cadastrar Cliente    ", bg=cor2, fg=cor1, bd=2,
                          command=lambda: self.controller.show_frame("cadClientMaior"))
        cadastro["font"] = ("Arial", "16", "bold")
        cadastro.grid(row=9, column=1, pady=5)

        salto9 = tk.Label(frame2, text="", bg=cor1)
        salto9.grid(row=10, column=1)

        historico = tk.Button(frame2, text="  Histórico de Vendas  ", bg=cor2, fg=cor1, bd=2,
                           command=lambda: self.controller.show_frame("vendHist"))
        historico["font"] = ("Arial", "16", "bold")
        historico.grid(row=11, column=1, pady=5)

        salto10 = tk.Label(frame2, text="", bg=cor1)
        salto10.grid(row=12, column=2)

        inserirproduto = tk.Button(frame2, text="      Inserir Produto      ", bg=cor2, fg=cor1, bd=2,
                         command=lambda: self.controller.show_frame("cadProdMaior"))
        inserirproduto["font"] = ("Arial", "16", "bold")
        inserirproduto.grid(row=13, column=1, pady=5)

        salto11 = tk.Label(frame2, text="", bg=cor1)
        salto11.grid(row=14, column=0)

        inserirtipo = tk.Button(frame2, text="         Inserir Tipo         ", bg=cor2, fg=cor1, bd=2,
                             command=lambda: Teste())
        inserirtipo["font"] = ("Arial", "16", "bold")
        inserirtipo.grid(row=15, column=1, pady=5)

        salto12 = tk.Label(frame2, text="", bg=cor1)
        salto12.grid(row=16, column=2)
        salto13 = tk.Label(frame2, text="", bg=cor1)
        salto13.grid(row=17, column=2)
        salto14 = tk.Label(frame2, text="", bg=cor1)
        salto14.grid(row=18, column=0)
        salto15 = tk.Label(frame2, text="", bg=cor1)
        salto15.grid(row=19, column=2)
        # fim

