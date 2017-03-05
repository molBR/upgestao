# encoding: utf-8

import Tkinter as Tkin
from database import database as db
import cadastro_produto_menor as cpm
from database import tratamentos as tr
import tkMessageBox
import cadastro_produto_deletar as cpd
import cadastro_produto_editar_1 as cpe


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
    def __del__(self):
        self.bd.close()

#Construtor
    def __init__(self):
        self.root = None

    def CloseWindow(self):
        self.root.destroy()
        self.root.quit()
        self.root = None

    def FazTela(self):
# Nao sei descrever o que e isso, tem que perguntar pro luquinha mito
        if (self.root != None):
            self.CloseWindow()
            self.root = None
            self.FazTela()
        else:
            self.root = Tkin.Toplevel()
            menu = Tkin.Menu(self.root)
            self.root.config(menu=menu)

            ###
            subMenu1 = Tkin.Menu(menu)
            menu.add_cascade(label="Menu", menu=subMenu1)
            subMenu1.add_command(label="Recarregar")
            subMenu1.add_separator()
            subMenu1.add_command(label="Sair", command=self.root.destroy)

            subMenu2 = Tkin.Menu(menu)
            menu.add_cascade(label="Arquivo", menu=subMenu2)
            subMenu2.add_command(label="Historico de Vendas")
            subMenu2.add_command(label="Clientes")
            subMenu2.add_command(label="Produtos")

            subMenu3 = Tkin.Menu(menu)
            menu.add_cascade(label="...", menu=subMenu3)
            # fim

            # barra de 'status'
            status = Tkin.Label(self.root, text="Estado: Rodando", bg="white", bd=1, relief=Tkin.SUNKEN, anchor=Tkin.W)
            status.pack(side=Tkin.BOTTOM, fill=Tkin.X)

            self.bd = db.Database(0)  # banco de dados
            self.tm = cpm.TelaMenor()  # inserir
            self.td = cpd.TelaMenorDel()  # deletar
            self.te = cpe.TelaMenorEdit1()  # editar

            self.cor1 = '#D32F2F'
            self.cor2 = '#E94545'
            self.cor3 = '#E6E6E6'

            self.toolbar = Tkin.Frame(self.root, bg=self.cor1)

            self.todos = Tkin.Button(self.toolbar, text="   Todos   ", bg=self.cor1, command=self.todos_apertado)
            self.todos['font'] = ('bold')
            self.todos['fg'] = 'white'
            self.todos.pack(side=Tkin.LEFT, padx=1, pady=6)
            self.doces = Tkin.Button(self.toolbar, text="   Doces   ", bg=self.cor1, command=self.doces_apertado)
            self.doces['font'] = ('bold')
            self.doces['fg'] = 'white'
            self.doces.pack(side=Tkin.LEFT, padx=1, pady=6)
            self.salgados = Tkin.Button(self.toolbar, text="Salgados", bg=self.cor1, command=self.salgados_apertado)
            self.salgados['font'] = ('bold')
            self.salgados['fg'] = 'white'
            self.salgados.pack(side=Tkin.LEFT, padx=1, pady=6)
            self.massas = Tkin.Button(self.toolbar, text="  Massas  ", bg=self.cor1, command=self.massas_apertado)
            self.massas['font'] = ('bold')
            self.massas['fg'] = 'white'
            self.massas.pack(side=Tkin.LEFT, padx=1, pady=6)
            self.bebidas = Tkin.Button(self.toolbar, text=" Bebidas ", bg=self.cor1, command=self.bebidas_apertado)
            self.bebidas['font'] = ('bold')
            self.bebidas['fg'] = 'white'
            self.bebidas.pack(side=Tkin.LEFT, padx=1, pady=6)
            self.outros = Tkin.Button(self.toolbar, text="   Outros   ", bg=self.cor1, command=self.outros_apertado)
            self.outros['font'] = ('bold')
            self.outros['fg'] = 'white'
            self.outros.pack(side=Tkin.LEFT, padx=1, pady=6)

            self.toolbar.pack(side=Tkin.TOP, fill=Tkin.X)

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
            self.root.title('Programa Guts')
            self.root.resizable(width=False, height=False)
            self.root.protocol("WM_DELETE_WINDOW", lambda: self.CloseWindow())
            self.root.geometry('1061x581')
            self.root.mainloop()



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
                t=info[row][0]
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor1, fg='black', font="bold", width=29)
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=0)
            else:
                t=info[row][0]
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor2, fg='black', font="bold", width=29)
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=0)
        for row in range(len(info)):
            if row % 2 == 0:
                t=info[row][1]
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor1, fg='black', font="bold", width=56)
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
            else:
                t=info[row][1]
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor2, fg='black', font="bold", width=56)
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
        for row in range(len(info)):
            if row % 2 == 0:
                t="R$ " + str(info[row][2])
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor1, fg='black', font="bold", width=29)
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
            else:
                t="R$ " + str(info[row][2])
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor2, fg='black', font="bold", width=29)
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


# fim