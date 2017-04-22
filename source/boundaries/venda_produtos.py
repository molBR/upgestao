# encoding: utf-8

from Tkinter import *
from source.entities import database as db

# funcao de teste
def Teste():
    print("Testado")
# fim

#funcao de destaque das abas
#fim

# menu principal
class TelaMaior(Frame):
    def todos_apertado(self):
        self.todos.config(relief=SUNKEN, background=self.cor2)
        self.doces.config(relief=RAISED, background=self.cor1)
        self.salgados.config(relief=RAISED, background=self.cor1)
        self.massas.config(relief=RAISED, background=self.cor1)
        self.bebidas.config(relief=RAISED, background=self.cor1)
        self.outros.config(relief=RAISED, background=self.cor1)
        self.tipos.config(relief=RAISED, background=self.cor1)

    def doces_apertado(self):
        self.todos.config(relief=RAISED, background=self.cor1)
        self.doces.config(relief=SUNKEN, background=self.cor2)
        self.salgados.config(relief=RAISED, background=self.cor1)
        self.massas.config(relief=RAISED, background=self.cor1)
        self.bebidas.config(relief=RAISED, background=self.cor1)
        self.outros.config(relief=RAISED, background=self.cor1)
        self.tipos.config(relief=RAISED, background=self.cor1)

    def salgados_apertado(self):
        self.todos.config(relief=RAISED, background=self.cor1)
        self.doces.config(relief=RAISED, background=self.cor1)
        self.salgados.config(relief=SUNKEN, background=self.cor2)
        self.massas.config(relief=RAISED, background=self.cor1)
        self.bebidas.config(relief=RAISED, background=self.cor1)
        self.outros.config(relief=RAISED, background=self.cor1)
        self.tipos.config(relief=RAISED, background=self.cor1)

    def massas_apertado(self):
        self.todos.config(relief=RAISED, background=self.cor1)
        self.doces.config(relief=RAISED, background=self.cor1)
        self.salgados.config(relief=RAISED, background=self.cor1)
        self.massas.config(relief=SUNKEN, background=self.cor2)
        self.bebidas.config(relief=RAISED, background=self.cor1)
        self.outros.config(relief=RAISED, background=self.cor1)
        self.tipos.config(relief=RAISED, background=self.cor1)

    def bebidas_apertado(self):
        self.todos.config(relief=RAISED, background=self.cor1)
        self.doces.config(relief=RAISED, background=self.cor1)
        self.salgados.config(relief=RAISED, background=self.cor1)
        self.massas.config(relief=RAISED, background=self.cor1)
        self.bebidas.config(relief=SUNKEN, background=self.cor2)
        self.outros.config(relief=RAISED, background=self.cor1)
        self.tipos.config(relief=RAISED, background=self.cor1)

    def outros_apertado(self):
        self.todos.config(relief=RAISED, background=self.cor1)
        self.doces.config(relief=RAISED, background=self.cor1)
        self.salgados.config(relief=RAISED, background=self.cor1)
        self.massas.config(relief=RAISED, background=self.cor1)
        self.bebidas.config(relief=RAISED, background=self.cor1)
        self.outros.config(relief=SUNKEN, background=self.cor2)
        self.tipos.config(relief=RAISED, background=self.cor1)

    def tipos_apertado(self):
        self.todos.config(relief=RAISED, background=self.cor1)
        self.doces.config(relief=RAISED, background=self.cor1)
        self.salgados.config(relief=RAISED, background=self.cor1)
        self.massas.config(relief=RAISED, background=self.cor1)
        self.bebidas.config(relief=RAISED, background=self.cor1)
        self.outros.config(relief=RAISED, background=self.cor1)
        self.tipos.config(relief=SUNKEN, background=self.cor2)

    #def __init__(self):


    def FazTela(self, root, control):

        self.bd = db.Database(0)  # banco de dados

        self.root = root
        for widget in self.root.winfo_children():
            widget.destroy()

        #ctrl.Control.start(self.root)

        self.root.title('Guts\' Orçamento - Nova Venda')

        # menu
        toolbar1 = Frame(self.root, bg="white")

        self.menu = Label(toolbar1, text="   Menu Inicial ", bg="white")
        self.menu["font"] = ("Arial", "10")
        self.menu.pack(side=LEFT)
        self.espaco1 = Label(toolbar1, text=" | ", bg="white")
        self.espaco1["font"] = ("Arial", "12")
        self.espaco1.pack(side=LEFT)
        self.novavenda = Button(toolbar1, text="Nova Venda", bg="light grey", relief=FLAT)
        self.novavenda["font"] = ("Arial", "10")
        self.novavenda.pack(side=LEFT, padx=1, pady=1)
        self.espaco2 = Label(toolbar1, text=" | ", bg="white")
        self.espaco2["font"] = ("Arial", "12")
        self.espaco2.pack(side=LEFT)
        self.cadastrarcliente = Button(toolbar1, text="Cadastrar Cliente", bg="white", relief=FLAT)
        self.cadastrarcliente["font"] = ("Arial", "10")
        self.cadastrarcliente.pack(side=LEFT, padx=1, pady=1)
        self.espaco3 = Label(toolbar1, text=" | ", bg="white")
        self.espaco3["font"] = ("Arial", "12")
        self.espaco3.pack(side=LEFT)
        self.historicovenda = Button(toolbar1, text="Historico de Vendas", bg="white", relief=FLAT)
        self.historicovenda["font"] = ("Arial", "10")
        self.historicovenda.pack(side=LEFT, padx=1, pady=1)
        self.espaco4 = Label(toolbar1, text=" | ", bg="white")
        self.espaco4["font"] = ("Arial", "12")
        self.espaco4.pack(side=LEFT)
        self.inserirproduto = Button(toolbar1, text="Inserir Produto", bg="white", relief=FLAT)
        self.inserirproduto["font"] = ("Arial", "10")
        self.inserirproduto.pack(side=LEFT, padx=1, pady=1)
        self.espaco5 = Label(toolbar1, text=" | ", bg="white")
        self.espaco5["font"] = ("Arial", "12")
        self.espaco5.pack(side=LEFT)
        self.inserirtipo = Button(toolbar1, text="Inserir Tipo", bg="white", relief=FLAT)
        self.inserirtipo["font"] = ("Arial", "10")
        self.inserirtipo.pack(side=LEFT, padx=1, pady=1)

        toolbar1.pack(side=TOP, fill=X)
        # fim

    # barra de 'status'
        status = Label(self.root, text="Estado: Rodando", bg="white", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
    # fim

    # abas de opcoes
        self.cor1 = '#D32F2F'
        self.cor2 = '#E94545'

        toolbar2 = Frame(self.root, bg=self.cor1)

        self.todos = Button(toolbar2, text="   Todos   ", bg=self.cor1, command=self.todos_apertado)
        self.todos["font"] = ("Arial", "12")
        self.todos['fg'] = 'white'
        self.todos.pack(side=LEFT, padx=1, pady=1)
        self.doces = Button(toolbar2, text="   Doces   ", bg=self.cor1, command=self.doces_apertado)
        self.doces["font"] = ("Arial", "12")
        self.doces['fg'] = 'white'
        self.doces.pack(side=LEFT, padx=1, pady=1)
        self.salgados = Button(toolbar2, text="Salgados", bg=self.cor1, command=self.salgados_apertado)
        self.salgados["font"] = ("Arial", "12")
        self.salgados['fg'] = 'white'
        self.salgados.pack(side=LEFT, padx=1, pady=1)
        self.massas = Button(toolbar2, text="  Massas  ", bg=self.cor1, command=self.massas_apertado)
        self.massas["font"] = ("Arial", "12")
        self.massas['fg'] = 'white'
        self.massas.pack(side=LEFT, padx=1, pady=1)
        self.bebidas = Button(toolbar2, text=" Bebidas ", bg=self.cor1, command=self.bebidas_apertado)
        self.bebidas["font"] = ("Arial", "12")
        self.bebidas['fg'] = 'white'
        self.bebidas.pack(side=LEFT, padx=1, pady=1)
        self.outros = Button(toolbar2, text="   Outros   ", bg=self.cor1, command=self.outros_apertado)
        self.outros["font"] = ("Arial", "12")
        self.outros['fg'] = 'white'
        self.outros.pack(side=LEFT, padx=1, pady=1)
        self.tipos = Button(toolbar2, text="   Tipos   ", bg=self.cor1, command=self.tipos_apertado)
        self.tipos["font"] = ("Arial", "12")
        self.tipos['fg'] = 'white'
        self.tipos.pack(side=LEFT, padx=1, pady=1)

        toolbar2.pack(side=TOP, fill=X)
    # fim

        self.cor3='#E6E6E6'

        self.container1 = Frame(self.root)
        self.container2 = Frame(self.root, bg=self.cor3)
        self.container3 = Frame(self.root, bg=self.cor3)
        self.container4 = Frame(self.root, bg=self.cor3)
        self.container1.pack(fill=X)
        self.container2.pack(side=BOTTOM, fill=X)
        self.container3.pack(side=BOTTOM, fill=X)
        self.container4.pack(side=BOTTOM, fill=X)

    #"cabecalho" da tabela dos itens
        self.objeto1 = Label(self.container1, text="Codigo:")
        self.objeto1["font"] = ["bold"]
        self.objeto1.pack(side=LEFT)
        self.objeto2 = Label(self.container1, text="                  ")
        self.objeto2["font"] = ["bold"]
        self.objeto2.pack(side=LEFT)
        self.objeto3 = Label(self.container1, text="Nome")
        self.objeto3["font"] = ["bold"]
        self.objeto3.pack(side=LEFT)
        self.objeto4 = Label(self.container1, text="                                            ")
        self.objeto4["font"] = ["bold"]
        self.objeto4.pack(side=LEFT)
        self.objeto5 = Label(self.container1, text="Valor")
        self.objeto5["font"] = ["bold"]
        self.objeto5.pack(side=LEFT)
        self.objeto6 = Label(self.container1, text="                            ")
        self.objeto6["font"] = ["bold"]
        self.objeto6.pack(side=LEFT)
        self.objeto7 = Label(self.container1, text="Codigo")
        self.objeto7["font"] = ["bold"]
        self.objeto7.pack(side=LEFT)
        self.objeto8 = Label(self.container1, text="                   ")
        self.objeto8["font"] = ["bold"]
        self.objeto8.pack(side=LEFT)
        self.objeto9 = Label(self.container1, text="Nome")
        self.objeto9["font"] = ["bold"]
        self.objeto9.pack(side=LEFT)
        self.objeto10 = Label(self.container1, text="                                           ")
        self.objeto10["font"] = ["bold"]
        self.objeto10.pack(side=LEFT)
        self.objeto11 = Label(self.container1, text="Quantidade")
        self.objeto11["font"] = ["bold"]
        self.objeto11.pack(side=LEFT)
    # fim

    # espaco com "inserir", "editar", "excluir" e "pesquisar"

        t = "VALOR"

        self.salto1 = Label(self.container2, text="", bg=self.cor3)
        self.salto1.pack(side=LEFT)

        self.espaco1 = Label(self.container3, text="               ", bg=self.cor3)
        self.espaco1.pack(side=LEFT)
        self.selecionar = Button(self.container3, text="Selecionar", command=Teste, bg=self.cor3)
        self.selecionar["font"] = ['bold']
        self.selecionar['padx'] = 1
        self.selecionar['pady'] = 1
        self.selecionar.pack(side=LEFT)
        self.espaco2 = Label(self.container3, text="           ", bg=self.cor3)
        self.espaco2.pack(side=LEFT)
        self.pesquisar1 = Label(self.container3, text="Pesquisar: ", bg=self.cor3)
        self.pesquisar1["font"] = ['bold']
        self.pesquisar1.pack(side=LEFT)
        self.pesquisar2 = Entry(self.container3)
        self.pesquisar2["width"] = 25
        self.pesquisar2["font"] = ("Arial", "10")
        self.pesquisar2.pack(side=LEFT)
        self.espaco3 = Label(self.container3, text=" ", bg=self.cor3)
        self.espaco3.pack(side=LEFT)
        self.ok = Button(self.container3, text="Ok", command=Teste, bg=self.cor3)
        self.ok["font"] = ['bold']
        self.ok['padx'] = 1
        self.ok['pady'] = 1
        self.ok.pack(side=LEFT)
        self.espaco4 = Label(self.container3, text="                     ", bg=self.cor3)
        self.espaco4.pack(side=LEFT)
        self.remover = Button(self.container3, text="Remover", command=Teste, bg=self.cor3)
        self.remover["font"] = ['bold']
        self.remover['padx'] = 1
        self.remover['pady'] = 1
        self.remover.pack(side=LEFT)
        self.espaco5 = Label(self.container3, text="                             ", bg=self.cor3)
        self.espaco5.pack(side=LEFT)
        self.total1 = Label(self.container3, text="Total: ", bg=self.cor3)
        self.total1["font"] = ['bold']
        self.total1.pack(side=LEFT)
        self.total2 = Label(self.container3, text=t, bg=self.cor3)
        self.total2["font"] = ['bold']
        self.total2.pack(side=LEFT)
        self.espaco6 = Label(self.container3, text="                             ", bg=self.cor3)
        self.espaco6.pack(side=LEFT)
        self.continuar = Button(self.container3, text="Continuar", command=Teste, bg=self.cor3)
        self.continuar["font"] = ['bold']
        self.continuar['padx'] = 1
        self.continuar['pady'] = 1
        self.continuar.pack(side=LEFT)

        self.salto2 = Label(self.container4, text="", bg=self.cor3)
        self.salto2.pack(side=LEFT)
    # fim

    # tabela dos itens
        Frame.__init__(self, self.root) #comeco frame dos produtos
        self.canvas1 = Canvas(self.root, borderwidth=0, background="#ffffff")
        self.frame1 = Frame(self.canvas1, background="#f0f0f0")
        self.vsb1 = Scrollbar(self.root, orient="vertical", command=self.canvas1.yview)
        self.canvas1.configure(yscrollcommand=self.vsb1.set)

        self.canvas1.pack(side="left", fill="both", expand=True)
        self.vsb1.pack(side="left", fill="y")
        self.canvas1.create_window((4,4), window=self.frame1, anchor="nw",
                                  tags="self.frame1")

        self.frame1.bind("<Configure>", self.onFrameConfigure1)

        self.pacote1 = [self.canvas1,self.frame1,self.vsb1,"self.frame1"]

        self.populate1(self.bd.selectProduto()) #fim frame dos produtos

        Frame.__init__(self, self.root) #comeco frame venda
        self.canvas2 = Canvas(self.root, borderwidth=0, background="#ffffff")
        self.frame2 = Frame(self.canvas2, background="#f0f0f0")
        self.vsb2 = Scrollbar(self.root, orient="vertical", command=self.canvas2.yview)
        self.canvas2.configure(yscrollcommand=self.vsb2.set)

        self.canvas2.pack(side="left", fill="both", expand=True)
        self.vsb2.pack(side="left", fill="y")
        self.canvas2.create_window((4, 4), window=self.frame2, anchor="nw",
                                  tags="self.frame2")

        self.frame2.bind("<Configure>", self.onFrameConfigure2)

        self.pacote2 = [self.canvas2, self.frame2, self.vsb2, "self.frame2"]

        self.populate2()  # fim frame dos produtos


    def deleteCanvas(self,pacote):
        if pacote[0] != None:
            pacote[0].destroy()
            pacote[2].destroy()
            pacote[0] = None
        return

    #  self.pacote1 = [self.canvas1,self.frame1,self.vsb1]
    def createCanvas(self,pacote):
        #Frame.__init__(self, self.root)
        pacote[0] = Canvas(self.root, borderwidth=0, background="#ffffff")
        pacote[1] = Frame(pacote[0], background="#f0f0f0")
        pacote[2] = Scrollbar(self.root, orient="vertical", command=pacote[0].yview)
        pacote[0].configure(yscrollcommand=pacote[2].set)

        pacote[0].pack(side="left", fill="both", expand=True)
        pacote[2].pack(side="left", fill="y")
        pacote[0].create_window((4,4), window=pacote[1], anchor="nw",
                                  tags=pacote[3])
        pacote[1].bind("<Configure>", self.onFrameConfigure1)

    def populate1(self,info): #comeco produtos
        self.deleteCanvas(self.pacote1)
        self.createCanvas(self.pacote1)

        for row in range(len(info)):
            if row % 2 == 0:
                cor = '#ffffff'
                var = IntVar()
                c = Checkbutton(self.pacote1[1], variable=var, background=cor)
                c.grid(row=row, column=0)
            else:
                cor = '#f0f0f0'
                var = IntVar()
                c = Checkbutton(self.pacote1[1], variable=var, background=cor)
                c.grid(row=row, column=0)
        for row in range(len(info)):
            if row % 2 == 0:
                cor = '#ffffff'
                t=info[row][0]
                ent = Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
            else:
                cor = '#f0f0f0'
                t = info[row][0]
                ent = Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
        for row in range(len(info)):
            if row % 2 == 0:
                cor = '#ffffff'
                t = info[row][1]
                ent = Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=25)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
            else:
                cor = '#f0f0f0'
                t = info[row][1]
                ent = Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=25)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
        for row in range(len(info)):
            if row % 2 == 0:
                cor = '#ffffff'
                t = info[row][2]
                ent = Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=3)
            else:
                cor = '#f0f0f0'
                t = info[row][2]
                ent = Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=3)
        #fim produtos

    def onFrameConfigure1(self, event): #comeco scroolbar frame1
        '''Reset the scroll region to encompass the inner frame'''
        self.pacote1[0].configure(scrollregion=self.pacote1[0].bbox("all")) #fim scroolbar frame1

    def populate2(self): #comeco venda

        self.deleteCanvas(self.pacote2)
        self.createCanvas(self.pacote2)
        info = 20
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                var = IntVar()
                c = Checkbutton(self.pacote2[1], variable=var, background=cor)
                c.grid(row=row, column=0)
            else:
                cor = '#f0f0f0'
                var = IntVar()
                c = Checkbutton(self.pacote2[1], variable=var, background=cor)
                c.grid(row=row, column=0)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t="codigo"
                ent = Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
            else:
                cor = '#f0f0f0'
                t = "codigo"
                ent = Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "nome "
                ent = Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', width=25)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
            else:
                cor = '#f0f0f0'
                t = "nome"
                ent = Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', width=25)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "quantidade"
                ent = Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=3)
            else:
                cor = '#f0f0f0'
                t = "quantidade"
                ent = Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=3)
        #fim


    def onFrameConfigure2(self, event): #comeco scroolbar frame2
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas2.configure(scrollregion=self.canvas2.bbox("all")) #fim scroolbar frame2
# fim
