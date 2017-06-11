# encoding: utf-8

from Tkinter import *

def Teste():
    print("Testado")

root=Tk()

toolbar1 = Frame(root, bg="white")

menu = Label(toolbar1, text=" Menu Inicial ", bg="white")
menu["font"] = ("Arial", "10")
menu.pack(side=LEFT)
espaco1 = Label(toolbar1, text=" | ", bg="white")
espaco1["font"] = ("Arial", "12")
espaco1.pack(side=LEFT)
novavenda = Button(toolbar1, text="Vendas", bg="light grey", relief=FLAT)
novavenda["font"] = ("Arial", "10")
novavenda.pack(side=LEFT, padx=1, pady=1)
espaco2 = Label(toolbar1, text=" | ", bg="white")
espaco2["font"] = ("Arial", "12")
espaco2.pack(side=LEFT)
historicovenda = Button(toolbar1, text="Historico de Vendas", bg="white", relief=FLAT)
historicovenda["font"] = ("Arial", "10")
historicovenda.pack(side=LEFT, padx=1, pady=1)
espaco3 = Label(toolbar1, text=" | ", bg="white")
espaco3["font"] = ("Arial", "12")
espaco3.pack(side=LEFT)
inserirproduto = Button(toolbar1, text="Cadastrar Produto", bg="white", relief=FLAT)
inserirproduto["font"] = ("Arial", "10")
inserirproduto.pack(side=LEFT, padx=1, pady=1)

toolbar1.pack(side=TOP, fill=X)

toolbar2 = Frame(root, bg="#fafafa")

clientes = Button(toolbar2, text=" Clientes ", bg="#fafafa", fg="blue", relief=FLAT)
clientes["font"] = ("Arial", "10")
clientes.pack(side=LEFT)
espaco1 = Label(toolbar2, text=" > ", bg="#fafafa", fg="blue")
espaco1["font"] = ("Arial", "12")
espaco1.pack(side=LEFT)
festa = Button(toolbar2, text=" Festa ", bg="#fafafa", fg="black", relief=FLAT)
festa["font"] = ("Arial", "10")
festa.pack(side=LEFT, padx=1, pady=1)
espaco2 = Label(toolbar2, text=" > ", bg="#fafafa", fg="blue")
espaco2["font"] = ("Arial", "12")
espaco2.pack(side=LEFT)
venda = Button(toolbar2, text=" Venda ", bg="#fafafa", fg="blue", relief=FLAT)
venda["font"] = ("Arial", "10")
venda.pack(side=LEFT, padx=1, pady=1)

toolbar2.pack(side=TOP, fill=X)

cor1 = '#D32F2F'

toolbar3 = Frame(root, bg=cor1)

todos = Label(toolbar3, text="Cadastro de Festa", bg=cor1)
todos["font"]=("bold", "14")
todos['fg']='white'
todos.pack(side=LEFT, padx=1, pady=1)

toolbar3.pack(side=TOP, fill=X)
# fim

# barra de 'status'
status = Label(root, text="Estado: Rodando", bg="white", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
# fim

class Example(Frame):
    def __init__(self, root): #controller):
        Frame.__init__(self, root)

        self.container1 = Frame(self, background="#fafafa")
        self.container2 = Frame(self)
        self.container1.pack(fill=X)
        self.container2.pack(side=BOTTOM, fill=X, padx=15, pady=15)

        self.salto0 = Label(self.container1, text="", width=20, background="#fafafa")
        self.salto0.grid(row=0, column=0)
        self.salto1 = Label(self.container1, text="", width=20, background="#fafafa")
        self.salto1.grid(row=1, column=0)
        self.salto2 = Label(self.container1, text="", width=20, background="#fafafa")
        self.salto2.grid(row=2, column=0)
        self.tipo1 = Label(self.container1, text="Tipo de Festa", width=38, background="#fafafa")
        self.tipo1["font"]=("Arial", "12")
        self.tipo1.grid(row=3, column=1)
        self.tipo2 = Entry(self.container1, width=50)
        self.tipo2.grid(row=4, column=1)
        self.rua1 = Label(self.container1, text="Rua:", width=38, background="#fafafa")
        self.rua1["font"]=("Arial", "12")
        self.rua1.grid(row=3, column=3)
        self.rua2 = Entry(self.container1, width=50)
        self.rua2.grid(row=4, column=3)
        self.salto3 = Label(self.container1, text="", width=20, background="#fafafa")
        self.salto3.grid(row=5, column=2)
        self.numero1 = Label(self.container1, text="Número:", width=38, background="#fafafa")
        self.numero1["font"]=("Arial", "12")
        self.numero1.grid(row=6, column=1)
        self.numero2 = Entry(self.container1, width=50)
        self.numero2.grid(row=7, column=1)
        self.bairro1 = Label(self.container1, text="Bairro:", width=38, background="#fafafa")
        self.bairro1["font"]=("Arial", "12")
        self.bairro1.grid(row=6, column=3)
        self.bairro2 = Entry(self.container1, width=50)
        self.bairro2.grid(row=7, column=3)
        self.salto4 = Label(self.container1, text=" ", width=20, background="#fafafa")
        self.salto4.grid(row=8, column=4)
        self.cidade1 = Label(self.container1, text="Cidade:", width=38, background="#fafafa")
        self.cidade1["font"]=("Arial", "12")
        self.cidade1.grid(row=9, column=1)
        self.cidade2 = Entry(self.container1, width=50)
        self.cidade2.grid(row=10, column=1)
        self.complemento1 = Label(self.container1, text="Complemento:", width=38, background="#fafafa")
        self.complemento1["font"]=("Arial", "12")
        self.complemento1.grid(row=9, column=3)
        self.complemento2 = Entry(self.container1, width=50)
        self.complemento2.grid(row=10, column=3)
        self.salto4 = Label(self.container1, text=" ", width=20, background="#fafafa")
        self.salto4.grid(row=11, column=0)
        self.adultos1 = Label(self.container1, text="Número de Adultos:", width=38, background="#fafafa")
        self.adultos1["font"]=("Arial", "12")
        self.adultos1.grid(row=12, column=1)
        self.adultos2 = Entry(self.container1, width=50)
        self.adultos2.grid(row=13, column=1)
        self.criancas1 = Label(self.container1, text="Número de Criancas:", width=38, background="#fafafa")
        self.criancas1["font"]=("Arial", "12")
        self.criancas1.grid(row=12, column=3)
        self.criancas2 = Entry(self.container1, width=50)
        self.criancas2.grid(row=13, column=3)
        self.salto5 = Label(self.container1, text=" ", width=20, background="#fafafa")
        self.salto5.grid(row=14, column=2)
        self.data1 = Label(self.container1, text="Data:", width=38, background="#fafafa")
        self.data1["font"]=("Arial", "12")
        self.data1.grid(row=15, column=1)
        self.data2 = Entry(self.container1, width=50)
        self.data2.grid(row=16, column=1)
        self.salto6 = Label(self.container1, text=" ", width=20, background="#fafafa")
        self.salto6.grid(row=17, column=4)
        self.salto7 = Label(self.container1, text=" ", width=20, background="#fafafa")
        self.salto7.grid(row=18, column=4)
        self.salto8 = Label(self.container1, text=" ", width=20, background="#fafafa")
        self.salto8.grid(row=19, column=4)

        self.espaco = Label(self.container2, text="                                                                                                                                                      ")
        self.espaco.pack(side=LEFT)
        self.continuar = Button(self.container2, text="Continuar", command=Teste)
        self.continuar["font"] = ("bold", "12")
        self.continuar['padx'] = 10
        self.continuar['pady'] = 10
        self.continuar.pack(side=LEFT)

Example(root).pack(side="top", fill="both", expand=True)
#root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
root.title('Inserir Tipo')
root.resizable(width=False, height=False)
root.geometry('1150x600')
root.mainloop()