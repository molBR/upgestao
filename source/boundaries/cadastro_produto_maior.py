# encoding: utf-8

import Tkinter as Tkin
import tkMessageBox

import cadastro_produto_deletar as cpd
import cadastro_produto_editar_1 as cpe
import cadastro_produto_menor as cpm
from source.entities import database as db
from source.entities import tratamentos as tr
from source.control import control as ctrl


class TelaMaior (Tkin.Frame):

#Botoes de selecao das categorias de produtos
    def todos_apertado(self):
        self.todos.config(relief=Tkin.SUNKEN, background=self.cor2)
        self.doces.config(relief=Tkin.RAISED, background=self.cor1)
        self.salgados.config(relief=Tkin.RAISED, background=self.cor1)
        self.massas.config(relief=Tkin.RAISED, background=self.cor1)
        self.bebidas.config(relief=Tkin.RAISED, background=self.cor1)
        self.outros.config(relief=Tkin.RAISED, background=self.cor1)
        self.populate(self.bd.selectProduto())

    def doces_apertado(self):
        self.todos.config(relief=Tkin.RAISED, background=self.cor1)
        self.doces.config(relief=Tkin.SUNKEN, background=self.cor2)
        self.salgados.config(relief=Tkin.RAISED, background=self.cor1)
        self.massas.config(relief=Tkin.RAISED, background=self.cor1)
        self.bebidas.config(relief=Tkin.RAISED, background=self.cor1)
        self.outros.config(relief=Tkin.RAISED, background=self.cor1)
        self.populate(self.bd.selectProdutoDoces())

    def salgados_apertado(self):
        self.todos.config(relief=Tkin.RAISED, background=self.cor1)
        self.doces.config(relief=Tkin.RAISED, background=self.cor1)
        self.salgados.config(relief=Tkin.SUNKEN, background=self.cor2)
        self.massas.config(relief=Tkin.RAISED, background=self.cor1)
        self.bebidas.config(relief=Tkin.RAISED, background=self.cor1)
        self.outros.config(relief=Tkin.RAISED, background=self.cor1)
        self.populate(self.bd.selectProdutoSalgados())

    def massas_apertado(self):
        self.todos.config(relief=Tkin.RAISED, background=self.cor1)
        self.doces.config(relief=Tkin.RAISED, background=self.cor1)
        self.salgados.config(relief=Tkin.RAISED, background=self.cor1)
        self.massas.config(relief=Tkin.SUNKEN, background=self.cor2)
        self.bebidas.config(relief=Tkin.RAISED, background=self.cor1)
        self.outros.config(relief=Tkin.RAISED, background=self.cor1)
        self.populate(self.bd.selectProdutoMassas())

    def bebidas_apertado(self):
        self.todos.config(relief=Tkin.RAISED, background=self.cor1)
        self.doces.config(relief=Tkin.RAISED, background=self.cor1)
        self.salgados.config(relief=Tkin.RAISED, background=self.cor1)
        self.massas.config(relief=Tkin.RAISED, background=self.cor1)
        self.bebidas.config(relief=Tkin.SUNKEN, background=self.cor2)
        self.outros.config(relief=Tkin.RAISED, background=self.cor1)
        self.populate(self.bd.selectProdutoBebidas())

    def outros_apertado(self):
        self.todos.config(relief=Tkin.RAISED, background=self.cor1)
        self.doces.config(relief=Tkin.RAISED, background=self.cor1)
        self.salgados.config(relief=Tkin.RAISED, background=self.cor1)
        self.massas.config(relief=Tkin.RAISED, background=self.cor1)
        self.bebidas.config(relief=Tkin.RAISED, background=self.cor1)
        self.outros.config(relief=Tkin.SUNKEN, background=self.cor2)
        self.populate(self.bd.selectProdutoOutros())
    # fim

#Destrutor para fechar o banco de dados
    #def __del__(self):
        #self.bd.close() //Estava fechando o bd de TelaMaior mesmo que nâo tenha aberto essa janela e por consequencia não tenha aberto bd

#Construtor
    def __init__(self):
        self.root = None

    def FazTela(self, root):
            self.root = root
            for widget in self.root.winfo_children():
                widget.destroy()
            ctrl.Control.start(self.root)

            self.root.title('Guts\' Orçamento - Cadastro de Produtos')

            ###
            self.toolbar1 = Tkin.Frame(self.root, bg="white")

            self.menu = Tkin.Label(self.toolbar1, text="   MENU ", bg="white")
            self.menu["font"] = ("Arial", "10")
            self.menu.pack(side=Tkin.LEFT)
            self.espaco1 = Tkin.Label(self.toolbar1, text=" | ", bg="white")
            self.espaco1["font"] = ("Arial", "12")
            self.espaco1.pack(side=Tkin.LEFT)
            self.novavenda = Tkin.Button(self.toolbar1, text="Nova Venda", bg="white", relief=Tkin.FLAT)
            self.novavenda["font"] = ("Arial", "10")
            self.novavenda.pack(side=Tkin.LEFT, padx=1, pady=1)
            self.espaco2 = Tkin.Label(self.toolbar1, text=" | ", bg="white")
            self.espaco2["font"] = ("Arial", "12")
            self.espaco2.pack(side=Tkin.LEFT)
            self.cadastrarcliente = Tkin.Button(self.toolbar1, text="Cadastrar Cliente", bg="white", relief=Tkin.FLAT)
            self.cadastrarcliente["font"] = ("Arial", "10")
            self.cadastrarcliente.pack(side=Tkin.LEFT, padx=1, pady=1)
            self.espaco3 = Tkin.Label(self.toolbar1, text=" | ", bg="white")
            self.espaco3["font"] = ("Arial", "12")
            self.espaco3.pack(side=Tkin.LEFT)
            self.historicovenda = Tkin.Button(self.toolbar1, text="Historico de Vendas", bg="white", relief=Tkin.FLAT)
            self.historicovenda["font"] = ("Arial", "10")
            self.historicovenda.pack(side=Tkin.LEFT, padx=1, pady=1)
            self.espaco4 = Tkin.Label(self.toolbar1, text=" | ", bg="white")
            self.espaco4["font"] = ("Arial", "12")
            self.espaco4.pack(side=Tkin.LEFT)
            self.inserirproduto = Tkin.Button(self.toolbar1, text="Inserir Produto", bg="light grey", relief=Tkin.FLAT)
            self.inserirproduto["font"] = ("Arial", "10")
            self.inserirproduto.pack(side=Tkin.LEFT, padx=1, pady=1)
            self.espaco5 = Tkin.Label(self.toolbar1, text=" | ", bg="white")
            self.espaco5["font"] = ("Arial", "12")
            self.espaco5.pack(side=Tkin.LEFT)
            self.inserirtipo = Tkin.Button(self.toolbar1, text="Inserir Tipo", bg="white", relief=Tkin.FLAT)
            self.inserirtipo["font"] = ("Arial", "10")
            self.inserirtipo.pack(side=Tkin.LEFT, padx=1, pady=1)

            self.toolbar1.pack(side=Tkin.TOP, fill=Tkin.X)
            # fim

            # barra de 'status'
            status = Tkin.Label(self.root, text="Estado: Rodando", bg="white", bd=1, relief=Tkin.SUNKEN, anchor=Tkin.W)
            status.pack(side=Tkin.BOTTOM, fill=Tkin.X)
            #

            self.bd = db.Database(0)  # banco de dados
            self.tm = cpm.TelaMenor()  # inserir
            self.td = cpd.TelaMenorDel()  # deletar
            self.te = cpe.TelaMenorEdit1()  # editar

            self.cor1 = '#D32F2F'
            self.cor2 = '#E94545'
            self.cor3 = '#E6E6E6'

            self.toolbar2 = Tkin.Frame(self.root, bg=self.cor1)

            self.todos = Tkin.Button(self.toolbar2, text="   Todos   ", bg=self.cor1, command=self.todos_apertado)
            self.todos['font'] = ('bold')
            self.todos['fg'] = 'white'
            self.todos.pack(side=Tkin.LEFT, padx=1, pady=6)
            self.doces = Tkin.Button(self.toolbar2, text="   Doces   ", bg=self.cor1, command=self.doces_apertado)
            self.doces['font'] = ('bold')
            self.doces['fg'] = 'white'
            self.doces.pack(side=Tkin.LEFT, padx=1, pady=6)
            self.salgados = Tkin.Button(self.toolbar2, text="Salgados", bg=self.cor1, command=self.salgados_apertado)
            self.salgados['font'] = ('bold')
            self.salgados['fg'] = 'white'
            self.salgados.pack(side=Tkin.LEFT, padx=1, pady=6)
            self.massas = Tkin.Button(self.toolbar2, text="  Massas  ", bg=self.cor1, command=self.massas_apertado)
            self.massas['font'] = ('bold')
            self.massas['fg'] = 'white'
            self.massas.pack(side=Tkin.LEFT, padx=1, pady=6)
            self.bebidas = Tkin.Button(self.toolbar2, text=" Bebidas ", bg=self.cor1, command=self.bebidas_apertado)
            self.bebidas['font'] = ('bold')
            self.bebidas['fg'] = 'white'
            self.bebidas.pack(side=Tkin.LEFT, padx=1, pady=6)
            self.outros = Tkin.Button(self.toolbar2, text="   Outros   ", bg=self.cor1, command=self.outros_apertado)
            self.outros['font'] = ('bold')
            self.outros['fg'] = 'white'
            self.outros.pack(side=Tkin.LEFT, padx=1, pady=6)

            self.toolbar2.pack(side=Tkin.TOP, fill=Tkin.X)

            self.container1 = Tkin.Frame(self.root)
            self.container2 = Tkin.Frame(self.root, bg=self.cor3)
            self.container3 = Tkin.Frame(self.root, bg=self.cor3)
            self.container4 = Tkin.Frame(self.root, bg=self.cor3)
            self.container1.pack(fill=Tkin.X)
            self.container2.pack(side=Tkin.BOTTOM, fill=Tkin.X)
            self.container3.pack(side=Tkin.BOTTOM, fill=Tkin.X)
            self.container4.pack(side=Tkin.BOTTOM, fill=Tkin.X)

            self.objeto1 = Tkin.Label(self.container1, text="Codigo:")
            self.objeto1["font"] = ["bold"]
            self.objeto1.pack(side=Tkin.LEFT)
            self.objeto2 = Tkin.Label(self.container1, text="                                                 ")
            self.objeto2["font"] = ["bold"]
            self.objeto2.pack(side=Tkin.LEFT)
            self.objeto3 = Tkin.Label(self.container1, text="Nome:")
            self.objeto3["font"] = ["bold"]
            self.objeto3.pack(side=Tkin.LEFT)
            self.objeto4 = Tkin.Label(self.container1,
                                      text="                                                                                                                 ")
            self.objeto4["font"] = ["bold"]
            self.objeto4.pack(side=Tkin.LEFT)
            self.objeto5 = Tkin.Label(self.container1, text="Valor:")
            self.objeto5["font"] = ["bold"]
            self.objeto5.pack(side=Tkin.LEFT)
            self.objeto6 = Tkin.Label(self.container1, text="                                              ")
            self.objeto6["font"] = ["bold"]
            self.objeto6.pack(side=Tkin.LEFT)
            # fim

            # espaco com "inserir", "editar", "excluir" e "pesquisar"

            self.salto1 = Tkin.Label(self.container2, text="", bg=self.cor3)
            self.salto1.pack(side=Tkin.LEFT)

            self.espaco1 = Tkin.Label(self.container3, text="                                                               ",
                                      bg=self.cor3)
            self.espaco1.pack(side=Tkin.LEFT)
            self.inserir = Tkin.Button(self.container3, text="Inserir", command=lambda: self.inserindo(self.bd), bg=self.cor3)
            self.inserir["font"] = ['bold']
            self.inserir['padx'] = 1
            self.inserir['pady'] = 1
            self.inserir.pack(side=Tkin.LEFT)
            self.espaco2 = Tkin.Label(self.container3, text="                    ", bg=self.cor3)
            self.espaco2.pack(side=Tkin.LEFT)
            self.editar = Tkin.Button(self.container3, text="Editar", command=lambda: self.editando(self.bd), bg=self.cor3)
            self.editar["font"] = ['bold']
            self.editar['padx'] = 1
            self.editar['pady'] = 1
            self.editar.pack(side=Tkin.LEFT)
            self.espaco2 = Tkin.Label(self.container3, text="                    ", bg=self.cor3)
            self.espaco2.pack(side=Tkin.LEFT)
            self.excluir = Tkin.Button(self.container3, text="Excluir", command=lambda: self.deletando(self.bd), bg=self.cor3)
            self.excluir["font"] = ['bold']
            self.excluir['padx'] = 1
            self.excluir['pady'] = 1
            self.excluir.pack(side=Tkin.LEFT)
            self.espaco3 = Tkin.Label(self.container3, text="                    ", bg=self.cor3)
            self.espaco3.pack(side=Tkin.LEFT)
            self.pesquisar1 = Tkin.Label(self.container3, text="Pesquisar: ", bg=self.cor3)
            self.pesquisar1["font"] = ['bold']
            self.pesquisar1.pack(side=Tkin.LEFT)
            self.pesquisar2 = Tkin.Entry(self.container3)
            self.pesquisar2["width"] = 25
            self.pesquisar2["font"] = ("Arial", "10")
            self.pesquisar2.pack(side=Tkin.LEFT)
            pesquisado = self.pesquisar2.get()  # pesquisado = o que foi escrito no "Entry / barra de pesquisa"
            self.espaco4 = Tkin.Label(self.container3, text=" ", bg=self.cor3)
            self.espaco4.pack(side=Tkin.LEFT)
            self.ok = Tkin.Button(self.container3, text="Ok", command=lambda: self.pesquisando(self.pesquisar2.get()), bg=self.cor3)
            self.ok["font"] = ['bold']
            self.ok['padx'] = 1
            self.ok['pady'] = 1
            self.ok.pack(side=Tkin.LEFT)

            self.salto2 = Tkin.Label(self.container4, text="", bg=self.cor3)
            self.salto2.pack(side=Tkin.LEFT)
            # fim
            self.canvas = None
            # tabela dos itens
            self.todos_apertado()



#funcao que cria o canvas, deve ser chamada toda vez que o mesmo e atualizado
    def createCanvas(self):
        Tkin.Frame.__init__(self, self.root)
        self.canvas = Tkin.Canvas(self.root, borderwidth=0, background="#ffffff")
        self.frame = Tkin.Frame(self.canvas, background="#f0f0f0")
        self.vsb = Tkin.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw", tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)
#fim

#Funcao que deleta o canvas, sempre uti
# izado para atualiza-lo
    def deleteCanvas(self):
        if self.canvas != None:
            self.canvas.destroy()
            self.vsb.destroy()
            self.canvas = None
        return
#fim

#Funcao chamada sempre que o botao inserir e apertado
    def inserindo(self,bd):
        self.tm.FazTela(bd)
        if(self.tm.GetWindow()!=None):
            self.tm.GetWindow().wait_window()
        self.populate(bd.selectProduto())
#fim

#Funcao chamada sempre que o botao editar eh apertado
    def editando(self, bd):
        self.te.FazTela(bd)
        if(self.te.GetWindow()!=None):
            self.te.GetWindow().wait_window()
        self.populate(bd.selectProduto())
#fim

#Funcao chamada sempre que o botao deletar eh apertado
    def deletando(self, bd):
        self.td.FazTela(bd)
        if (self.td.GetWindow() != None):
            self.td.GetWindow().wait_window()
        self.populate(bd.selectProduto())
#

#Funcao chamada sempre que o botao pesquisar eh apertado
    def pesquisando(self,id):
        if id == "":
            self.populate(self.bd.selectProduto())
            return
        else:
            try:
                tr.VerificaDigit(id)
            except Exception as e:
                tkMessageBox.showerror("Erro encontrado", e.message)
            else:
                self.todos_apertado()
                self.populate(self.bd.selectProdutoIdAll(id))

#Funcao que popula o canvas de dados, ele recebe por parametro os dados e formata-o
    def populate(self,info):
        '''Put in some fake data'''
        cor1 = '#ffffff'
        cor2 = '#f0f0f0'
        self.deleteCanvas()
        self.createCanvas()

        for row in range(len(info)):
            if row % 2 == 0:
                var = Tkin.IntVar()
                c = Tkin.Checkbutton(self.frame, variable=var, background=cor1)
                c.grid(row=row, column=0)
            else:
                var = Tkin.IntVar()
                c = Tkin.Checkbutton(self.frame, variable=var, background=cor2)
                c.grid(row=row, column=0)
        for row in range(len(info)):
            if row % 2 == 0:
                t=info[row][0]
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor1, fg='black', width=29)
                ent["font"] = ("Arial", "13")
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
            else:
                t=info[row][0]
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor2, fg='black', width=29)
                ent["font"] = ("Arial", "13")
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
        for row in range(len(info)):
            if row % 2 == 0:
                t=info[row][1]
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor1, fg='black', width=56)
                ent["font"] = ("Arial", "13")
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
            else:
                t=info[row][1]
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor2, fg='black', width=56)
                ent["font"] = ("Arial", "13")
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
        for row in range(len(info)):
            if row % 2 == 0:
                t="R$ " + str(info[row][2])
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor1, fg='black', width=29)
                ent["font"] = ("Arial", "13")
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=3)
            else:
                t="R$ " + str(info[row][2])
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor2, fg='black', width=29)
                ent["font"] = ("Arial", "13")
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=3)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


# fim