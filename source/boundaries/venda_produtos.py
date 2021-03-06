# encoding: utf-8

import Tkinter as tk
import os as os
import tkMessageBox
from datetime import datetime

from source.entities import database as db
from source.entities import tratamentos as tr
from source.entities import venda as ve
import venda_produtos_menor as vpm


# funcao de teste
def Teste():
    print("Testado")


# fim

# funcao de destaque das abas
# fim

#Classe que define os produtos selecionados na venda juntamente com sua quantidade
class SelectedProd:

    def __init__(self, prodInfo, quant):
        self.prodInfo = prodInfo
        self.quant = tk.IntVar()
        self.quant.set(quant)


    def getprodInfo(self):
        return self.prodInfo

    def getQuant(self):
        return self.quant

class VendProd(tk.Frame):
    def __init__(self, parent, controller,Cliente,Venda):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bd = db.Database()
        self.SomaQuant = tk.StringVar()
        self.fechaTela = tk.FALSE
        self.resetValues()
        self.FazTela()
        self.Cliente = Cliente
        self.Venda = Venda
        self.vpm = vpm.Application()


    def insereTudo(self):
        agora = datetime.now().strftime('%d/%m/%y - %H:%M:%S')
        if(not self.listaSelec):
           pass
        else:
            self.calculaTotal()
            v1 = ve.Venda(0,self.Cliente.getId(),self.Cliente.getNome(),self.TipoEvento.getTipo(),self.TipoEvento.getAdultos(),
                          self.TipoEvento.getCriancas(),self.TipoEvento.getRua(),self.Cliente.getTelefone(),
                          self.Cliente.getEmail(),self.TipoEvento.getData(),agora,self.SomaQuant,self.SomaQuant,
                          self.SomaQuant,self.SomaQuant)
            self.vpm.FazTela(self.bd, v1,self.controller)
            if (self.vpm.GetWindow() != None):
                self.vpm.GetWindow().wait_window()
            vend_id = self.bd.selectLastIdVenda()
            for i in range(len(self.listaSelec)):
                self.bd.insertProdVend(self.listaSelec[i].getprodInfo()[1],
                                       self.listaSelec[i].getprodInfo()[2],
                                       self.listaSelec[i].getQuant().get(),
                                       vend_id,
                                       self.listaSelec[i].getprodInfo()[4])




    def setCE(self,Cliente,TipoEvento):
        self.Cliente = Cliente
        self.TipoEvento = TipoEvento

    def resetValues(self):
        self.listaProduto = []
        self.listaProduto = self.bd.selectProduto()

        self.listaSelec = []
        self.SomaQuant.set('0,00')

    def todos_apertado(self):
        self.todos.config(relief=tk.SUNKEN, background=self.cor2)
        self.doces.config(relief=tk.RAISED, background=self.cor1)
        self.salgados.config(relief=tk.RAISED, background=self.cor1)
        self.massas.config(relief=tk.RAISED, background=self.cor1)
        self.bebidas.config(relief=tk.RAISED, background=self.cor1)
        self.outros.config(relief=tk.RAISED, background=self.cor1)
        self.populate1(self.trataLista(self.bd.selectProduto()))
        self.populate2(self.listaSelec)

    def doces_apertado(self):
        self.todos.config(relief=tk.RAISED, background=self.cor1)
        self.doces.config(relief=tk.SUNKEN, background=self.cor2)
        self.salgados.config(relief=tk.RAISED, background=self.cor1)
        self.massas.config(relief=tk.RAISED, background=self.cor1)
        self.bebidas.config(relief=tk.RAISED, background=self.cor1)
        self.outros.config(relief=tk.RAISED, background=self.cor1)
        self.populate1(self.trataLista(self.bd.selectProdutoDoces()))
        self.populate2(self.listaSelec)

    def salgados_apertado(self):
        self.todos.config(relief=tk.RAISED, background=self.cor1)
        self.doces.config(relief=tk.RAISED, background=self.cor1)
        self.salgados.config(relief=tk.SUNKEN, background=self.cor2)
        self.massas.config(relief=tk.RAISED, background=self.cor1)
        self.bebidas.config(relief=tk.RAISED, background=self.cor1)
        self.outros.config(relief=tk.RAISED, background=self.cor1)
        self.populate1(self.trataLista(self.bd.selectProdutoSalgados()))
        self.populate2(self.listaSelec)

    def massas_apertado(self):
        self.todos.config(relief=tk.RAISED, background=self.cor1)
        self.doces.config(relief=tk.RAISED, background=self.cor1)
        self.salgados.config(relief=tk.RAISED, background=self.cor1)
        self.massas.config(relief=tk.SUNKEN, background=self.cor2)
        self.bebidas.config(relief=tk.RAISED, background=self.cor1)
        self.outros.config(relief=tk.RAISED, background=self.cor1)
  #      self.tipos.config(relief=tk.RAISED, background=self.cor1)
        self.populate1(self.trataLista(self.bd.selectProdutoMassas()))
        self.populate2(self.listaSelec)

    def bebidas_apertado(self):
        self.todos.config(relief=tk.RAISED, background=self.cor1)
        self.doces.config(relief=tk.RAISED, background=self.cor1)
        self.salgados.config(relief=tk.RAISED, background=self.cor1)
        self.massas.config(relief=tk.RAISED, background=self.cor1)
        self.bebidas.config(relief=tk.SUNKEN, background=self.cor2)
        self.outros.config(relief=tk.RAISED, background=self.cor1)
        self.populate1(self.trataLista(self.bd.selectProdutoBebidas()))
        self.populate2(self.listaSelec)

    def outros_apertado(self):
        self.todos.config(relief=tk.RAISED, background=self.cor1)
        self.doces.config(relief=tk.RAISED, background=self.cor1)
        self.salgados.config(relief=tk.RAISED, background=self.cor1)
        self.massas.config(relief=tk.RAISED, background=self.cor1)
        self.bebidas.config(relief=tk.RAISED, background=self.cor1)
        self.outros.config(relief=tk.SUNKEN, background=self.cor2)
        self.populate1(self.trataLista(self.bd.selectProdutoOutros()))
        self.populate2(self.listaSelec)


    def trataLista(self, commandBD):
        self.listaProduto = commandBD
        if (self.listaSelec):
            aux = len(self.listaProduto) - 1
            percorre = 0
            while (percorre <= aux):
                for j in range(len(self.listaSelec)):
                    try:
                        if (self.listaProduto[percorre][0] == self.listaSelec[j].getprodInfo()[0]):
                        #if self.listaSelec[j].getprodInfo() in self.listaProduto:
                            self.listaProduto.pop(percorre)
                            aux = aux - 1
                    except IndexError:
                        pass
                percorre = percorre + 1
        return self.listaProduto

    def pesquisando(self, id):
        if id == "":
            self.populate1(self.trataLista(self.bd.selectProduto()))
            self.populate2(self.listaSelec)
            return
        else:
            try:
                tr.VerificaDigit(id)
            except Exception as e:
                tkMessageBox.showerror("Erro encontrado", e.message)
            else:
                # self.todos_apertado()
                self.populate1(self.trataLista(self.bd.selectProdutoIdAll(id)))
                self.populate2(self.listaSelec)

    def calculaTotal(self):
        print "oi"
        valorTot = 0
        if(self.listaSelec):
            for i in range(len(self.listaSelec)):
                auxProdValue = tr.swapComma2Dot(self.listaSelec[i].getprodInfo()[2])
                valorTot = valorTot + float(auxProdValue) * int(self.listaSelec[i].getQuant().get())
            valorTot = "%.2f" % round(valorTot,2) #arredondar com 2 casas decimais. OBRIGADO STACKOVERFLOW
        valorTot = tr.swapDot2Comma(valorTot)
        self.SomaQuant.set(valorTot)


    def FazTela(self):
        # menu
        toolbar1 = tk.Frame(self, bg="white")

        self.menu = tk.Button(toolbar1, text="   Menu Inicial ", bg="white", relief=tk.FLAT,
                              command=lambda: self.controller.show_frame("menuInicial"))
        self.menu["font"] = ("Arial", "10")
        self.menu.pack(side=tk.LEFT)
        self.espaco1 = tk.Label(toolbar1, text=" | ", bg="white")
        self.espaco1["font"] = ("Arial", "12")
        self.espaco1.pack(side=tk.LEFT)
        self.novavenda = tk.Button(toolbar1, text="Nova Venda", bg="light gray", relief=tk.FLAT)
        self.novavenda["font"] = ("Arial", "10")
        self.novavenda.pack(side=tk.LEFT, padx=1, pady=1)
        self.espaco2 = tk.Label(toolbar1, text=" | ", bg="white")
        self.espaco2["font"] = ("Arial", "12")
        self.espaco2.pack(side=tk.LEFT)
        self.cadastrarcliente = tk.Button(toolbar1, text="Cadastrar Cliente", bg="white", relief=tk.FLAT,
                                          command=lambda: self.controller.show_frame("cadClientMaior"))
        self.cadastrarcliente["font"] = ("Arial", "10")
        self.cadastrarcliente.pack(side=tk.LEFT, padx=1, pady=1)
        self.espaco3 = tk.Label(toolbar1, text=" | ", bg="white")
        self.espaco3["font"] = ("Arial", "12")
        self.espaco3.pack(side=tk.LEFT)

        toolbar1.pack(side=tk.TOP, fill=tk.X)
        # fim


        # barra de 'status'
        status = tk.Label(self, text="Estado: Executando", bg="white", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status.pack(side=tk.BOTTOM, fill=tk.X)
        # fim


        # abas de opcoes
        self.cor1 = '#D32F2F'
        self.cor2 = '#E94545'

        toolbar2 = tk.Frame(self, bg=self.cor1)

        self.todos = tk.Button(toolbar2, text="   Todos   ", bg=self.cor1, command=self.todos_apertado)
        self.todos["font"] = ("Arial", "12")
        self.todos['fg'] = 'white'
        self.todos.pack(side=tk.LEFT, padx=1, pady=1)
        self.doces = tk.Button(toolbar2, text="   Doces   ", bg=self.cor1, command=self.doces_apertado)
        self.doces["font"] = ("Arial", "12")
        self.doces['fg'] = 'white'
        self.doces.pack(side=tk.LEFT, padx=1, pady=1)
        self.salgados = tk.Button(toolbar2, text="Salgados", bg=self.cor1, command=self.salgados_apertado)
        self.salgados["font"] = ("Arial", "12")
        self.salgados['fg'] = 'white'
        self.salgados.pack(side=tk.LEFT, padx=1, pady=1)
        self.massas = tk.Button(toolbar2, text="  Massas  ", bg=self.cor1, command=self.massas_apertado)
        self.massas["font"] = ("Arial", "12")
        self.massas['fg'] = 'white'
        self.massas.pack(side=tk.LEFT, padx=1, pady=1)
        self.bebidas = tk.Button(toolbar2, text=" Bebidas ", bg=self.cor1, command=self.bebidas_apertado)
        self.bebidas["font"] = ("Arial", "12")
        self.bebidas['fg'] = 'white'
        self.bebidas.pack(side=tk.LEFT, padx=1, pady=1)
        self.outros = tk.Button(toolbar2, text="   Outros   ", bg=self.cor1, command=self.outros_apertado)
        self.outros["font"] = ("Arial", "12")
        self.outros['fg'] = 'white'
        self.outros.pack(side=tk.LEFT, padx=1, pady=1)
        #Apagar se der certo!
        #self.tipos = tk.Button(toolbar2, text="   Tipos   ", bg=self.cor1, command=self.tipos_apertado)
        #self.tipos["font"] = ("Arial", "12")
        #self.tipos['fg'] = 'white'
        #self.tipos.pack(side=tk.LEFT, padx=1, pady=1)

        toolbar2.pack(side=tk.TOP, fill=tk.X)
        # fim

        self.cor3 = '#E6E6E6'

        self.container1 = tk.Frame(self)
        self.frameProd = tk.Frame(self)
        self.container2 = tk.Frame(self, bg=self.cor3)
        self.container3 = tk.Frame(self, bg=self.cor3)
        self.container4 = tk.Frame(self, bg=self.cor3)
        self.container1.pack(side=tk.TOP, fill=tk.X)
        self.frameProd.pack(side=tk.BOTTOM, fill=tk.X)
        self.container2.pack(side=tk.BOTTOM, fill=tk.X)
        self.container3.pack(side=tk.BOTTOM, fill=tk.X)
        self.container4.pack(side=tk.BOTTOM, fill=tk.X)

        # "cabecalho" da tabela dos itens
        self.objeto1 = tk.Label(self.container1, text="Cod\t")
        self.objeto1["font"] = ["bold"]
        self.objeto1.pack(side=tk.LEFT)
        self.objeto2 = tk.Label(self.container1, text="\t")
        self.objeto2["font"] = ["bold"]
        self.objeto2.pack(side=tk.LEFT)
        self.objeto3 = tk.Label(self.container1, text="Nome")
        self.objeto3["font"] = ["bold"]
        self.objeto3.pack(side=tk.LEFT)
        t = "                            " #quando a distancia, multiplica-se por t
        for i in range(0,2):
            t = t + t
        self.objeto4 = tk.Label(self.container1, text=t)
        self.objeto4["font"] = ["bold"]
        self.objeto4.pack(side=tk.LEFT)
        self.objeto5 = tk.Label(self.container1, text="Valor")
        self.objeto5["font"] = ["bold"]
        self.objeto5.pack(side=tk.LEFT)
        self.objeto6 = tk.Label(self.container1, text="                                        ")
        self.objeto6["font"] = ["bold"]
        self.objeto6.pack(side=tk.LEFT)
        self.objeto7 = tk.Label(self.container1, text="Nome")
        self.objeto7["font"] = ["bold"]
        self.objeto7.pack(side=tk.LEFT)
        t = "                         "  # quando a distancia, multiplica-se por t
        for i in range(0,2):
            t=t+t
        self.objeto8 = tk.Label(self.container1, text=t)
        self.objeto8["font"] = ["bold"]
        self.objeto8.pack(side=tk.LEFT)
        self.objeto9 = tk.Label(self.container1, text="Valor")
        self.objeto9["font"] = ["bold"]
        self.objeto9.pack(side=tk.LEFT)
        self.objeto10 = tk.Label(self.container1, text=" ")
        self.objeto10["font"] = ["bold"]
        self.objeto10.pack(side=tk.LEFT)
        self.objeto11 = tk.Label(self.container1, text="Quantidade")
        self.objeto11["font"] = ["bold"]
        self.objeto11.pack(side=tk.LEFT)
        # fim

        # tabela dos itens

        # comeco frame dos produtos
        self.canvas1 = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame1 = tk.Frame(self.canvas1, background="#f0f0f0")
        self.vsb1 = tk.Scrollbar(self, orient="vertical", command=self.canvas1.yview)
        self.canvas1.configure(yscrollcommand=self.vsb1.set)

        self.vsb1.pack(side=tk.RIGHT, fill="y")
        self.canvas1.pack(side=tk.LEFT, fill="both", expand=True)
        self.canvas1.create_window((4, 4), window=self.frame1, anchor="nw",
                                   tags="self.frame1")

        self.frame1.bind("<Configure>", self.onFrameConfigure1)

        self.pacote1 = [self.canvas1, self.frame1, self.vsb1, "self.frame1", self.onFrameConfigure1]
        self.populate1(self.listaProduto)
        # fim frame dos produtos

        # comeco frame venda
        self.canvas2 = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame2 = tk.Frame(self.canvas2, background="#f0f0f0")
        self.vsb2 = tk.Scrollbar(self, orient="vertical", command=self.canvas2.yview)
        self.canvas2.configure(yscrollcommand=self.vsb2.set)

        self.canvas2.pack(side="left", fill="both", expand=True)
        self.vsb2.pack(side="right", fill="y")
        self.canvas2.create_window((4, 4), window=self.frame2, anchor="nw",
                                   tags="self.frame2")

        self.frame2.bind("<Configure>", self.onFrameConfigure2)

        self.pacote2 = [self.canvas2, self.frame2, self.vsb2, "self.frame2", self.onFrameConfigure2]
        self.todos_apertado()
        self.populate2(self.listaSelec)
        # fim frame dos produtos

        # espaco com "inserir", "editar", "excluir" e "pesquisar"

        # t = "VALOR"

        self.salto1 = tk.Label(self.container2, text="", bg=self.cor3)
        self.salto1.pack(side=tk.LEFT)

        self.espaco1 = tk.Label(self.container3, text="               ", bg=self.cor3)
        self.espaco1.pack(side=tk.LEFT)
        self.voltar = tk.Button(self.container3, text="Voltar", command=lambda: self.controller.show_frame('vendEvent'), bg=self.cor3)
        self.voltar["font"] = ['bold']
        self.voltar['padx'] = 1
        self.voltar['pady'] = 1
        self.voltar.pack(side=tk.LEFT)
        self.espaco2 = tk.Label(self.container3, text="           ", bg=self.cor3)
        self.espaco2.pack(side=tk.LEFT)
        self.pesquisar1 = tk.Label(self.container3, text="Pesquisar: ", bg=self.cor3)
        self.pesquisar1["font"] = ['bold']
        self.pesquisar1.pack(side=tk.LEFT)
        self.pesquisar2 = tk.Entry(self.container3)
        self.pesquisar2["width"] = 25
        self.pesquisar2["font"] = ("Arial", "10")
        self.pesquisar2.pack(side=tk.LEFT)
        self.espaco3 = tk.Label(self.container3, text=" ", bg=self.cor3)
        self.espaco3.pack(side=tk.LEFT)
        self.ok = tk.Button(self.container3, text="Ok", command=lambda: self.pesquisando(self.pesquisar2.get()),
                            bg=self.cor3)
        self.ok["font"] = ['bold']
        self.ok['padx'] = 1
        self.ok['pady'] = 1
        self.ok.pack(side=tk.LEFT)
        self.espaco4 = tk.Label(self.container3, text="                     ", bg=self.cor3)
        self.espaco4.pack(side=tk.LEFT)
        # self.remover = tk.Button(self.container3, text="Remover", command=lambda:self.RemoveCheck(), bg=self.cor3)
        # self.remover["font"] = ['bold']
        # self.remover['padx'] = 1
        # self.remover['pady'] = 1
        # self.remover.pack(side=tk.LEFT)
        self.espaco5 = tk.Label(self.container3, text="                             ", bg=self.cor3)
        self.espaco5.pack(side=tk.LEFT)
        self.total1 = tk.Label(self.container3, text="Total: ", bg=self.cor3)
        self.total1["font"] = ['bold']
        self.total1.pack(side=tk.LEFT)
        self.total2 = tk.Label(self.container3, textvariable=self.SomaQuant, bg=self.cor3)

        self.total2["font"] = ['bold']
        self.total2.pack(side=tk.LEFT)
        self.photo = tk.PhotoImage(file= os.getcwd() + "/source/images/repeat.gif")
        self.calcular = tk.Button(self.container3, width=20, height=20, image=self.photo, relief=tk.FLAT, command=lambda:self.calculaTotal())
        self.calcular.pack(side=tk.LEFT)
        self.calcular.image = self.photo
        self.espaco6 = tk.Label(self.container3, text="                             ", bg=self.cor3)
        self.espaco6.pack(side=tk.LEFT)
        self.continuar = tk.Button(self.container3, text="Continuar", command=lambda:self.insereTudo(), bg=self.cor3)
        self.continuar["font"] = ['bold']
        self.continuar['padx'] = 1
        self.continuar['pady'] = 1
        self.continuar.pack(side=tk.LEFT)

        self.salto2 = tk.Label(self.container4, text="", bg=self.cor3)
        self.salto2.pack(side=tk.LEFT)

    # fim

    def deleteCanvas(self, pacote):
        if pacote[0] != None:
            pacote[0].destroy()
            pacote[1].destroy()
            pacote[2].destroy()
            pacote[0] = None
        return

    #  self.pacote1 = [self.canvas1,self.frame1,self.vsb1]
    def createCanvas(self, pacote):
        # Frame.__init__(self, self.root)
        pacote[0] = tk.Canvas(self, borderwidth=0, background="#ffffff")
        pacote[1] = tk.Frame(pacote[0], background="#f0f0f0")
        pacote[2] = tk.Scrollbar(self, orient="vertical", command=pacote[0].yview)
        pacote[0].configure(yscrollcommand=pacote[2].set)

        pacote[0].pack(side="left", fill="both", expand=True)
        pacote[2].pack(side="left", fill="y")
        pacote[0].create_window((4, 4), window=pacote[1], anchor="nw",
                                tags=pacote[3])
        pacote[1].bind("<Configure>", pacote[4])


    def populate1(self, info):  # comeco produtos
        self.deleteCanvas(self.pacote1)
        self.createCanvas(self.pacote1)
        # self.listaCheckbox = []
        photo1 = tk.PhotoImage(file=os.getcwd() + "/source/images/arrow.gif")
        if (info != None):

            for row in range(len(info)):
                if row % 2 == 0:
                    cor = '#ffffff'
                    t = info[row][0]
                    ent = tk.Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=4)
                    ent["font"] = ("Arial", "13")
                    var = tk.StringVar()
                    var.set(t)
                    ent.config(textvariable=var, relief='flat')
                    ent.grid(row=row, column=1)
                else:
                    cor = '#f0f0f0'
                    t = info[row][0]
                    ent = tk.Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=4)
                    ent["font"] = ("Arial", "13")
                    var = tk.StringVar()
                    var.set(t)
                    ent.config(textvariable=var, relief='flat')
                    ent.grid(row=row, column=1)
            for row in range(len(info)):
                if row % 2 == 0:
                    cor = '#ffffff'
                    t = info[row][1]
                    ent = tk.Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=55)
                    ent["font"] = ("Arial", "13")
                    var = tk.StringVar()
                    var.set(t)
                    ent.config(textvariable=var, relief='flat')
                    ent.grid(row=row, column=2)
                else:
                    cor = '#f0f0f0'
                    t = info[row][1]
                    ent = tk.Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=55)
                    ent["font"] = ("Arial", "13")
                    var = tk.StringVar()
                    var.set(t)
                    ent.config(textvariable=var, relief='flat')
                    ent.grid(row=row, column=2)
            for row in range(len(info)):
                if row % 2 == 0:
                    cor = '#ffffff'
                    t = info[row][2]
                    ent = tk.Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=10)
                    ent["font"] = ("Arial", "13")
                    var = tk.StringVar()
                    var.set(t)
                    ent.config(textvariable=var, relief='flat')
                    ent.grid(row=row, column=3)
                else:
                    cor = '#f0f0f0'
                    t = info[row][2]
                    ent = tk.Entry(self.pacote1[1], state='readonly', readonlybackground=cor, fg='black', width=10)
                    ent["font"] = ("Arial", "13")
                    var = tk.StringVar()
                    var.set(t)
                    ent.config(textvariable=var, relief='flat')
                    ent.grid(row=row, column=3)
            for row in range(len(info)):
                button1 = tk.Button(self.pacote1[1], width=20, height=20, image=photo1, relief=tk.FLAT,
                                    command=lambda row=row: self.selecionaProduto(row))
                button1.grid(row=row, column=4)
                button1.image = photo1
                # fim produtos

    def selecionaProduto(self, row):
        auxSelectedProd = SelectedProd(self.listaProduto[row], 1)
        self.listaSelec.append(auxSelectedProd)
        self.listaSelec = tr.mergeSort(self.listaSelec)
        self.calculaTotal()
        self.populate1(self.trataLista(self.bd.selectProduto()))
        self.populate2(self.listaSelec)

    def onFrameConfigure1(self, event):  # comeco scroolbar frame1
        '''Reset the scroll region to encompass the inner frame'''
        self.pacote1[0].configure(scrollregion=self.pacote1[0].bbox("all"))  # fim scroolbar frame1

    def populate2(self, info):  # comeco venda
        self.deleteCanvas(self.pacote2)
        self.createCanvas(self.pacote2)

        self.listQuant = []

        photo2 = tk.PhotoImage(file=os.getcwd() + "/source/images/x.gif")
        if (info != None):
            for row in range(len(info)):
                if row % 2 == 0:
                    cor = '#ffffff'
                    t = info[row].getprodInfo()[1]
                    ent = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', width=50)
                    ent["font"] = ("Arial", "13")
                    var = tk.StringVar()
                    var.set(t)
                    ent.config(textvariable=var, relief='flat')
                    ent.grid(row=row, column=1)
                else:
                    cor = '#f0f0f0'
                    t = info[row].getprodInfo()[1]
                    ent = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', width=50)
                    ent["font"] = ("Arial", "13")
                    var = tk.StringVar()
                    var.set(t)
                    ent.config(textvariable=var, relief='flat')
                    ent.grid(row=row, column=1)
            for row in range(len(info)):
                if row % 2 == 0:
                    cor = '#ffffff'
                    t = info[row].getprodInfo()[2]
                    ent = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', width=5)
                    ent["font"] = ("Arial", "13")
                    var = tk.StringVar()
                    var.set(t)
                    ent.config(textvariable=var, relief='flat')
                    ent.grid(row=row, column=2)
                else:
                    cor = '#f0f0f0'
                    t = info[row].getprodInfo()[2]
                    ent = tk.Entry(self.pacote2[1], state='readonly', readonlybackground=cor, fg='black', width=5)
                    ent["font"] = ("Arial", "13")
                    var = tk.StringVar()
                    var.set(t)
                    ent.config(textvariable=var, relief='flat')
                    ent.grid(row=row, column=2)
            for row in range(len(info)):
                var = self.listaSelec[row].getQuant()
                ent1 = tk.Entry(self.pacote2[1])
                ent1.config(textvariable=var, relief='flat')
                ent1.grid(row=row, column=3)
                if row % 2 == 0:
                    cor = '#ffffff'
                else:
                    cor = '#f0f0f0'

            for row in range(len(info)):
                button2 = tk.Button(self.pacote2[1], width=20, height=20, image=photo2, relief=tk.FLAT,
                                    command=lambda row=row: self.deselecionaProduto(row))
                button2.grid(row=row, column=4)
                button2.image = photo2
                # fim

    def deselecionaProduto(self, row):
        self.listaSelec.pop(row)
        self.calculaTotal()
        self.todos_apertado()

    def onFrameConfigure2(self, event):  # comeco scroolbar frame2
        '''Reset the scroll region to encompass the inner frame'''
        self.pacote2[0].configure(scrollregion=self.pacote2[0].bbox("all"))  # fim scroolbar frame2

    # Name mangling for subclasses
    __resetValues = resetValues
    __FazTela = FazTela
    # fim
