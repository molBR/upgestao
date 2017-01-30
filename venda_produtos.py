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
menu = Menu(root)
root.config(menu=menu)

subMenu1 = Menu(menu)
menu.add_cascade(label="Menu", menu=subMenu1)
subMenu1.add_command(label="Recarregar", command=Teste)
subMenu1.add_separator()
subMenu1.add_command(label="Sair", command=root.destroy)

subMenu2 = Menu(menu)
menu.add_cascade(label="Arquivo", menu=subMenu2)
subMenu2.add_command(label="Historico de Vendas", command=Teste)
subMenu2.add_command(label="Clientes", command=Teste)
subMenu2.add_command(label="Produtos", command=Teste)

subMenu3 = Menu(menu)
menu.add_cascade(label="...", menu=subMenu3)
# fim

# abas de opcoes
cor1 = '#D32F2F'
cor2 = '#E94545'

toolbar = Frame(root, bg=cor1)

todos = Button(toolbar, text="   Todos   ", bg=cor1,  command=todos_apertado)
todos['font']=('bold')
todos['fg']='white'
todos.pack(side=LEFT, padx=1, pady=6)
doces = Button(toolbar, text="   Doces   ", bg=cor1,  command=doces_apertado)
doces['font']=('bold')
doces['fg']='white'
doces.pack(side=LEFT, padx=1, pady=6)
salgados = Button(toolbar, text="Salgados", bg=cor1, command=salgados_apertado)
salgados['font']=('bold')
salgados['fg']='white'
salgados.pack(side=LEFT, padx=1, pady=6)
massas = Button(toolbar, text="  Massas  ", bg=cor1, command=massas_apertado)
massas['font']=('bold')
massas['fg']='white'
massas.pack(side=LEFT, padx=1, pady=6)
bebidas = Button(toolbar, text=" Bebidas ", bg=cor1, command=bebidas_apertado)
bebidas['font']=('bold')
bebidas['fg']='white'
bebidas.pack(side=LEFT, padx=1, pady=6)
outros = Button(toolbar, text="   Outros   ", bg=cor1, command=outros_apertado)
outros['font']=('bold')
outros['fg']='white'
outros.pack(side=LEFT, padx=1, pady=6)

toolbar.pack(side=TOP, fill=X)
# fim

# barra de 'status'
status = Label(root, text="Estado: Rodando", bg="white", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
# fim

class Example(Frame):
    def __init__(self, root):

        cor3='#E6E6E6'

        self.container1 = Frame(root)
        self.container2 = Frame(root, bg=cor3)
        self.container3 = Frame(root, bg=cor3)
        self.container4 = Frame(root, bg=cor3)
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

        self.salto1 = Label(self.container2, text="", bg=cor3)
        self.salto1.pack(side=LEFT)

        self.espaco1 = Label(self.container3, text="               ", bg=cor3)
        self.espaco1.pack(side=LEFT)
        self.selecionar = Button(self.container3, text="Selecionar", command=Teste, bg=cor3)
        self.selecionar["font"] = ['bold']
        self.selecionar['padx'] = 1
        self.selecionar['pady'] = 1
        self.selecionar.pack(side=LEFT)
        self.espaco2 = Label(self.container3, text="           ", bg=cor3)
        self.espaco2.pack(side=LEFT)
        self.pesquisar1 = Label(self.container3, text="Pesquisar: ", bg=cor3)
        self.pesquisar1["font"] = ['bold']
        self.pesquisar1.pack(side=LEFT)
        self.pesquisar2 = Entry(self.container3)
        self.pesquisar2["width"] = 25
        self.pesquisar2["font"] = ("Arial", "10")
        self.pesquisar2.pack(side=LEFT)
        self.espaco3 = Label(self.container3, text=" ", bg=cor3)
        self.espaco3.pack(side=LEFT)
        self.ok = Button(self.container3, text="Ok", command=Teste, bg=cor3)
        self.ok["font"] = ['bold']
        self.ok['padx'] = 1
        self.ok['pady'] = 1
        self.ok.pack(side=LEFT)
        self.espaco4 = Label(self.container3, text="                     ", bg=cor3)
        self.espaco4.pack(side=LEFT)
        self.remover = Button(self.container3, text="Remover", command=Teste, bg=cor3)
        self.remover["font"] = ['bold']
        self.remover['padx'] = 1
        self.remover['pady'] = 1
        self.remover.pack(side=LEFT)
        self.espaco5 = Label(self.container3, text="                             ", bg=cor3)
        self.espaco5.pack(side=LEFT)
        self.total1 = Label(self.container3, text="Total: ", bg=cor3)
        self.total1["font"] = ['bold']
        self.total1.pack(side=LEFT)
        self.total2 = Label(self.container3, text=t, bg=cor3)
        self.total2["font"] = ['bold']
        self.total2.pack(side=LEFT)
        self.espaco6 = Label(self.container3, text="                             ", bg=cor3)
        self.espaco6.pack(side=LEFT)
        self.continuar = Button(self.container3, text="Continuar", command=Teste, bg=cor3)
        self.continuar["font"] = ['bold']
        self.continuar['padx'] = 1
        self.continuar['pady'] = 1
        self.continuar.pack(side=LEFT)

        self.salto2 = Label(self.container4, text="", bg=cor3)
        self.salto2.pack(side=LEFT)
# fim

# tabela dos itens
        Frame.__init__(self, root) #comeco frame dos produtos
        self.canvas1 = Canvas(root, borderwidth=0, background="#ffffff")
        self.frame1 = Frame(self.canvas1, background="#f0f0f0")
        self.vsb1 = Scrollbar(root, orient="vertical", command=self.canvas1.yview)
        self.canvas1.configure(yscrollcommand=self.vsb1.set)

        self.canvas1.pack(side="left", fill="both", expand=True)
        self.vsb1.pack(side="left", fill="y")
        self.canvas1.create_window((4,4), window=self.frame1, anchor="nw",
                                  tags="self.frame1")

        self.frame1.bind("<Configure>", self.onFrameConfigure1)

        self.populate1() #fim frame dos produtos

        Frame.__init__(self, root) #comeco frame venda
        self.canvas2 = Canvas(root, borderwidth=0, background="#ffffff")
        self.frame2 = Frame(self.canvas2, background="#f0f0f0")
        self.vsb2 = Scrollbar(root, orient="vertical", command=self.canvas2.yview)
        self.canvas2.configure(yscrollcommand=self.vsb2.set)

        self.canvas2.pack(side="left", fill="both", expand=True)
        self.vsb2.pack(side="left", fill="y")
        self.canvas2.create_window((4, 4), window=self.frame2, anchor="nw",
                                  tags="self.frame2")

        self.frame2.bind("<Configure>", self.onFrameConfigure2)

        self.populate2() #fim frame venda

    def populate1(self): #comeco produtos
        info = 20
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t="codigo"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', font="bold", width=15)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=0)
            else:
                cor = '#f0f0f0'
                t = "codigo"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', font="bold", width=15)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=0)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "nome "
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', font="bold", width=25)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
            else:
                cor = '#f0f0f0'
                t = "nome"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', font="bold", width=25)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "R$" "  valor"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', font="bold", width=15)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
            else:
                cor = '#f0f0f0'
                t = "R$"  "  valor"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', font="bold", width=15)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
        #fim produtos

    def onFrameConfigure1(self, event): #comeco scroolbar frame1
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas1.configure(scrollregion=self.canvas1.bbox("all")) #fim scroolbar frame1

    def populate2(self): #comeco venda
        info = 20
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t="codigo"
                ent = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=15)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=0)
            else:
                cor = '#f0f0f0'
                t = "codigo"
                ent = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=15)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=0)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "nome "
                ent = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=25)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
            else:
                cor = '#f0f0f0'
                t = "nome"
                ent = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=25)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "quantidade"
                ent = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=15)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
            else:
                cor = '#f0f0f0'
                t = "quantidade"
                ent = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=15)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
        #fim venda

    def onFrameConfigure2(self, event): #comeco scroolbar frame2
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas2.configure(scrollregion=self.canvas2.bbox("all")) #fim scroolbar frame2
# fim

Example(root).pack(side="top", fill="both", expand=True)
#root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
root.title('Programa Guts')
root.resizable(width=False, height=False)
root.geometry('1061x581')
root.mainloop()