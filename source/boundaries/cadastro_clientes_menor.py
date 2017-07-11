# encoding: utf-8

import tkMessageBox
from Tkinter import *
from source.entities import tratamentos as tr
from source.entities import database as db


class clienteCadastro():
# Construtor
    def __init__(self):
        self.top = None
        self.bd = db.Database()
    #    self.FazTela()

#Funcao de fechamento da janela
    def CloseWindow(self):
        self.top.destroy()
        #self.top.quit()
        self.top = None

#Retorna o valor objeto da janela
    def GetWindow(self):
        return self.top

    def Testado(self, nome,endereco,email,telefone):
        try:
            c1 = tr.ClientesReceive(nome,endereco,email,telefone)
        except tr.ErroEntrada as e:
            tkMessageBox.showerror("Erro encontrado", e.message)
        else:
            self.bd.insertCliente(c1)
        self.CloseWindow()

    def FazTela(self):
        #Condicional para que não sejam abertas duas janelas simultaneamente
        if(self.top!=None):
            return

        self.top = Toplevel()
        self.top.title('Guts\' Orçamento - Novo Cliente')

        cor = '#D32F2F'
        info = 25

        info1 = Frame(self.top)
        info1.grid(sticky=N+W+E)

        salto1 = Label(info1, text="          ")
        salto1.grid(row=0, column=0)

        nome1 = Label(info1, text="Nome:")
        nome1['font']=['bold']
        nome1.grid(row=1, column=1, sticky=W)
        nome2 = Entry(info1)
        nome2["width"]=40
        nome2["font"] = ("Arial", "10")
        nome2.grid(row=2, column=1)

        salto2 = Label(info1, text="          ")
        salto2.grid(row=0, column=2)

        endereco1 = Label(info1, text="Endereço:")
        endereco1['font']=['bold']
        endereco1.grid(row=1, column=3, sticky=W)
        endereco2 = Entry(info1)
        endereco2["width"]=40
        endereco2["font"] = ("Arial", "10")
        endereco2.grid(row=2, column=3)

        salto3 = Label(info1, text="          ")
        salto3.grid(row=0, column=4)

        salto4 = Label(info1, text="")
        salto4.grid(row=3, column=0)

        telefone1 = Label(info1, text="Telefone:")
        telefone1['font']=['bold']
        telefone1.grid(row=4, column=1, sticky=W)
        telefone2 = Entry(info1)
        telefone2["width"]=40
        telefone2["font"] = ("Arial", "10")
        telefone2.grid(row=5, column=1)

        email1 = Label(info1, text="E-mail:")
        email1['font']=['bold']
        email1.grid(row=4, column=3, sticky=W)
        email2 = Entry(info1)
        email2["width"]=40
        email2["font"] = ("Arial", "10")
        email2.grid(row=5, column=3)

        salto5 = Label(info1, text="")
        salto5.grid(row=6, column=0)


        info2 = Frame(self.top)
        info2.grid(sticky=S+W+E)

        espaco1 = Label(info2, text="                                                                                                     ")
        espaco1.grid(row=0, column=0)

        pronto = Button(info2, text="Pronto", bg=cor,command=lambda:self.Testado(nome2.get(),endereco2.get(),telefone2.get(),email2.get()))
        pronto["font"]=['bold']
        pronto['fg']='white'
        pronto['padx']=1
        pronto['pady']=1
        pronto.grid(row=1, column=1)

        espaco2 = Label(info2, text="                                                                                                     ")
        espaco2.grid(row=2, column=2)

        self.top.protocol("WM_DELETE_WINDOW", lambda: self.CloseWindow())

       # status = Label(info2, text="Estado: Normal", bg="white", bd=1, relief=SUNKEN, anchor=W)
       # status.grid(row=3, column=0, sticky=S + W + E, columnspan=3)

        #root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
#        root.title('Cadastro do Cliente')
#        root.resizable(width=False, height=False)
        #root.mainloop()