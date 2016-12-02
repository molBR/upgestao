from Tkinter import *

# funcao para teste
def Teste():
    print("Testado")
# fim

root=Tk()

# menu principal
menu = Menu(root)
root.config(menu=menu)

subMenu1 = Menu(menu)
menu.add_cascade(label="Arquivo", menu=subMenu1)
subMenu1.add_command(label="Novo", command=Teste)
subMenu1.add_command(label="Salvar", command=Teste)
subMenu1.add_separator()
subMenu1.add_command(label="Sair", command=Teste)

subMenu2 = Menu(menu)
menu.add_cascade(label="Editar", menu=subMenu2)
subMenu2.add_command(label="Copiar Tudo", command=Teste)
subMenu2.add_command(label="Copiar", command=Teste)
subMenu2.add_command(label="Colar", command=Teste)
subMenu2.add_command(label="Cortar", command=Teste)

subMenu3 = Menu(menu)
menu.add_cascade(label="Visualizar", menu=subMenu3)
subMenu3.add_command(label="Ferramentas", command=Teste)
subMenu3.add_command(label="Arquivo Recente", command=Teste)
# fim

# abas de opcoes
cor1 = '#D32F2F'

toolbar = Frame(root, bg=cor1)

opcao1 = Button(toolbar, text="   Doces   ", bg=cor1,  command=Teste)
opcao1['font']=('bold')
opcao1['fg']='white'
opcao1.pack(side=LEFT, padx=1, pady=1)
opcao2 = Button(toolbar, text="Salgados", bg=cor1, command=Teste)
opcao2['font']=('bold')
opcao2['fg']='white'
opcao2.pack(side=LEFT, padx=1, pady=1)
opcao3 = Button(toolbar, text="  Massas  ", bg=cor1, command=Teste)
opcao3['font']=('bold')
opcao3['fg']='white'
opcao3.pack(side=LEFT, padx=1, pady=1)
opcao4 = Button(toolbar, text="  Bebidas  ", bg=cor1, command=Teste)
opcao4['font']=('bold')
opcao4['fg']='white'
opcao4.pack(side=LEFT, padx=1, pady=1)
opcao5 = Button(toolbar, text="   Outros   ", bg=cor1, command=Teste)
opcao5['font']=('bold')
opcao5['fg']='white'
opcao5.pack(side=LEFT, padx=1, pady=1)

toolbar.pack(side=TOP, fill=X)
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
        self.objeto2 = Label(self.container1, text="                                       ")
        self.objeto2["font"] = ["bold"]
        self.objeto2.pack(side=LEFT)
        self.objeto3 = Label(self.container1, text="Nome:")
        self.objeto3["font"] = ["bold"]
        self.objeto3.pack(side=LEFT)
        self.objeto4 = Label(self.container1, text="                                              ")
        self.objeto4["font"] = ["bold"]
        self.objeto4.pack(side=LEFT)
        self.objeto5 = Label(self.container1, text="Valor:")
        self.objeto5["font"] = ["bold"]
        self.objeto5.pack(side=LEFT)
        self.objeto6 = Label(self.container1, text="                                              ")
        self.objeto6["font"] = ["bold"]
        self.objeto6.pack(side=LEFT)
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
        self.canvas = Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#f0f0f0")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()

    def populate(self):
        info = 20
        '''Put in some fake data'''
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                var1 = IntVar()
                Checkbutton(self.frame, text="", variable=var1, background=cor, command=Teste).grid(row=row, sticky=W)
                t="codigo"
                Label(self.frame, text=t, font="bold", background=cor).grid(row=row, column=1)
            else:
                cor = '#f0f0f0'
                var1 = IntVar()
                Checkbutton(self.frame, text="", variable=var1, background=cor).grid(row=row, sticky=W)
                t = "codigo"
                Label(self.frame, text=t, font="bold", background=cor).grid(row=row, column=1)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "                                         "
                Label(self.frame, text=t, font="bold", background=cor).grid(row=row, column=2)
            else:
                cor = '#f0f0f0'
                t = ""
                Label(self.frame, text=t, font="bold", background=cor).grid(row=row, column=2)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "nome "
                Label(self.frame, text=t, font="bold", background=cor).grid(row=row, column=3)
            else:
                cor = '#f0f0f0'
                t = "nome"
                Label(self.frame, text=t, font="bold", background=cor).grid(row=row, column=3)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "                                               "
                Label(self.frame, text=t, font="bold", background=cor).grid(row=row, column=4)
            else:
                cor = '#f0f0f0'
                t = ""
                Label(self.frame, text=t, font="bold", background=cor).grid(row=row, column=4)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "R$" "  valor"
                Label(self.frame, text=t, font="bold", background=cor).grid(row=row, column=5)
            else:
                cor = '#f0f0f0'
                t = "R$"  "  valor"
                Label(self.frame, text=t, font="bold", background=cor).grid(row=row, column=5)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "                                               "
                Label(self.frame, text=t, font="bold", background=cor).grid(row=row, column=6)
            else:
                cor = '#f0f0f0'
                t = ""
                Label(self.frame, text=t, font="bold", background=cor).grid(row=row, column=6)


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
# fim

Example(root).pack(side="top", fill="both", expand=True)
root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
root.title('Programa Guts')
root.resizable(width=False, height=False)
root.geometry('750x450')
root.mainloop()