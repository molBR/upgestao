from Tkinter import *

# funcao de teste
def Teste():
    print("Testado")
# fim

#funcao de destaque das abas
def todos_apertado():
    todos.config(relief=SUNKEN, background=cor2)
    doces.config(relief=RAISED, background=cor1)
    salgados.config(relief=RAISED, background=cor1)
    massas.config(relief=RAISED, background=cor1)
    bebidas.config(relief=RAISED, background=cor1)
    outros.config(relief=RAISED, background=cor1)
def doces_apertado():
    todos.config(relief=RAISED, background=cor1)
    doces.config(relief=SUNKEN, background=cor2)
    salgados.config(relief=RAISED, background=cor1)
    massas.config(relief=RAISED, background=cor1)
    bebidas.config(relief=RAISED, background=cor1)
    outros.config(relief=RAISED, background=cor1)
def salgados_apertado():
    todos.config(relief=RAISED, background=cor1)
    doces.config(relief=RAISED, background=cor1)
    salgados.config(relief=SUNKEN, background=cor2)
    massas.config(relief=RAISED, background=cor1)
    bebidas.config(relief=RAISED, background=cor1)
    outros.config(relief=RAISED, background=cor1)
def massas_apertado():
    todos.config(relief=RAISED, background=cor1)
    doces.config(relief=RAISED, background=cor1)
    salgados.config(relief=RAISED, background=cor1)
    massas.config(relief=SUNKEN, background=cor2)
    bebidas.config(relief=RAISED, background=cor1)
    outros.config(relief=RAISED, background=cor1)
def bebidas_apertado():
    todos.config(relief=RAISED, background=cor1)
    doces.config(relief=RAISED, background=cor1)
    salgados.config(relief=RAISED, background=cor1)
    massas.config(relief=RAISED, background=cor1)
    bebidas.config(relief=SUNKEN, background=cor2)
    outros.config(relief=RAISED, background=cor1)
def outros_apertado():
    todos.config(relief=RAISED, background=cor1)
    doces.config(relief=RAISED, background=cor1)
    salgados.config(relief=RAISED, background=cor1)
    massas.config(relief=RAISED, background=cor1)
    bebidas.config(relief=RAISED, background=cor1)
    outros.config(relief=SUNKEN, background=cor2)
#fim

root=Tk()

# menu principal
toolbar1 = Frame(root, bg="white")

menu = Label(toolbar1, text="   MENU ", bg="white")
menu["font"] = ("Arial", "10")
menu.pack(side=LEFT)
espaco1 = Label(toolbar1, text=" | ", bg="white")
espaco1["font"] = ("Arial", "12")
espaco1.pack(side=LEFT)
novavenda = Button(toolbar1, text="Nova Venda", bg="white", relief=FLAT)
novavenda["font"] = ("Arial", "10")
novavenda.pack(side=LEFT, padx=1, pady=1)
espaco2 = Label(toolbar1, text=" | ", bg="white")
espaco2["font"] = ("Arial", "12")
espaco2.pack(side=LEFT)
cadastrarcliente = Button(toolbar1, text="Cadastrar Cliente", bg="white", relief=FLAT)
cadastrarcliente["font"] = ("Arial", "10")
cadastrarcliente.pack(side=LEFT, padx=1, pady=1)
espaco3 = Label(toolbar1, text=" | ", bg="white")
espaco3["font"] = ("Arial", "12")
espaco3.pack(side=LEFT)
historicovenda = Button(toolbar1, text="Historico de Vendas", bg="white", relief=FLAT)
historicovenda["font"] = ("Arial", "10")
historicovenda.pack(side=LEFT, padx=1, pady=1)
espaco4 = Label(toolbar1, text=" | ", bg="white")
espaco4["font"] = ("Arial", "12")
espaco4.pack(side=LEFT)
inserirproduto = Button(toolbar1, text="Inserir Produto", bg="white", relief=FLAT)
inserirproduto["font"] = ("Arial", "10")
inserirproduto.pack(side=LEFT, padx=1, pady=1)
espaco5 = Label(toolbar1, text=" | ", bg="white")
espaco5["font"] = ("Arial", "12")
espaco5.pack(side=LEFT)
inserirtipo = Button(toolbar1, text="Inserir Tipo", bg="light grey", relief=FLAT)
inserirtipo["font"] = ("Arial", "10")
inserirtipo.pack(side=LEFT, padx=1, pady=1)

toolbar1.pack(side=TOP, fill=X)
# fim

# abas de opcoes
cor1 = '#D32F2F'
cor2 = '#E94545'

toolbar2 = Frame(root, bg=cor1)

todos = Button(toolbar2, text="   Todos   ", bg=cor1,  command=todos_apertado)
todos['font']=('bold')
todos['fg']='white'
todos.pack(side=LEFT, padx=1, pady=1)
doces = Button(toolbar2, text="   Doces   ", bg=cor1,  command=doces_apertado)
doces['font']=('bold')
doces['fg']='white'
doces.pack(side=LEFT, padx=1, pady=1)
salgados = Button(toolbar2, text="Salgados", bg=cor1, command=salgados_apertado)
salgados['font']=('bold')
salgados['fg']='white'
salgados.pack(side=LEFT, padx=1, pady=1)
massas = Button(toolbar2, text="  Massas  ", bg=cor1, command=massas_apertado)
massas['font']=('bold')
massas['fg']='white'
massas.pack(side=LEFT, padx=1, pady=1)
bebidas = Button(toolbar2, text=" Bebidas ", bg=cor1, command=bebidas_apertado)
bebidas['font']=('bold')
bebidas['fg']='white'
bebidas.pack(side=LEFT, padx=1, pady=1)
outros = Button(toolbar2, text="   Outros   ", bg=cor1, command=outros_apertado)
outros['font']=('bold')
outros['fg']='white'
outros.pack(side=LEFT, padx=1, pady=1)

toolbar2.pack(side=TOP, fill=X)
# fim

# barra de 'status'
status = Label(root, text="Estado: Rodando", bg="white", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
# fim

class Example(Frame):
    def __init__(self, root):

        self.container1 = Frame(root)
        self.container2 = Frame(root)
        self.container1.pack(fill=X)
        self.container2.pack(side=BOTTOM, fill=X, padx=15, pady=15)

#"cabecalho" da tabela dos itens
        self.objeto1 = Label(self.container1, text="       Codigo:")
        self.objeto1["font"] = ["bold"]
        self.objeto1.pack(side=LEFT)
        self.objeto2 = Label(self.container1, text="                  ")
        self.objeto2["font"] = ["bold"]
        self.objeto2.pack(side=LEFT)
        self.objeto3 = Label(self.container1, text="Nome:")
        self.objeto3["font"] = ["bold"]
        self.objeto3.pack(side=LEFT)
        self.objeto4 = Label(self.container1, text="                                                                                              ")
        self.objeto4["font"] = ["bold"]
        self.objeto4.pack(side=LEFT)
        self.objeto1 = Label(self.container1, text="Codigo:")
        self.objeto1["font"] = ["bold"]
        self.objeto1.pack(side=LEFT)
        self.objeto2 = Label(self.container1, text="                  ")
        self.objeto2["font"] = ["bold"]
        self.objeto2.pack(side=LEFT)
        self.objeto3 = Label(self.container1, text="Nome:")
        self.objeto3["font"] = ["bold"]
        self.objeto3.pack(side=LEFT)
        self.objeto4 = Label(self.container1, text="                                                       ")
        self.objeto4["font"] = ["bold"]
        self.objeto4.pack(side=LEFT)
# fim

# espaco com "inserir", "editar", "excluir" e "pesquisar"

        self.espaco1 = Label(self.container2, text="             ")
        self.espaco1.pack(side=LEFT)
        self.inserir = Button(self.container2, text="Inserir", command=Teste)
        self.inserir["font"] = ("Arial", "10")
        self.inserir['padx'] = 10
        self.inserir.pack(side=LEFT)
        self.espaco2 = Label(self.container2, text="             ")
        self.espaco2.pack(side=LEFT)
        self.editar = Button(self.container2, text="Editar", command=Teste)
        self.editar["font"] = ("Arial", "10")
        self.editar['padx'] = 10
        self.editar.pack(side=LEFT)
        self.espaco2 = Label(self.container2, text="             ")
        self.espaco2.pack(side=LEFT)
        self.excluir = Button(self.container2, text="Excluir", command=Teste)
        self.excluir["font"] = ("Arial", "10")
        self.excluir['padx'] = 10
        self.excluir.pack(side=LEFT)
        self.espaco3 = Label(self.container2, text="             ")
        self.espaco3.pack(side=LEFT)
        self.pesquisar1 = Label(self.container2, text="Pesquisar: ")
        self.pesquisar1["font"] = ("Arial", "10")
        self.pesquisar1.pack(side=LEFT)
        self.pesquisar2 = Entry(self.container2)
        self.pesquisar2["width"] = 25
        self.pesquisar2["font"] = ("Arial", "10")
        self.pesquisar2.pack(side=LEFT)
        pesquisado = self.pesquisar2.get()  # pesquisado = o que foi escrito no "Entry / barra de pesquisa"
        self.espaco4 = Label(self.container2, text=" ")
        self.espaco4.pack(side=LEFT)
        self.ok = Button(self.container2, text="Ok", command=Teste)
        self.ok["font"] = ("Arial", "10")
        self.ok['padx'] = 10
        self.ok.pack(side=LEFT)
# fim

# tabela dos itens
        Frame.__init__(self, root)
        self.canvas1 = Canvas(root, borderwidth=0, background="#ffffff")
        self.frame1 = Frame(self.canvas1, background="#f0f0f0")
        self.vsb1 = Scrollbar(root, orient="vertical", command=self.canvas1.yview)
        self.canvas1.configure(yscrollcommand=self.vsb1.set)

        self.canvas1.pack(side="left", fill="both", expand=True)
        self.vsb1.pack(side="left", fill="y")
        self.canvas1.create_window((4, 4), window=self.frame1, anchor="nw",
                                   tags="self.frame1")

        self.frame1.bind("<Configure>", self.onFrameConfigure1)

        self.populate1()

        Frame.__init__(self, root)
        self.canvas2 = Canvas(root, borderwidth=0, background="#ffffff")
        self.frame2 = Frame(self.canvas2, background="#f0f0f0")
        self.vsb2 = Scrollbar(root, orient="vertical", command=self.canvas2.yview)
        self.canvas2.configure(yscrollcommand=self.vsb2.set)

        self.canvas2.pack(side="left", fill="both", expand=True)
        self.vsb2.pack(side="left", fill="y")
        self.canvas2.create_window((4, 4), window=self.frame2, anchor="nw",
                                   tags="self.frame2")

        self.frame2.bind("<Configure>", self.onFrameConfigure2)

        self.populate2()

    def populate1(self):
        info = 20
        '''Put in some fake data'''
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                var = IntVar()
                c = Checkbutton(self.frame1, variable=var, background=cor)
                c.grid(row=row, column=0)
            else:
                cor = '#f0f0f0'
                var = IntVar()
                c = Checkbutton(self.frame1, variable=var, background=cor)
                c.grid(row=row, column=0)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t="codigo"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
            else:
                cor = '#f0f0f0'
                t = "codigo"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "nome "
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', width=40)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
            else:
                cor = '#f0f0f0'
                t = "nome"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', width=40)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)

    def onFrameConfigure1(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas1.configure(scrollregion=self.canvas1.bbox("all"))

    def populate2(self):
        info = 20
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                var = IntVar()
                c = Checkbutton(self.frame2, variable=var, background=cor)
                c.grid(row=row, column=0)
            else:
                cor = '#f0f0f0'
                var = IntVar()
                c = Checkbutton(self.frame2, variable=var, background=cor)
                c.grid(row=row, column=0)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t="codigo"
                ent = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
            else:
                cor = '#f0f0f0'
                t = "codigo"
                ent = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', width=15)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "nome "
                ent = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', width=40)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
            else:
                cor = '#f0f0f0'
                t = "nome"
                ent = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', width=40)
                ent["font"] = ("Arial", "13")
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)

    def onFrameConfigure2(self, event): #comeco scroolbar frame2
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas2.configure(scrollregion=self.canvas2.bbox("all")) #fim
# fim

Example(root).pack(side="top", fill="both", expand=True)
#root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
root.title('Inserir Tipo')
root.resizable(width=False, height=False)
root.geometry('1150x600')
root.mainloop()