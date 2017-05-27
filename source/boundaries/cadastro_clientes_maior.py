# encoding: utf-8

import Tkinter as tk

import cadastro_clientes_menor as cadClientMenor
from source.entities import database as db


# funcao de teste
def Teste():
    print("Testado")
# fim

class CadClient(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.FazTela()

    def FazTela(self):

            # menu principal
            toolbar1 = tk.Frame(self, bg="white")
            menu = tk.Button(toolbar1, text="   Menu Inicial ", bg="white", relief=tk.FLAT,
                               command=lambda: self.controller.show_frame("menuInicial"))
            menu["font"] = ("Arial", "10")
            menu.pack(side=tk.LEFT)
            espaco1 = tk.Label(toolbar1, text=" | ", bg="white")
            espaco1["font"] = ("Arial", "12")
            espaco1.pack(side=tk.LEFT)
            novavenda = tk.Button(toolbar1, text="Nova Venda", bg="white", relief=tk.FLAT,
                          command=lambda: self.controller.show_frame("vendProd"))
            novavenda["font"] = ("Arial", "10")
            novavenda.pack(side=tk.LEFT, padx=1, pady=1)
            espaco2 = tk.Label(toolbar1, text=" | ", bg="white")
            espaco2["font"] = ("Arial", "12")
            espaco2.pack(side=tk.LEFT)
            cadastrarcliente = tk.Button(toolbar1, text="Cadastrar Cliente", bg="light grey", relief=tk.FLAT)
            cadastrarcliente["font"] = ("Arial", "10")
            cadastrarcliente.pack(side=tk.LEFT, padx=1, pady=1)
            espaco3 = tk.Label(toolbar1, text=" | ", bg="white")
            espaco3["font"] = ("Arial", "12")
            espaco3.pack(side=tk.LEFT)
            historicovenda = tk.Button(toolbar1, text="Historico de Vendas", bg="white", relief=tk.FLAT,
                          command=lambda: self.controller.show_frame("vendHist"))
            historicovenda["font"] = ("Arial", "10")
            historicovenda.pack(side=tk.LEFT, padx=1, pady=1)
            espaco4 = tk.Label(toolbar1, text=" | ", bg="white")
            espaco4["font"] = ("Arial", "12")
            espaco4.pack(side=tk.LEFT)
            inserirproduto = tk.Button(toolbar1, text="Inserir Produto", bg="white", relief=tk.FLAT,
                          command=lambda: self.controller.show_frame("cadProdMaior"))
            inserirproduto["font"] = ("Arial", "10")
            inserirproduto.pack(side=tk.LEFT, padx=1, pady=1)
            espaco5 = tk.Label(toolbar1, text=" | ", bg="white")
            espaco5["font"] = ("Arial", "12")
            espaco5.pack(side=tk.LEFT)
            inserirtipo = tk.Button(toolbar1, text="Inserir Tipo", bg="white", relief=tk.FLAT,
                          command=lambda: Teste())
            inserirtipo["font"] = ("Arial", "10")
            inserirtipo.pack(side=tk.LEFT, padx=1, pady=1)

            toolbar1.pack(side=tk.TOP, fill=tk.X)
            # fim

            # abas de opcoes
            cor1 = '#D32F2F'
            v = "valor"

            toolbar2 = tk.Frame(self, bg=cor1)

            clientes = tk.Label(toolbar2, text=" Clientes Cadastrados:", bg=cor1, font="bold", fg="white")
            clientes.pack(side=tk.LEFT, pady=10)
            valor = tk.Label(toolbar2, text=v, bg=cor1, font="bold", fg="white")
            valor.pack(side=tk.LEFT)

            toolbar2.pack(side=tk.TOP, fill=tk.X)
            # fim

            # barra de 'status'
            status = tk.Label(self, text="Estado: Rodando", bg="white", bd=1, relief=tk.SUNKEN, anchor=tk.W)
            status.pack(side=tk.BOTTOM, fill=tk.X)
            # fim

            self.bd = db.Database(0)  # banco de dados
            print self.bd.selectCliente()

            cor3 = '#E6E6E6'
            info = 53

            #Criação da classe de tela menor de cadastro de cliente
            clientMenor = cadClientMenor.clienteCadastro()


            self.container1 = tk.Frame(self)
            self.container2 = tk.Frame(self, bg=cor3)
            self.container3 = tk.Frame(self, bg=cor3)
            self.container4 = tk.Frame(self, bg=cor3)
            self.container1.pack(fill=tk.X)
            self.container2.pack(side=tk.BOTTOM, fill=tk.X)
            self.container3.pack(side=tk.BOTTOM, fill=tk.X)
            self.container4.pack(side=tk.BOTTOM, fill=tk.X)

            self.cliente = tk.Label(self.container1, text="Clientes:")
            self.cliente["font"] = ["bold"]
            self.cliente.pack(side=tk.LEFT)
            for espaco in range(info):
                t = " "
                tk.Label(self.container1, text=t).pack(side=tk.LEFT)
            self.dados = tk.Label(self.container1, text="Dados:")
            self.dados["font"] = ["bold"]
            self.dados.pack(side=tk.LEFT)

            # espaco com "salvar docx", "excluir" e "pesquisar"

            self.salto1 = tk.Label(self.container2, text="", bg=cor3)
            self.salto1.pack(side=tk.LEFT)

            self.espaco1 = tk.Label(self.container3, text="                                                          ",
                                 bg=cor3)
            self.espaco1.pack(side=tk.LEFT)
            self.cadastro = tk.Button(self.container3, text="Cadastrar", command=lambda: clientMenor.FazTela(self), bg=cor3)
            self.cadastro["font"] = ['bold']
            self.cadastro['padx'] = 1
            self.cadastro['pady'] = 1
            self.cadastro.pack(side=tk.LEFT)
            self.espaco2 = tk.Label(self.container3, text="                    ", bg=cor3)
            self.espaco2.pack(side=tk.LEFT)
            self.pesquisar1 = tk.Label(self.container3, text="Pesquisar: ", bg=cor3)
            self.pesquisar1["font"] = ['bold']
            self.pesquisar1.pack(side=tk.LEFT)
            self.pesquisar2 = tk.Entry(self.container3)
            self.pesquisar2["width"] = 40
            self.pesquisar2["font"] = ("Arial", "10")
            self.pesquisar2.pack(side=tk.LEFT)
            self.espaco3 = tk.Label(self.container3, text=" ", bg=cor3)
            self.espaco3.pack(side=tk.LEFT)
            self.ok = tk.Button(self.container3, text="Ok", command=Teste, bg=cor3)
            self.ok["font"] = ['bold']
            self.ok['padx'] = 1
            self.ok['pady'] = 1
            self.ok.pack(side=tk.LEFT)
            self.espaco4 = tk.Label(self.container3, text="                    ", bg=cor3)
            self.espaco4.pack(side=tk.LEFT)
            self.excluir = tk.Button(self.container3, text="Excluir", command=Teste, bg=cor3)
            self.excluir["font"] = ['bold']
            self.excluir['padx'] = 1
            self.excluir['pady'] = 1
            self.excluir.pack(side=tk.LEFT)

            self.salto2 = tk.Label(self.container4, text="", bg=cor3)
            self.salto2.pack(side=tk.LEFT)
            # fim

            # tabela dos itens
            #Frame.__init__(self, self.root)
            self.canvas1 = tk.Canvas(self, borderwidth=0, background="#ffffff")
            self.frame1 = tk.Frame(self.canvas1, background="#f0f0f0")
            self.vsb1 = tk.Scrollbar(self, orient="vertical", command=self.canvas1.yview)
            self.canvas1.configure(yscrollcommand=self.vsb1.set)

            self.canvas1.pack(side="left", fill="both", expand=True)
            self.vsb1.pack(side="left", fill="y")
            self.canvas1.create_window((4, 4), window=self.frame1, anchor="nw",
                                       tags="self.frame1")

            self.frame1.bind("<Configure>", self.onFrameConfigure1)

            self.populate1(self.bd.selectCliente())

            #Frame.__init__(self, self.root)
            self.canvas2 = tk.Canvas(self, borderwidth=0, background="#fafafa")
            self.frame2 = tk.Frame(self.canvas2, background="#fafafa")
            self.vsb2 = tk.Scrollbar(self, orient="vertical", command=self.canvas2.yview)
            self.canvas2.configure(yscrollcommand=self.vsb2.set)

            self.canvas2.pack(side="left", fill="both", expand=True)
            self.vsb2.pack(side="left", fill="y")
            self.canvas2.create_window((4, 4), window=self.frame2, anchor="nw",
                                       tags="self.frame2")

            self.frame2.bind("<Configure>", self.onFrameConfigure2)

            self.populate2(self.bd.selectCliente())

    def populate1(self,info):

        '''Put in some fake data'''
        for row in range(len(info)):
            if row % 2 == 0:
                cor = '#ffffff'
                var = tk.IntVar()
                c = tk.Checkbutton(self.frame1, variable=var, background=cor)
                c.grid(row=row, column=0)
            else:
                cor = '#f0f0f0'
                var = tk.IntVar()
                c = tk.Checkbutton(self.frame1, variable=var, background=cor)
                c.grid(row=row, column=0)
        for row in range(len(info)):
            if row % 2 == 0:
                cor = '#ffffff'
                t = info[row][1]
                ent = tk.Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', width=57)
                ent["font"] = ("Arial", "13")
                var = tk.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
            else:
                cor = '#f0f0f0'
                t = info[row][1]
                ent = tk.Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', width=57)
                ent["font"] = ("Arial", "13")
                var = tk.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)

    def onFrameConfigure1(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas1.configure(scrollregion=self.canvas1.bbox("all"))

    def populate2(self,info):
        cor = '#fafafa'
        nome = info[0][1]
        endereco = info[0][3]
        data = info[0][2]
        email = info[0][3]
        telefone = info[0][5]
        celular = info[0][5]

        salto1 = tk.Label(self.frame2, text="               ", bg=cor)
        salto1.grid(row=0, column=0)

        nome1 = tk.Label(self.frame2, text="Nome:", bg=cor)
        nome1['font'] = ['bold']
        nome1.grid(row=1, column=1, sticky=tk.W)
        nome2 = tk.Entry(self.frame2, text=nome, bg=cor)
        nome2["width"] = 58
        nome2["font"] = ['bold']
        var = tk.StringVar()
        var.set(nome)
        nome2.config(textvariable=var, relief='flat')
        nome2.grid(row=2, column=1)

        salto2 = tk.Label(self.frame2, text="", bg=cor)
        salto2.grid(row=3, column=0)

        endereco1 = tk.Label(self.frame2, text="Endereco:", bg=cor)
        endereco1['font'] = ['bold']
        endereco1.grid(row=4, column=1, sticky=tk.W)
        endereco2 = tk.Entry(self.frame2, text=nome, bg=cor)
        endereco2["width"] = 58
        endereco2["font"] = ['bold']
        var = tk.StringVar()
        var.set(endereco)
        endereco2.config(textvariable=var, relief='flat')
        endereco2.grid(row=5, column=1)

        salto3 = tk.Label(self.frame2, text="", bg=cor)
        salto3.grid(row=6, column=0)

        data1 = tk.Label(self.frame2, text="Data:", bg=cor)
        data1['font'] = ['bold']
        data1.grid(row=7, column=1, sticky=tk.W)
        data2 = tk.Entry(self.frame2, text=nome, bg=cor)
        data2["width"] = 58
        data2["font"] = ['bold']
        var = tk.StringVar()
        var.set(data)
        data2.config(textvariable=var, relief='flat')
        data2.grid(row=8, column=1)

        salto4 = tk.Label(self.frame2, text="", bg=cor)
        salto4.grid(row=9, column=0)

        email1 = tk.Label(self.frame2, text="Email:", bg=cor)
        email1['font'] = ['bold']
        email1.grid(row=10, column=1, sticky=tk.W)
        email2 = tk.Entry(self.frame2, text=nome, bg=cor)
        email2["width"] = 58
        email2["font"] = ['bold']
        var = tk.StringVar()
        var.set(email)
        email2.config(textvariable=var, relief='flat')
        email2.grid(row=11, column=1)

        salto5 = tk.Label(self.frame2, text="", bg=cor)
        salto5.grid(row=12, column=0)

        telefone1 = tk.Label(self.frame2, text="Telefone:", bg=cor)
        telefone1['font'] = ['bold']
        telefone1.grid(row=13, column=1, sticky=tk.W)
        telefone2 = tk.Entry(self.frame2, text=nome, bg=cor)
        telefone2["width"] = 58
        telefone2["font"] = ['bold']
        var = tk.StringVar()
        var.set(telefone)
        telefone2.config(textvariable=var, relief='flat')
        telefone2.grid(row=14, column=1)

        salto6 = tk.Label(self.frame2, text="", bg=cor)
        salto6.grid(row=15, column=0)

        celular1 = tk.Label(self.frame2, text="Celular:", bg=cor)
        celular1['font'] = ['bold']
        celular1.grid(row=16, column=1, sticky=tk.W)
        celular2 = tk.Entry(self.frame2, text=nome, bg=cor)
        celular2["width"] = 58
        celular2["font"] = ['bold']
        var = tk.StringVar()
        var.set(celular)
        celular2.config(textvariable=var, relief='flat')
        celular2.grid(row=17, column=1)

        salto7 = tk.Label(self.frame2, text="", bg=cor)
        salto7.grid(row=18, column=0)

    def onFrameConfigure2(self, event):  # comeco scroolbar frame2
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas2.configure(scrollregion=self.canvas2.bbox("all"))  # fim scroolbar frame2
# fim

