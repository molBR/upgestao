# encoding: utf-8

import Tkinter as tk
import os as os
from source.entities import database as db
import tkMessageBox
from source.entities import testefuzz as tf
from Docx import documentoShow as ds



# funcao de teste
def Teste():
    print("Testado")

class VendHist(tk.Frame):

    def __init__(self, parent, controller):
        try:
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.bd = db.Database()
            self.FazTela()
            self.ClienteSelec = self.bd.selectClienteId(self.bd.selectVenda()[0][1])
            self.VendaSelec = self.bd.selectVenda()[0]
            self.listaProdSelec = self.bd.selectProdVendIdVend(self.bd.selectVenda()[0][1])
        except:
            pass



    def visualiza(self,info,row):
        self.populate1(self.bd.selectVenda())
        self.ClienteSelec = self.bd.selectClienteId(info[1])
        self.VendaSelec = self.bd.selectVendaId(info[0])
        self.listaProdSelec = self.bd.selectProdVendIdVend(info[0])
        self.populate2(self.VendaSelec, self.ClienteSelec[0],
                       self.listaProdSelec)

    def pesquisando(self,pesquisa):
        if pesquisa == "" or self.pesquisar2.get() == " ":
            self.deleteCanvas(self.pacote1)
            self. deleteCanvas(self.pacote2)
            self.populate1(self.bd.selectVenda())
            try:
                self.populate2(self.bd.selectFirstVenda(), self.bd.selectClienteId(self.bd.selectFirstVenda()[1]),
                           self.bd.selectProdVendIdVend(self.bd.selectFirstVenda()[0]))
            except:
                pass

        else:
            self.deleteCanvas(self.pacote1)
            self.deleteCanvas(self.pacote2)
            self.populate1(tf.PassaHistFuzzy(self.bd.selectVenda(),self.pesquisar2.get()))
            self.populate2(self.bd.selectFirstVenda(), self.bd.selectClienteId(self.bd.selectFirstVenda()[1]),
                           self.bd.selectProdVendIdVend(self.bd.selectFirstVenda()[0]))

    def deletando(self,id):
        self.JanelaPequena(id)
        self.populate1(self.bd.selectVenda())
        try:
            self.populate2(self.bd.selectFirstVenda(), self.bd.selectClienteId(self.bd.selectFirstVenda()[1]),
                       self.bd.selectProdVendIdVend(self.bd.selectFirstVenda()[0]))  # fim frame venda
        except:
            pass


    def deleteCanvas(self,pacote):
        if pacote[0] != None:
            pacote[0].destroy()
            pacote[1].destroy()
            pacote[2].destroy()
            pacote[0] = None
        return

    def createCanvas(self,pacote):
        #Frame.__init__(self, self.root)
        pacote[0] = tk.Canvas(self, borderwidth=0, background="#ffffff")
        pacote[1] = tk.Frame(pacote[0], background="#ffffff")
        pacote[2] = tk.Scrollbar(self, orient="vertical", command=pacote[0].yview)
        pacote[0].configure(yscrollcommand=pacote[2].set)

        pacote[0].pack(side="left", fill="both", expand=True)
        pacote[2].pack(side="left", fill="y")
        pacote[0].create_window((4,4), window=pacote[1], anchor="nw",
                                tags=pacote[3])
        pacote[1].bind("<Configure>", pacote[4])


    def JanelaPequena(self,id):
        if tkMessageBox.askokcancel("Deletar","Deseja mesmo deletar?"):
            self.bd.deleteVenda(id)


    def FazTela(self):

            # menu principal
            toolbar1 = tk.Frame(self, bg="white")

            self.menu = tk.Button(toolbar1, text="   Menu Inicial ", bg="white", relief=tk.FLAT,
                               command=lambda: self.controller.show_frame("menuInicial"))
            self.menu["font"] = ("Arial", "10")
            self.menu.pack(side=tk.LEFT)
            self.espaco1 = tk.Label(toolbar1, text=" | ", bg="white")
            self.espaco1["font"] = ("Arial", "12")
            self.espaco1.pack(side=tk.LEFT)
            """
            self.novavenda = tk.Button(toolbar1, text="Nova Venda", bg="white", relief=tk.FLAT,
                               command=lambda: self.controller.show_frame("vendProd"))
            self.novavenda["font"] = ("Arial", "10")
            self.novavenda.pack(side=tk.LEFT, padx=1, pady=1)
            self.espaco2 = tk.Label(toolbar1, text=" | ", bg="white")
            self.espaco2["font"] = ("Arial", "12")
            self.espaco2.pack(side=tk.LEFT)
            """
            self.cadastrarcliente = tk.Button(toolbar1, text="Clientes e Vendas", bg="white", relief=tk.FLAT,
                               command=lambda: self.controller.show_frame("cadClientMaior"))
            self.cadastrarcliente["font"] = ("Arial", "10")
            self.cadastrarcliente.pack(side=tk.LEFT, padx=1, pady=1)
            self.espaco3 = tk.Label(toolbar1, text=" | ", bg="white")
            self.espaco3["font"] = ("Arial", "12")
            self.espaco3.pack(side=tk.LEFT)
            self.historicovenda = tk.Button(toolbar1, text="Historico de Vendas", bg="light grey", relief=tk.FLAT)
            self.historicovenda["font"] = ("Arial", "10")
            self.historicovenda.pack(side=tk.LEFT, padx=1, pady=1)
            self.espaco4 = tk.Label(toolbar1, text=" | ", bg="white")
            self.espaco4["font"] = ("Arial", "12")
            self.espaco4.pack(side=tk.LEFT)
            self.inserirproduto = tk.Button(toolbar1, text="Inserir Produto", bg="white", relief=tk.FLAT,
                               command=lambda: self.controller.show_frame("cadProdMaior"))
            self.inserirproduto["font"] = ("Arial", "10")
            self.inserirproduto.pack(side=tk.LEFT, padx=1, pady=1)
            """
            self.espaco5 = tk.Label(toolbar1, text=" | ", bg="white")
            self.espaco5["font"] = ("Arial", "12")
            self.espaco5.pack(side=tk.LEFT)

            self.inserirtipo = tk.Button(toolbar1, text="Inserir Tipo", bg="white", relief=tk.FLAT,
                               command=lambda: Teste())
            self.inserirtipo["font"] = ("Arial", "10")
            self.inserirtipo.pack(side=tk.LEFT, padx=1, pady=1)
            """
            toolbar1.pack(side=tk.TOP, fill=tk.X)
            # fim

            # barra de 'status'
            status = tk.Label(self, text="Estado: Executando", bg="white", bd=1, relief=tk.SUNKEN, anchor=tk.W)
            status.pack(side=tk.BOTTOM, fill=tk.X)
            # fim

            # abas de opcoes
            cor1 = '#D32F2F'
            q = "quantidades"
            info = 71

            toolbar = tk.Frame(self, bg=cor1)

            ordenar = tk.Label(toolbar, text=" Ordenar Por:", bg=cor1, font="bold", fg="white")
            ordenar.pack(side=tk.LEFT, pady=1)
            variable = tk.StringVar(toolbar)
            variable.set("Nome")
            opcoes = tk.OptionMenu(toolbar, variable, "Nome", "Data  ", "Valor ")
            opcoes.config(bg=cor1, font="white", fg="white")
            opcoes["menu"].config(bg=cor1, font="white", fg="white")
            opcoes.pack(side=tk.LEFT)
            for espaco in range(info):
                t = " "
                tk.Label(toolbar, text=t, bg=cor1).pack(side=tk.LEFT)
            vendas = tk.Label(toolbar, text="Vendas Realizadas:", bg=cor1, font="bold", fg="white")
            vendas.pack(side=tk.LEFT, pady=10)
            quantidade = tk.Label(toolbar, text=q, bg=cor1, font="bold", fg="white")
            quantidade.pack(side=tk.LEFT)

            toolbar.pack(side=tk.TOP, fill=tk.X)
            # fim


            cor3='#E6E6E6'

            self.container1 = tk.Frame(self)
            self.container2 = tk.Frame(self, bg=cor3)
            self.container3 = tk.Frame(self, bg=cor3)
            self.container4 = tk.Frame(self, bg=cor3)
            self.container1.pack(fill=tk.X)
            self.container2.pack(side=tk.BOTTOM, fill=tk.X)
            self.container3.pack(side=tk.BOTTOM, fill=tk.X)
            self.container4.pack(side=tk.BOTTOM, fill=tk.X)

            # "cabecalho" da tabela dos itens

            self.nome = tk.Label(self.container1, text=" Nome:")
            self.nome["font"] = ["bold"]
            self.nome.pack(side=tk.LEFT)
            self.pulo1 = tk.Label(self.container1, text="                                                 ")
            self.pulo1["font"] = ["bold"]
            self.pulo1.pack(side=tk.LEFT)
            self.data = tk.Label(self.container1, text="Data:")
            self.data["font"] = ["bold"]
            self.data.pack(side=tk.LEFT)
            self.pulo2 = tk.Label(self.container1, text="                  ")
            self.pulo2["font"] = ["bold"]
            self.pulo2.pack(side=tk.LEFT)
            self.valor = tk.Label(self.container1, text="Valor:")
            self.valor["font"] = ["bold"]
            self.valor.pack(side=tk.LEFT)
            self.pulo3 = tk.Label(self.container1, text="                                ")
            self.pulo3.pack(side=tk.LEFT)
            self.dados = tk.Label(self.container1, text="Dados Gerais:")
            self.dados["font"] = ["bold"]
            self.dados.pack(side=tk.LEFT)
            # fim

    # espaco com "salvar docx", "excluir" e "pesquisar"

            t = "VALOR"

            self.salto1 = tk.Label(self.container2, text="", bg=cor3)
            self.salto1.pack(side=tk.LEFT)

            self.espaco1 = tk.Label(self.container3, text="                                                                          ", bg=cor3)
            self.espaco1.pack(side=tk.LEFT)
            self.pesquisar1 = tk.Label(self.container3, text="Pesquisar: ", bg=cor3)
            self.pesquisar1["font"] = ['bold']
            self.pesquisar1.pack(side=tk.LEFT)
            self.pesquisar2 = tk.Entry(self.container3)
            self.pesquisar2["width"] = 25
            self.pesquisar2["font"] = ("Arial", "10")
            self.pesquisar2.pack(side=tk.LEFT)
            self.espaco2 = tk.Label(self.container3, text=" ", bg=cor3)
            self.espaco2.pack(side=tk.LEFT)
            self.ok = tk.Button(self.container3, text="Ok", command=lambda:self.pesquisando("1"), bg=cor3)
            self.ok["font"] = ['bold']
            self.ok['padx'] = 1
            self.ok['pady'] = 1
            self.ok.pack(side=tk.LEFT)
            self.espaco3 = tk.Label(self.container3, text="                    ", bg=cor3)
            self.espaco3.pack(side=tk.LEFT)
            self.salvar = tk.Button(self.container3, text="Salvar Docx", command=lambda:ds.docx(self.ClienteSelec[0],self.VendaSelec,self.listaProdSelec,2,2,2), bg=cor3)
            self.salvar["font"] = ['bold']
            self.salvar['padx'] = 1
            self.salvar['pady'] = 1
            self.salvar.pack(side=tk.LEFT)

            self.salto2 = tk.Label(self.container4, text="", bg=cor3)
            self.salto2.pack(side=tk.LEFT)
    # fim

    # tabela dos itens
            #tk.Frame.__init__(self, self.root)  # comeco frame dos produtos
            self.canvas1 = tk.Canvas(self, borderwidth=0, background="#ffffff")
            self.frame1 = tk.Frame(self.canvas1, background="#f0f0f0")
            self.vsb1 = tk.Scrollbar(self, orient="vertical", command=self.canvas1.yview)
            self.canvas1.configure(yscrollcommand=self.vsb1.set)

            self.canvas1.pack(side="left", fill="both", expand=True)
            self.vsb1.pack(side="left", fill="y")
            self.canvas1.create_window((4, 4), window=self.frame1, anchor="nw",
                                       tags="self.frame1")

            self.pacote1 = [self.canvas1, self.frame1, self.vsb1, "self.frame1", self.onFrameConfigure1]

            self.populate1(self.bd.selectVenda())  # fim frame dos produtos

            #tk.Frame.__init__(self, self.root)  # comeco frame venda
            self.canvas2 = tk.Canvas(self, borderwidth=0, background="#ffffff")
            self.frame2 = tk.Frame(self.canvas2, background="#f0f0f0")
            self.vsb2 = tk.Scrollbar(self, orient="vertical", command=self.canvas2.yview)
            self.canvas2.configure(yscrollcommand=self.vsb2.set)

            self.canvas2.pack(side="left", fill="both", expand=True)
            self.vsb2.pack(side="left", fill="y")
            self.canvas2.create_window((4, 4), window=self.frame2, anchor="nw",
                                       tags="self.frame2")

            self.frame2.bind("<Configure>", self.onFrameConfigure2)

            self.pacote2 = [self.canvas2, self.frame2, self.vsb2, "self.frame2", self.onFrameConfigure2]
            try: #GAMBIARRA MONSTRA
                self.populate2(self.bd.selectFirstVenda(),self.bd.selectClienteId(self.bd.selectFirstVenda()[1])[0],self.bd.selectProdVendIdVend(self.bd.selectFirstVenda()[0]))  # fim frame venda
            except TypeError:
                pass

    def populate1(self,info):  # comeco produtos
        #info = 40
        info_cliente = []

        self.deleteCanvas(self.pacote1)
        self.createCanvas(self.pacote1)
        try: #GAMBIARRA
            for i in range(self.bd.TamVenda()):
                info_cliente.append(self.bd.selectClientNameId(info[i][1]))
        except IndexError:
            pass
        photo1 = tk.PhotoImage(file= os.getcwd() + "/source/images/eye.gif")
        photo2 = tk.PhotoImage(file= os.getcwd() + "/source/images/x.gif")
        for row in range(len(info)):
            if row % 2 == 0:
                button1 = tk.Button(self.pacote1[1], width=20, height=20, image=photo1, relief=tk.FLAT, command= lambda row=row: self.visualiza(info[row],row))
                button1.grid(row=row, column=1)
                button1.image = photo1
            else:
                button1 = tk.Button(self.pacote1[1], width=20, height=20, image=photo1, relief=tk.FLAT, command=lambda row=row: self.visualiza(info[row],row))
                button1.grid(row=row, column=1)
                button1.image = photo1
        for row in range(len(info)):
            if row % 2 == 0:
                cor = '#ffffff'
                t = info_cliente[row]
                ent = tk.Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=20)
                ent["font"] = ("Arial", "13")
                var = tk.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
            else:
                cor = '#f0f0f0'
                t = info_cliente[row]
                ent = tk.Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=20)
                ent["font"] = ("Arial", "13")
                var = tk.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
        for row in range(len(info)):
            if row % 2 == 0:
                cor = '#ffffff'
                t = info[row][7]
                ent = tk.Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = tk.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=3)
            else:
                cor = '#f0f0f0'
                t = info[row][7]
                ent = tk.Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = tk.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=3)
        for row in range(len(info)):
            if row % 2 == 0:
                cor = '#ffffff'
                t = info[row][12]
                ent = tk.Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = tk.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=4)
            else:
                cor = '#f0f0f0'
                t = info[row][12]
                ent = tk.Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = tk.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=4)
        for row in range(len(info)):
            if row % 2 == 0:
                button2 = tk.Button(self.pacote1[1], width=20, height=20, image=photo2, relief=tk.FLAT, command=lambda row=row: self.deletando(info[row][0]))
                button2.grid(row=row, column=6)
                button2.image = photo2
            else:
                button2 = tk.Button(self.pacote1[1], width=20, height=20, image=photo2, relief=tk.FLAT, command=lambda row=row: self.deletando(info[row][0]))
                button2.grid(row=row, column=6)
                button2.image = photo2
                # fim produtos

    def onFrameConfigure1(self, event):  # comeco scroolbar frame1
        '''Reset the scroll region to encompass the inner frame'''
        self.pacote1[0].configure(scrollregion=self.pacote1[0].bbox("all"))  # fim scroolbar frame1

    def populate2(self,infoVenda,infoCliente,infoListaProduto):  # comeco venda

        print infoListaProduto
        self.deleteCanvas(self.pacote2)
        self.createCanvas(self.pacote2)

        x = 31 #var para deixar o espaco ao lado dos dados com a mesma cor de fundo
        cor = '#fafafa'
        nada = ""
        nome1var = "Nome:"
        try:
            nome2var = infoCliente[0][1]
        except:
            try:
                nome2var = infoCliente[1]
            except:
                pass
        else:
            infoCliente = infoCliente[0]
        endereco1var = "Endereco:"
        endereco2var =  infoCliente[3]
        email1var = "Email:"
        email2var = infoCliente[5]
        telefone1var = "Telefone:"
        telefone2var = infoCliente[4]
        festa1var = "Tipo de Festa:"
        festa2var = infoVenda[3]
        data1var = "Data:"
        data2var = infoVenda[7]
        npessoas1var = "Numero de Adultos:"
        npessoas2var = infoVenda[4]
        npessoasCrin1var = "Numero de Crianças"
        npessoasCrin2var = infoVenda[5] #nao inserido ainda
        local1var = "Espaco/Local:"
        local2var = infoVenda[6]
        produtosvar = "Produtos:"
        NOME = "Nome"
        QUANTIDADE = "Quant."
        VALOR = "Valor"
        docesvar = "Doces:"
        salgadosvar = "Salgados:"
        massasvar = "Massas:"
        bebidasvar = "Bebidas:"
        outrosvar = "Outros:"
        produtonome = "nome"
        produtoquant = "quant"
        produtovalor = "valor"
        total1var = "Valor Total:"
        total2var = infoVenda[12]

        #titulo
        nome1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nome1var)
        nome1.config(textvariable=var, relief='flat')
        nome1.grid(row=0, column=0)

        #preencher cor
        for row in range (x):
            espaco1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
            var = tk.StringVar()
            var.set(nada)
            espaco1.config(textvariable=var, relief='flat')
            espaco1.grid(row=row, column=1)

        #preencher cor
        for row in range(x):
            espaco2 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
            var = tk.StringVar()
            var.set(nada)
            espaco2.config(textvariable=var, relief='flat')
            espaco2.grid(row=row, column=2)

        #informacao
        nome2 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nome2var)
        nome2.config(textvariable=var, relief='flat')
        nome2.grid(row=1, column=0)

        #espaco
        salto1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto1.config(textvariable=var, relief='flat')
        salto1.grid(row=2, column=0)

        #titulo e informacao
        endereco1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(endereco1var)
        endereco1.config(textvariable=var, relief='flat')
        endereco1.grid(row=3, column=0)
        endereco2 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(endereco2var)
        endereco2.config(textvariable=var, relief='flat')
        endereco2.grid(row=4, column=0)

        #espaco
        salto2 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto2.config(textvariable=var, relief='flat')
        salto2.grid(row=5, column=0)

        #titulo e informacao
        data1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(data1var)
        data1.config(textvariable=var, relief='flat')
        data1.grid(row=6, column=0)
        data2 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(data2var)
        data2.config(textvariable=var, relief='flat')
        data2.grid(row=7, column=0)

        #espaco
        salto3 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto3.config(textvariable=var, relief='flat')
        salto3.grid(row=8, column=0)

        #titulo e informacao
        email1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(email1var)
        email1.config(textvariable=var, relief='flat')
        email1.grid(row=9, column=0)
        email2 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(email2var)
        email2.config(textvariable=var, relief='flat')
        email2.grid(row=10, column=0)

        #espaco
        salto4 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto4.config(textvariable=var, relief='flat')
        salto4.grid(row=11, column=0)

        #titulo e informacao
        telefone1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(telefone1var)
        telefone1.config(textvariable=var, relief='flat')
        telefone1.grid(row=12, column=0)
        telefone2 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(telefone2var)
        telefone2.config(textvariable=var, relief='flat')
        telefone2.grid(row=13, column=0)

        #espaco
        salto5 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto5.config(textvariable=var, relief='flat')
        salto5.grid(row=14, column=0)

        #espaco
        salto6 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto6.config(textvariable=var, relief='flat')
        salto6.grid(row=17, column=0)

        #titulo e informacao
        festa1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(festa1var)
        festa1.config(textvariable=var, relief='flat')
        festa1.grid(row=18, column=0)
        festa2 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(festa2var)
        festa2.config(textvariable=var, relief='flat')
        festa2.grid(row=19, column=0)

        #espaco
        salto7 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto7.config(textvariable=var, relief='flat')
        salto7.grid(row=20, column=0)

        #titulo e informacao
        npessoas1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(npessoas1var)
        npessoas1.config(textvariable=var, relief='flat')
        npessoas1.grid(row=21, column=0)
        npessoas2 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(npessoas2var)
        npessoas2.config(textvariable=var, relief='flat')
        npessoas2.grid(row=22, column=0)

        #espaco
        salto8 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto8.config(textvariable=var, relief='flat')
        salto8.grid(row=23, column=0)

        #titulo e informacao
        npessoasCrin1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(npessoasCrin1var)
        npessoasCrin1.config(textvariable=var, relief='flat')
        npessoasCrin1.grid(row=24, column=0)
        npessoasCrin2 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(npessoasCrin2var)
        npessoasCrin2.config(textvariable=var, relief='flat')
        npessoasCrin2.grid(row=25, column=0)

        #espaco
        salto9 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto9.config(textvariable=var, relief='flat')
        salto9.grid(row=26, column=0)

        #titulo e informacao
        local1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(local1var)
        local1.config(textvariable=var, relief='flat')
        local1.grid(row=27, column=0)
        local2 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(local2var)
        local2.config(textvariable=var, relief='flat')
        local2.grid(row=28, column=0)

        #espaco
        salto10 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto10.config(textvariable=var, relief='flat')
        salto10.grid(row=29, column=0)

        #titulo
        produtos = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(produtosvar)
        produtos.config(textvariable=var, relief='flat')
        produtos.grid(row=30, column=0)

        #titulo
        nome = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(NOME)
        nome.config(textvariable=var, relief='flat')
        nome.grid(row=31, column=0)
        quantidade = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(QUANTIDADE)
        quantidade.config(textvariable=var, relief='flat')
        quantidade.grid(row=31
                        , column=1)
        valor = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(VALOR)
        valor.config(textvariable=var, relief='flat')
        valor.grid(row=31, column=2)

        #espaco
        salto11 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto11.config(textvariable=var, relief='flat')
        salto11.grid(row=32, column=0)
        espaco3 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(nada)
        espaco3.config(textvariable=var, relief='flat')
        espaco3.grid(row=32, column=1)
        espaco4 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(nada)
        espaco4.config(textvariable=var, relief='flat')
        espaco4.grid(row=32, column=2)

        #exemplo de como vai ficar as informacoes 519/858
        doces = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(docesvar)
        doces.config(textvariable=var, relief='flat')
        doces.grid(row=33, column=0)

        espaco5 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(nada)
        espaco5.config(textvariable=var, relief='flat')
        espaco5.grid(row=33, column=1)

        espaco6 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(nada)
        espaco6.config(textvariable=var, relief='flat')
        espaco6.grid(row=33, column=2)


        contaLinha = 0
        for i in range(len(infoListaProduto)):
            if (infoListaProduto[i][5] == "1"):
                prodSel1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold",
                                 width=33)
                var = tk.StringVar()
                var.set(infoListaProduto[i][1])
                prodSel1.config(textvariable=var, relief='flat')
                prodSel1.grid(row=34+contaLinha, column=0)
                prodSelQuant1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black',
                                      font="bold", width=10)
                var = tk.StringVar()
                var.set(infoListaProduto[i][3])
                prodSelQuant1.config(textvariable=var, relief='flat')
                prodSelQuant1.grid(row=34+contaLinha, column=1)
                prodSelValor1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black',
                                      font="bold", width=12)
                var = tk.StringVar()
                var.set(infoListaProduto[i][2])
                prodSelValor1.config(textvariable=var, relief='flat')
                prodSelValor1.grid(row=34+contaLinha, column=2)
                contaLinha = contaLinha + 1
        contaLinha = contaLinha + 1

        salto12 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto12.config(textvariable=var, relief='flat')
        salto12.grid(row=34+contaLinha, column=0)

        espaco7 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(nada)
        espaco7.config(textvariable=var, relief='flat')
        espaco7.grid(row=34+contaLinha, column=1)

        espaco8 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(nada)
        espaco8.config(textvariable=var, relief='flat')
        espaco8.grid(row=34+contaLinha, column=2)

        contaLinha = contaLinha + 1

        salgados = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(salgadosvar)
        salgados.config(textvariable=var, relief='flat')
        salgados.grid(row=34+contaLinha, column=0)

        espaco9 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(nada)
        espaco9.config(textvariable=var, relief='flat')
        espaco9.grid(row=34+contaLinha, column=1)

        espaco10 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(nada)
        espaco10.config(textvariable=var, relief='flat')
        espaco10.grid(row=34+contaLinha, column=2)

        contaLinha = contaLinha + 1

        for i in range(len(infoListaProduto)):
            if (infoListaProduto[i][5] == "2"):
                prodSel1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold",
                                 width=33)
                var = tk.StringVar()
                var.set(infoListaProduto[i][1])
                prodSel1.config(textvariable=var, relief='flat')
                prodSel1.grid(row=34+contaLinha, column=0)
                prodSelQuant1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black',
                                      font="bold", width=10)
                var = tk.StringVar()
                var.set(infoListaProduto[i][3])
                prodSelQuant1.config(textvariable=var, relief='flat')
                prodSelQuant1.grid(row=34+contaLinha, column=1)
                prodSelValor1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black',
                                      font="bold", width=12)
                var = tk.StringVar()
                var.set(infoListaProduto[i][2])
                prodSelValor1.config(textvariable=var, relief='flat')
                prodSelValor1.grid(row=34+contaLinha, column=2)
                contaLinha = contaLinha + 1

        contaLinha = contaLinha + 1

        salto13 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto13.config(textvariable=var, relief='flat')
        salto13.grid(row=34+contaLinha, column=0)

        espaco11 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(nada)
        espaco11.config(textvariable=var, relief='flat')
        espaco11.grid(row=34+contaLinha, column=1)

        espaco12 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(nada)
        espaco12.config(textvariable=var, relief='flat')
        espaco12.grid(row=34+contaLinha, column=2)

        contaLinha = contaLinha + 1

        massas = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(massasvar)
        massas.config(textvariable=var, relief='flat')
        massas.grid(row=34+contaLinha, column=0)

        espaco13 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(nada)
        espaco13.config(textvariable=var, relief='flat')
        espaco13.grid(row=34+contaLinha, column=1)

        espaco14 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(nada)
        espaco14.config(textvariable=var, relief='flat')
        espaco14.grid(row=34+contaLinha, column=2)

        contaLinha = contaLinha + 1

        for i in range(len(infoListaProduto)):
            if (infoListaProduto[i][5] == "3"):
                prodSel1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold",
                                 width=33)
                var = tk.StringVar()
                var.set(infoListaProduto[i][1])
                prodSel1.config(textvariable=var, relief='flat')
                prodSel1.grid(row=34+contaLinha, column=0)
                prodSelQuant1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black',
                                      font="bold", width=10)
                var = tk.StringVar()
                var.set(infoListaProduto[i][3])
                prodSelQuant1.config(textvariable=var, relief='flat')
                prodSelQuant1.grid(row=34+contaLinha, column=1)
                prodSelValor1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black',
                                      font="bold", width=12)
                var = tk.StringVar()
                var.set(infoListaProduto[i][2])
                prodSelValor1.config(textvariable=var, relief='flat')
                prodSelValor1.grid(row=34+contaLinha, column=2)
                contaLinha = contaLinha + 1

        contaLinha = contaLinha + 1

        salto14 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto14.config(textvariable=var, relief='flat')
        salto14.grid(row=34+contaLinha, column=0)

        espaco15 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(nada)
        espaco15.config(textvariable=var, relief='flat')
        espaco15.grid(row=34+contaLinha, column=1)

        espaco16 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(nada)
        espaco16.config(textvariable=var, relief='flat')
        espaco16.grid(row=34+contaLinha, column=2)

        contaLinha = contaLinha + 1

        bebidas = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(bebidasvar)
        bebidas.config(textvariable=var, relief='flat')
        bebidas.grid(row=34+contaLinha, column=0)

        espaco17 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(nada)
        espaco17.config(textvariable=var, relief='flat')
        espaco17.grid(row=34+contaLinha, column=1)

        espaco18 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(nada)
        espaco18.config(textvariable=var, relief='flat')
        espaco18.grid(row=34+contaLinha, column=2)

        contaLinha = contaLinha + 1

        for i in range(len(infoListaProduto)):
            if (infoListaProduto[i][5] == "4"):
                prodSel1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold",
                                 width=33)
                var = tk.StringVar()
                var.set(infoListaProduto[i][1])
                prodSel1.config(textvariable=var, relief='flat')
                prodSel1.grid(row=34+contaLinha, column=0)
                prodSelQuant1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black',
                                      font="bold", width=10)
                var = tk.StringVar()
                var.set(infoListaProduto[i][3])
                prodSelQuant1.config(textvariable=var, relief='flat')
                prodSelQuant1.grid(row=34+contaLinha, column=1)
                prodSelValor1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black',
                                      font="bold", width=12)
                var = tk.StringVar()
                var.set(infoListaProduto[i][2])
                prodSelValor1.config(textvariable=var, relief='flat')
                prodSelValor1.grid(row=34+contaLinha, column=2)
                contaLinha = contaLinha + 1

        contaLinha = contaLinha + 1

        salto15 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto15.config(textvariable=var, relief='flat')
        salto15.grid(row=34+contaLinha, column=0)

        espaco19 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(nada)
        espaco19.config(textvariable=var, relief='flat')
        espaco19.grid(row=34+contaLinha, column=1)

        espaco20 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(nada)
        espaco20.config(textvariable=var, relief='flat')
        espaco20.grid(row=34+contaLinha, column=2)

        contaLinha = contaLinha + 1

        outros = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(outrosvar)
        outros.config(textvariable=var, relief='flat')
        outros.grid(row=34+contaLinha, column=0)

        espaco21 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(nada)
        espaco21.config(textvariable=var, relief='flat')
        espaco21.grid(row=34+contaLinha, column=1)

        espaco22 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(nada)
        espaco22.config(textvariable=var, relief='flat')
        espaco22.grid(row=34+contaLinha, column=2)

        contaLinha = contaLinha + 1

        for i in range(len(infoListaProduto)):
            if (infoListaProduto[i][5] == "5"):
                prodSel1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold",
                                 width=33)
                var = tk.StringVar()
                var.set(infoListaProduto[i][1])
                prodSel1.config(textvariable=var, relief='flat')
                prodSel1.grid(row=34+contaLinha, column=0)
                prodSelQuant1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black',
                                      font="bold", width=10)
                var = tk.StringVar()
                var.set(infoListaProduto[i][3])
                prodSelQuant1.config(textvariable=var, relief='flat')
                prodSelQuant1.grid(row=34+contaLinha, column=1)
                prodSelValor1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black',
                                      font="bold", width=12)
                var = tk.StringVar()
                var.set(infoListaProduto[i][2])
                prodSelValor1.config(textvariable=var, relief='flat')
                prodSelValor1.grid(row=34+contaLinha, column=2)
                contaLinha = contaLinha + 1

        contaLinha = contaLinha + 1

        salto16 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(nada)
        salto16.config(textvariable=var, relief='flat')
        salto16.grid(row=34+contaLinha, column=0)


        espaco23 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(nada)
        espaco23.config(textvariable=var, relief='flat')
        espaco23.grid(row=34+contaLinha, column=1)

        espaco24 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(nada)
        espaco24.config(textvariable=var, relief='flat')
        espaco24.grid(row=34+contaLinha, column=2)

        contaLinha = contaLinha + 1

        #titulo e informacao
        total1 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(total1var)
        total1.config(textvariable=var, relief='flat')
        total1.grid(row=34+contaLinha, column=0)

        contaLinha = contaLinha + 1

        total2 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = tk.StringVar()
        var.set(total2var)
        total2.config(textvariable=var, relief='flat')
        total2.grid(row=34+contaLinha, column=0)

        contaLinha = contaLinha + 1

        #preencher cor
        espaco25 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(nada)
        espaco25.config(textvariable=var, relief='flat')
        espaco25.grid(row=34+contaLinha, column=1)

        espaco26 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(nada)
        espaco26.config(textvariable=var, relief='flat')
        espaco26.grid(row=34+contaLinha, column=2)

        contaLinha = contaLinha + 1

        espaco27 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = tk.StringVar()
        var.set(nada)
        espaco27.config(textvariable=var, relief='flat')
        espaco27.grid(row=34+contaLinha, column=1)

        espaco28 = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = tk.StringVar()
        var.set(nada)
        espaco28.config(textvariable=var, relief='flat')
        espaco28.grid(row=34+contaLinha, column=2)

    def onFrameConfigure2(self, event):  # comeco scroolbar frame2
        '''Reset the scroll region to encompass the inner frame'''
        self.pacote2[0].configure(scrollregion=self.pacote2[0].bbox("all"))  # fim scroolbar frame2
# fim
