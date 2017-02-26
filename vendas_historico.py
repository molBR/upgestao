# encoding: utf-8

from Tkinter import *



# funcao de teste
def Teste(self):
    print("Testado")

class TelaMaior(Frame):



    def __init__(self,root):
        self.root = None

    def FazTela(self):
        #TelaMaior(root).pack(side="top", fill="both", expand=True)
        # root.iconbitmap(r'C:\Python27\DLLs\icon.ico')


        # fim

        self.root = Toplevel()

        # menu principal
        menu = Menu(self.root)
        self.root.config(menu=menu)

        subMenu1 = Menu(menu)
        menu.add_cascade(label="Menu", menu=subMenu1)
        subMenu1.add_command(label="Recarregar", command=Teste)
        subMenu1.add_separator()
        subMenu1.add_command(label="Sair", command=self.root.destroy)

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
        q = "quantidades"
        info = 71

        toolbar = Frame(self.root, bg=cor1)

        ordenar = Label(toolbar, text=" Ordenar Por:", bg=cor1, font="bold", fg="white")
        ordenar.pack(side=LEFT, pady=1)
        variable = StringVar(toolbar)
        variable.set("Nome")
        opcoes = OptionMenu(toolbar, variable, "Nome", "Data  ", "Valor ")
        opcoes.config(bg=cor1, font="white", fg="white")
        opcoes["menu"].config(bg=cor1, font="white", fg="white")
        opcoes.pack(side=LEFT)
        for espaco in range(info):
            t = " "
            Label(toolbar, text=t, bg=cor1).pack(side=LEFT)
        vendas = Label(toolbar, text="Vendas Realizadas:", bg=cor1, font="bold", fg="white")
        vendas.pack(side=LEFT, pady=10)
        quantidade = Label(toolbar, text=q, bg=cor1, font="bold", fg="white")
        quantidade.pack(side=LEFT)

        toolbar.pack(side=TOP, fill=X)
        # fim

        # barra de 'status'
        status = Label(self.root, text="Estado: Rodando", bg="white", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        # fim


        cor3='#E6E6E6'

        self.container1 = Frame(self.root)
        self.container2 = Frame(self.root, bg=cor3)
        self.container3 = Frame(self.root, bg=cor3)
        self.container4 = Frame(self.root, bg=cor3)
        self.container1.pack(fill=X)
        self.container2.pack(side=BOTTOM, fill=X)
        self.container3.pack(side=BOTTOM, fill=X)
        self.container4.pack(side=BOTTOM, fill=X)

        # "cabecalho" da tabela dos itens

        self.nome = Label(self.container1, text=" Nome:")
        self.nome["font"] = ["bold"]
        self.nome.pack(side=LEFT)
        self.pulo1 = Label(self.container1, text="                                                 ")
        self.pulo1["font"] = ["bold"]
        self.pulo1.pack(side=LEFT)
        self.data = Label(self.container1, text="Data:")
        self.data["font"] = ["bold"]
        self.data.pack(side=LEFT)
        self.pulo2 = Label(self.container1, text="                  ")
        self.pulo2["font"] = ["bold"]
        self.pulo2.pack(side=LEFT)
        self.valor = Label(self.container1, text="Valor:")
        self.valor["font"] = ["bold"]
        self.valor.pack(side=LEFT)
        self.pulo3 = Label(self.container1, text="                                ")
        self.pulo3.pack(side=LEFT)
        self.dados = Label(self.container1, text="Dados Gerais:")
        self.dados["font"] = ["bold"]
        self.dados.pack(side=LEFT)
        # fim

# espaco com "salvar docx", "excluir" e "pesquisar"

        t = "VALOR"

        self.salto1 = Label(self.container2, text="", bg=cor3)
        self.salto1.pack(side=LEFT)

        self.espaco1 = Label(self.container3, text="                                                                          ", bg=cor3)
        self.espaco1.pack(side=LEFT)
        self.pesquisar1 = Label(self.container3, text="Pesquisar: ", bg=cor3)
        self.pesquisar1["font"] = ['bold']
        self.pesquisar1.pack(side=LEFT)
        self.pesquisar2 = Entry(self.container3)
        self.pesquisar2["width"] = 25
        self.pesquisar2["font"] = ("Arial", "10")
        self.pesquisar2.pack(side=LEFT)
        self.espaco2 = Label(self.container3, text=" ", bg=cor3)
        self.espaco2.pack(side=LEFT)
        self.ok = Button(self.container3, text="Ok", command=Teste, bg=cor3)
        self.ok["font"] = ['bold']
        self.ok['padx'] = 1
        self.ok['pady'] = 1
        self.ok.pack(side=LEFT)
        self.espaco3 = Label(self.container3, text="                    ", bg=cor3)
        self.espaco3.pack(side=LEFT)
        self.salvar = Button(self.container3, text="Salvar Docx", command=Teste, bg=cor3)
        self.salvar["font"] = ['bold']
        self.salvar['padx'] = 1
        self.salvar['pady'] = 1
        self.salvar.pack(side=LEFT)
        self.espaco4 = Label(self.container3, text="                    ", bg=cor3)
        self.espaco4.pack(side=LEFT)
        self.excluir = Button(self.container3, text="Excluir", command=Teste, bg=cor3)
        self.excluir["font"] = ['bold']
        self.excluir['padx'] = 1
        self.excluir['pady'] = 1
        self.excluir.pack(side=LEFT)

        self.salto2 = Label(self.container4, text="", bg=cor3)
        self.salto2.pack(side=LEFT)
# fim

# tabela dos itens
        Frame.__init__(self, self.root)  # comeco frame dos produtos
        self.canvas1 = Canvas(self.root, borderwidth=0, background="#ffffff")
        self.frame1 = Frame(self.canvas1, background="#f0f0f0")
        self.vsb1 = Scrollbar(self.root, orient="vertical", command=self.canvas1.yview)
        self.canvas1.configure(yscrollcommand=self.vsb1.set)

        self.canvas1.pack(side="left", fill="both", expand=True)
        self.vsb1.pack(side="left", fill="y")
        self.canvas1.create_window((4, 4), window=self.frame1, anchor="nw",
                                   tags="self.frame1")

        self.frame1.bind("<Configure>", self.onFrameConfigure1)

        self.populate1()  # fim frame dos produtos

        Frame.__init__(self, self.root)  # comeco frame venda
        self.canvas2 = Canvas(self.root, borderwidth=0, background="#ffffff")
        self.frame2 = Frame(self.canvas2, background="#f0f0f0")
        self.vsb2 = Scrollbar(self.root, orient="vertical", command=self.canvas2.yview)
        self.canvas2.configure(yscrollcommand=self.vsb2.set)

        self.canvas2.pack(side="left", fill="both", expand=True)
        self.vsb2.pack(side="left", fill="y")
        self.canvas2.create_window((4, 4), window=self.frame2, anchor="nw",
                                   tags="self.frame2")

        self.frame2.bind("<Configure>", self.onFrameConfigure2)

        self.populate2()  # fim frame venda

        self.root.title('Programa Guts')
        self.root.resizable(width=False, height=False)
        self.root.geometry('1061x581')
        self.root.mainloop()




    def populate1(self):  # comeco produtos
        info = 40
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "nome"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', font="bold", width=28)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=0)
            else:
                cor = '#f0f0f0'
                t = "nome"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', font="bold", width=28)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=0)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "data"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', font="bold", width=13)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
            else:
                cor = '#f0f0f0'
                t = "data"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', font="bold", width=13)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
        for row in range(info):
            if row % 2 == 0:
                cor = '#ffffff'
                t = "R$" "  valor"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', font="bold", width=14)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
            else:
                cor = '#f0f0f0'
                t = "R$"  "  valor"
                ent = Entry(self.frame1, state='readonly', readonlybackground=cor, fg='black', font="bold", width=14)
                var = StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
                # fim produtos

    def onFrameConfigure1(self, event):  # comeco scroolbar frame1
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas1.configure(scrollregion=self.canvas1.bbox("all"))  # fim scroolbar frame1

    def populate2(self):  # comeco venda
        x = 31 #var para deixar o espaco ao lado dos dados com a mesma cor de fundo
        cor = '#fafafa'
        nada = ""
        nome1var = "Nome:"
        nome2var = "nome"
        endereco1var = "Endereco:"
        endereco2var = "endereco"
        data1var = "Data:"
        data2var = "data"
        email1var = "Email:"
        email2var = "email"
        telefone1var = "Telefone:"
        telefone2var = "telefone"
        celular1var = "Celular:"
        celular2var = "celular"
        festa1var = "Tipo de Festa:"
        festa2var = "festa"
        cliente1var = "Instituicao/Cliente:"
        cliente2var = "cliente"
        npessoas1var = "Numero de Pessoas:"
        npessoas2var = "numero pessoas"
        local1var = "Espaco/Local:"
        local2var = "local"
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
        total2var = "valor total"

        #titulo
        nome1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nome1var)
        nome1.config(textvariable=var, relief='flat')
        nome1.grid(row=0, column=0)

        #preencher cor
        for row in range (x):
            espaco1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
            var = StringVar()
            var.set(nada)
            espaco1.config(textvariable=var, relief='flat')
            espaco1.grid(row=row, column=1)

        #preencher cor
        for row in range(x):
            espaco2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
            var = StringVar()
            var.set(nada)
            espaco2.config(textvariable=var, relief='flat')
            espaco2.grid(row=row, column=2)

        #informacao
        nome2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nome2var)
        nome2.config(textvariable=var, relief='flat')
        nome2.grid(row=1, column=0)

        #espaco
        salto1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto1.config(textvariable=var, relief='flat')
        salto1.grid(row=2, column=0)

        #titulo e informacao
        endereco1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(endereco1var)
        endereco1.config(textvariable=var, relief='flat')
        endereco1.grid(row=3, column=0)
        endereco2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(endereco2var)
        endereco2.config(textvariable=var, relief='flat')
        endereco2.grid(row=4, column=0)

        #espaco
        salto2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto2.config(textvariable=var, relief='flat')
        salto2.grid(row=5, column=0)

        #titulo e informacao
        data1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(data1var)
        data1.config(textvariable=var, relief='flat')
        data1.grid(row=6, column=0)
        data2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(data2var)
        data2.config(textvariable=var, relief='flat')
        data2.grid(row=7, column=0)

        #espaco
        salto3 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto3.config(textvariable=var, relief='flat')
        salto3.grid(row=8, column=0)

        #titulo e informacao
        email1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(email1var)
        email1.config(textvariable=var, relief='flat')
        email1.grid(row=9, column=0)
        email2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(email2var)
        email2.config(textvariable=var, relief='flat')
        email2.grid(row=10, column=0)

        #espaco
        salto4 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto4.config(textvariable=var, relief='flat')
        salto4.grid(row=11, column=0)

        #titulo e informacao
        telefone1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(telefone1var)
        telefone1.config(textvariable=var, relief='flat')
        telefone1.grid(row=12, column=0)
        telefone2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(telefone2var)
        telefone2.config(textvariable=var, relief='flat')
        telefone2.grid(row=13, column=0)

        #espaco
        salto5 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto5.config(textvariable=var, relief='flat')
        salto5.grid(row=14, column=0)

        #titulo e informacao
        celular1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(celular1var)
        celular1.config(textvariable=var, relief='flat')
        celular1.grid(row=15, column=0)
        celular2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(celular2var)
        celular2.config(textvariable=var, relief='flat')
        celular2.grid(row=16, column=0)

        #espaco
        salto6 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto6.config(textvariable=var, relief='flat')
        salto6.grid(row=17, column=0)

        #titulo e informacao
        festa1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(festa1var)
        festa1.config(textvariable=var, relief='flat')
        festa1.grid(row=18, column=0)
        festa2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(festa2var)
        festa2.config(textvariable=var, relief='flat')
        festa2.grid(row=19, column=0)

        #espaco
        salto7 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto7.config(textvariable=var, relief='flat')
        salto7.grid(row=20, column=0)

        #titulo e informacao
        cliente1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(cliente1var)
        cliente1.config(textvariable=var, relief='flat')
        cliente1.grid(row=21, column=0)
        cliente2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(cliente2var)
        cliente2.config(textvariable=var, relief='flat')
        cliente2.grid(row=22, column=0)

        #espaco
        salto8 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto8.config(textvariable=var, relief='flat')
        salto8.grid(row=23, column=0)

        #titulo e informacao
        npessoas1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(npessoas1var)
        npessoas1.config(textvariable=var, relief='flat')
        npessoas1.grid(row=24, column=0)
        npessoas2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(npessoas2var)
        npessoas2.config(textvariable=var, relief='flat')
        npessoas2.grid(row=25, column=0)

        #espaco
        salto9 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto9.config(textvariable=var, relief='flat')
        salto9.grid(row=26, column=0)

        #titulo e informacao
        local1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(local1var)
        local1.config(textvariable=var, relief='flat')
        local1.grid(row=27, column=0)
        local2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(local2var)
        local2.config(textvariable=var, relief='flat')
        local2.grid(row=28, column=0)

        #espaco
        salto10 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto10.config(textvariable=var, relief='flat')
        salto10.grid(row=29, column=0)

        #titulo
        produtos = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(produtosvar)
        produtos.config(textvariable=var, relief='flat')
        produtos.grid(row=30, column=0)

        #titulo
        nome = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(NOME)
        nome.config(textvariable=var, relief='flat')
        nome.grid(row=31, column=0)
        quantidade = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(QUANTIDADE)
        quantidade.config(textvariable=var, relief='flat')
        quantidade.grid(row=31, column=1)
        valor = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(VALOR)
        valor.config(textvariable=var, relief='flat')
        valor.grid(row=31, column=2)

        #espaco
        salto11 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto11.config(textvariable=var, relief='flat')
        salto11.grid(row=32, column=0)
        espaco3 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(nada)
        espaco3.config(textvariable=var, relief='flat')
        espaco3.grid(row=32, column=1)
        espaco4 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(nada)
        espaco4.config(textvariable=var, relief='flat')
        espaco4.grid(row=32, column=2)

        #exemplo de como vai ficar as informacoes 519/858
        doces = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(docesvar)
        doces.config(textvariable=var, relief='flat')
        doces.grid(row=33, column=0)

        espaco5 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(nada)
        espaco5.config(textvariable=var, relief='flat')
        espaco5.grid(row=33, column=1)

        espaco6 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(nada)
        espaco6.config(textvariable=var, relief='flat')
        espaco6.grid(row=33, column=2)

        doce1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(produtonome)
        doce1.config(textvariable=var, relief='flat')
        doce1.grid(row=34, column=0)
        docequant1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(produtoquant)
        docequant1.config(textvariable=var, relief='flat')
        docequant1.grid(row=34, column=1)
        docevalor1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(produtovalor)
        docevalor1.config(textvariable=var, relief='flat')
        docevalor1.grid(row=34, column=2)

        doce2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(produtonome)
        doce2.config(textvariable=var, relief='flat')
        doce2.grid(row=35, column=0)
        docequant2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(produtoquant)
        docequant2.config(textvariable=var, relief='flat')
        docequant2.grid(row=35, column=1)
        docevalor2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(produtovalor)
        docevalor2.config(textvariable=var, relief='flat')
        docevalor2.grid(row=35, column=2)

        doce3 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(produtonome)
        doce3.config(textvariable=var, relief='flat')
        doce3.grid(row=36, column=0)
        docequant3 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(produtoquant)
        docequant3.config(textvariable=var, relief='flat')
        docequant3.grid(row=36, column=1)
        docevalor3 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(produtovalor)
        docevalor3.config(textvariable=var, relief='flat')
        docevalor3.grid(row=36, column=2)

        doce4 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(produtonome)
        doce4.config(textvariable=var, relief='flat')
        doce4.grid(row=37, column=0)
        docequant4 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(produtoquant)
        docequant4.config(textvariable=var, relief='flat')
        docequant4.grid(row=37, column=1)
        docevalor4 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(produtovalor)
        docevalor4.config(textvariable=var, relief='flat')
        docevalor4.grid(row=37, column=2)

        salto12 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto12.config(textvariable=var, relief='flat')
        salto12.grid(row=38, column=0)

        espaco7 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(nada)
        espaco7.config(textvariable=var, relief='flat')
        espaco7.grid(row=38, column=1)

        espaco8 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(nada)
        espaco8.config(textvariable=var, relief='flat')
        espaco8.grid(row=38, column=2)

        salgados = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(salgadosvar)
        salgados.config(textvariable=var, relief='flat')
        salgados.grid(row=39, column=0)

        espaco9 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(nada)
        espaco9.config(textvariable=var, relief='flat')
        espaco9.grid(row=39, column=1)

        espaco10 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(nada)
        espaco10.config(textvariable=var, relief='flat')
        espaco10.grid(row=39, column=2)

        salgado1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(produtonome)
        salgado1.config(textvariable=var, relief='flat')
        salgado1.grid(row=40, column=0)
        salgadoquant1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(produtoquant)
        salgadoquant1.config(textvariable=var, relief='flat')
        salgadoquant1.grid(row=40, column=1)
        salgadovalor1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(produtovalor)
        salgadovalor1.config(textvariable=var, relief='flat')
        salgadovalor1.grid(row=40, column=2)

        salgado2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(produtonome)
        salgado2.config(textvariable=var, relief='flat')
        salgado2.grid(row=41, column=0)
        salgadoquant2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(produtoquant)
        salgadoquant2.config(textvariable=var, relief='flat')
        salgadoquant2.grid(row=41, column=1)
        salgadovalor2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(produtovalor)
        salgadovalor2.config(textvariable=var, relief='flat')
        salgadovalor2.grid(row=41, column=2)

        salgado3 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(produtonome)
        salgado3.config(textvariable=var, relief='flat')
        salgado3.grid(row=42, column=0)
        salgadoquant3 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(produtoquant)
        salgadoquant3.config(textvariable=var, relief='flat')
        salgadoquant3.grid(row=42, column=1)
        salgadovalor3 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(produtovalor)
        salgadovalor3.config(textvariable=var, relief='flat')
        salgadovalor3.grid(row=42, column=2)

        salto13 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto13.config(textvariable=var, relief='flat')
        salto13.grid(row=43, column=0)

        espaco11 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(nada)
        espaco11.config(textvariable=var, relief='flat')
        espaco11.grid(row=43, column=1)

        espaco12 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(nada)
        espaco12.config(textvariable=var, relief='flat')
        espaco12.grid(row=43, column=2)

        massas = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(massasvar)
        massas.config(textvariable=var, relief='flat')
        massas.grid(row=44, column=0)

        espaco13 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(nada)
        espaco13.config(textvariable=var, relief='flat')
        espaco13.grid(row=44, column=1)

        espaco14 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(nada)
        espaco14.config(textvariable=var, relief='flat')
        espaco14.grid(row=44, column=2)

        massa1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(produtonome)
        massa1.config(textvariable=var, relief='flat')
        massa1.grid(row=45, column=0)
        massaquant1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(produtoquant)
        massaquant1.config(textvariable=var, relief='flat')
        massaquant1.grid(row=45, column=1)
        massavalor1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(produtovalor)
        massavalor1.config(textvariable=var, relief='flat')
        massavalor1.grid(row=45, column=2)

        massa2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(produtonome)
        massa2.config(textvariable=var, relief='flat')
        massa2.grid(row=46, column=0)
        massaquant2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(produtoquant)
        massaquant2.config(textvariable=var, relief='flat')
        massaquant2.grid(row=46, column=1)
        massavalor2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(produtovalor)
        massavalor2.config(textvariable=var, relief='flat')
        massavalor2.grid(row=46, column=2)

        salto14 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto14.config(textvariable=var, relief='flat')
        salto14.grid(row=47, column=0)

        espaco15 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(nada)
        espaco15.config(textvariable=var, relief='flat')
        espaco15.grid(row=47, column=1)

        espaco16 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(nada)
        espaco16.config(textvariable=var, relief='flat')
        espaco16.grid(row=47, column=2)

        bebidas = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(bebidasvar)
        bebidas.config(textvariable=var, relief='flat')
        bebidas.grid(row=48, column=0)

        espaco17 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(nada)
        espaco17.config(textvariable=var, relief='flat')
        espaco17.grid(row=48, column=1)

        espaco18 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(nada)
        espaco18.config(textvariable=var, relief='flat')
        espaco18.grid(row=48, column=2)

        bebida1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(produtonome)
        bebida1.config(textvariable=var, relief='flat')
        bebida1.grid(row=49, column=0)
        bebidaquant1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(produtoquant)
        bebidaquant1.config(textvariable=var, relief='flat')
        bebidaquant1.grid(row=49, column=1)
        bebidavalor1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(produtovalor)
        bebidavalor1.config(textvariable=var, relief='flat')
        bebidavalor1.grid(row=49, column=2)

        salto15 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto15.config(textvariable=var, relief='flat')
        salto15.grid(row=50, column=0)

        espaco19 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(nada)
        espaco19.config(textvariable=var, relief='flat')
        espaco19.grid(row=50, column=1)

        espaco20 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(nada)
        espaco20.config(textvariable=var, relief='flat')
        espaco20.grid(row=50, column=2)

        outros = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(outrosvar)
        outros.config(textvariable=var, relief='flat')
        outros.grid(row=51, column=0)

        espaco21 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(nada)
        espaco21.config(textvariable=var, relief='flat')
        espaco21.grid(row=51, column=1)

        espaco22 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(nada)
        espaco22.config(textvariable=var, relief='flat')
        espaco22.grid(row=51, column=2)

        salto16 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(nada)
        salto16.config(textvariable=var, relief='flat')
        salto16.grid(row=52, column=0)

        espaco23 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(nada)
        espaco23.config(textvariable=var, relief='flat')
        espaco23.grid(row=52, column=1)

        espaco24 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(nada)
        espaco24.config(textvariable=var, relief='flat')
        espaco24.grid(row=52, column=2)

        #titulo e informacao
        total1 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(total1var)
        total1.config(textvariable=var, relief='flat')
        total1.grid(row=53, column=0)
        total2 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=33)
        var = StringVar()
        var.set(total2var)
        total2.config(textvariable=var, relief='flat')
        total2.grid(row=54, column=0)

        #preencher cor
        espaco25 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(nada)
        espaco25.config(textvariable=var, relief='flat')
        espaco25.grid(row=53, column=1)

        espaco26 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(nada)
        espaco26.config(textvariable=var, relief='flat')
        espaco26.grid(row=53, column=2)

        espaco27 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=10)
        var = StringVar()
        var.set(nada)
        espaco27.config(textvariable=var, relief='flat')
        espaco27.grid(row=54, column=1)

        espaco28 = Entry(self.frame2, state='readonly', readonlybackground=cor, fg='black', font="bold", width=12)
        var = StringVar()
        var.set(nada)
        espaco28.config(textvariable=var, relief='flat')
        espaco28.grid(row=54, column=2)

    def onFrameConfigure2(self, event):  # comeco scroolbar frame2
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas2.configure(scrollregion=self.canvas2.bbox("all"))  # fim scroolbar frame2
# fim
