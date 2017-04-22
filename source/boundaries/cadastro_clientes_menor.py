# encoding: utf-8

from Tkinter import *


class clienteCadastro(Frame):
    def FazTela(self, root):

        #root = Toplevel()

        cor = '#D32F2F'
        info = 25

        info1 = Frame(root)
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

        endereco1 = Label(info1, text="Endereco:")
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

        data1 = Label(info1, text="Data:")
        data1['font']=['bold']
        data1.grid(row=4, column=1, sticky=W)
        data2 = Entry(info1)
        data2["width"]=40
        data2["font"] = ("Arial", "10")
        data2.grid(row=5, column=1)

        email1 = Label(info1, text="E-mail:")
        email1['font']=['bold']
        email1.grid(row=4, column=3, sticky=W)
        email2 = Entry(info1)
        email2["width"]=40
        email2["font"] = ("Arial", "10")
        email2.grid(row=5, column=3)

        salto5 = Label(info1, text="")
        salto5.grid(row=6, column=0)

        telefone1 = Label(info1, text="Telefone:")
        telefone1['font']=['bold']
        telefone1.grid(row=7, column=1, sticky=W)
        telefone2 = Entry(info1)
        telefone2["width"]=40
        telefone2["font"] = ("Arial", "10")
        telefone2.grid(row=8, column=1)

        celular1 = Label(info1, text="Celular:")
        celular1['font']=['bold']
        celular1.grid(row=7, column=3, sticky=W)
        celular2 = Entry(info1)
        celular2["width"]=40
        celular2["font"] = ("Arial", "10")
        celular2.grid(row=8, column=3)

        info2 = Frame(root)
        info2.grid(sticky=S+W+E)

        espaco1 = Label(info2, text="                                                                                                     ")
        espaco1.grid(row=0, column=0)

        pronto = Button(info2, text="Pronto", bg=cor)
        pronto["font"]=['bold']
        pronto['fg']='white'
        pronto['padx']=1
        pronto['pady']=1
        pronto.grid(row=1, column=1)

        espaco2 = Label(info2, text="                                                                                                     ")
        espaco2.grid(row=2, column=2)

        status = Label(info2, text="Estado: Normal", bg="white", bd=1, relief=SUNKEN, anchor=W)
        status.grid(row=3, column=0, sticky=S + W + E, columnspan=3)

        #root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
        root.title('Cadastro do Cliente')
        root.resizable(width=False, height=False)
        root.mainloop()