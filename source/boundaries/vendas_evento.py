# encoding: utf-8

import Tkinter as tk
import source.entities.tratamentos as tr
import source.entities.tipoEvento as te
import tkMessageBox

def Teste():
    print("Testado")

class VendEvent(tk.Frame):
#root=Tk()

    def __init__(self, parent, controller,Cliente):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.FazTela()
        self.Cliente = Cliente
        self.tipoEvento = te.tipoEvento(1,1,1,1,1,1,1,1,1)


    def setCliente(self,Cliente):
        self.Cliente = Cliente

    def Insere(self,tipo,rua,numero,bairro,complemento,adultos,criancas,data):
        print self.Cliente.getNome()
        try:
            self.tipoEvento = tr.EventosReceive(tipo,rua,numero,bairro,complemento,adultos,criancas,data)
        except tr.ErroEntrada as e:
            tkMessageBox.showerror("Erro encontrado ", e.message)
        else:
            self.controller.show_frame('vendProd')


    def getTipoEvento(self):
        return self.tipoEvento

    def FazTela(self):

        toolbar1 = tk.Frame(self, bg="white")

        menu = tk.Label(toolbar1, text=" Menu Inicial ", bg="white")
        menu["font"] = ("Arial", "10")
        menu.pack(side=tk.LEFT)
        espaco1 = tk.Label(toolbar1, text=" | ", bg="white")
        espaco1["font"] = ("Arial", "12")
        espaco1.pack(side=tk.LEFT)
        novavenda = tk.Button(toolbar1, text="Vendas", bg="light grey", relief=tk.FLAT)
        novavenda["font"] = ("Arial", "10")
        novavenda.pack(side=tk.LEFT, padx=1, pady=1)
        espaco2 = tk.Label(toolbar1, text=" | ", bg="white")
        espaco2["font"] = ("Arial", "12")
        espaco2.pack(side=tk.LEFT)
        #historicovenda = tk.Button(toolbar1, text="Historico de Vendas", bg="white", relief=tk.FLAT)
        #historicovenda["font"] = ("Arial", "10")
        #historicovenda.pack(side=tk.LEFT, padx=1, pady=1)
        #espaco3 = tk.Label(toolbar1, text=" | ", bg="white")
        #espaco3["font"] = ("Arial", "12")
        #espaco3.pack(side=tk.LEFT)
        #inserirproduto = tk.Button(toolbar1, text="Cadastrar Produto", bg="white", relief=tk.FLAT)
        #inserirproduto["font"] = ("Arial", "10")
        #inserirproduto.pack(side=tk.LEFT, padx=1, pady=1)

        toolbar1.pack(side=tk.TOP, fill=tk.X)

        toolbar2 = tk.Frame(self, bg="#fafafa")

        clientes = tk.Button(toolbar2, text=" Clientes ", bg="#fafafa", fg="blue", relief=tk.FLAT)
        clientes["font"] = ("Arial", "10")
        clientes.pack(side=tk.LEFT)
        espaco1 = tk.Label(toolbar2, text=" > ", bg="#fafafa", fg="blue")
        espaco1["font"] = ("Arial", "12")
        espaco1.pack(side=tk.LEFT)
        festa = tk.Button(toolbar2, text=" Festa ", bg="#fafafa", fg="black", relief=tk.FLAT)
        festa["font"] = ("Arial", "10")
        festa.pack(side=tk.LEFT, padx=1, pady=1)
        espaco2 = tk.Label(toolbar2, text=" > ", bg="#fafafa", fg="blue")
        espaco2["font"] = ("Arial", "12")
        espaco2.pack(side=tk.LEFT)
        venda = tk.Button(toolbar2, text=" Venda ", bg="#fafafa", fg="blue", relief=tk.FLAT)
        venda["font"] = ("Arial", "10")
        venda.pack(side=tk.LEFT, padx=1, pady=1)

        toolbar2.pack(side=tk.TOP, fill=tk.X)

        cor1 = '#D32F2F'

        toolbar3 = tk.Frame(self, bg=cor1)

        todos = tk.Label(toolbar3, text="Cadastro de Festa", bg=cor1)
        todos["font"] = ("bold", "14")
        todos['fg'] = 'white'
        todos.pack(side=tk.LEFT, padx=1, pady=1)

        toolbar3.pack(side=tk.TOP, fill=tk.X)
        # fim

        # barra de 'status'
        status = tk.Label(self, text="Estado: Rodando", bg="white", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status.pack(side=tk.BOTTOM, fill=tk.X)
        # fim


        self.container1 = tk.Frame(self, background="#fafafa")
        self.container2 = tk.Frame(self)
        self.container1.pack(fill=tk.X)
        self.container2.pack(side=tk.BOTTOM, fill=tk.X, padx=15, pady=15)

        self.salto0 = tk.Label(self.container1, text="", width=20, background="#fafafa")
        self.salto0.grid(row=0, column=0)
        self.salto1 = tk.Label(self.container1, text="", width=20, background="#fafafa")
        self.salto1.grid(row=1, column=0)
        self.salto2 = tk.Label(self.container1, text="", width=20, background="#fafafa")
        self.salto2.grid(row=2, column=0)
        self.tipo1 = tk.Label(self.container1, text="Tipo de Festa", width=38, background="#fafafa")
        self.tipo1["font"]=("Arial", "12")
        self.tipo1.grid(row=3, column=1)
        self.tipo2 = tk.Entry(self.container1, width=50)
        self.tipo2.grid(row=4, column=1)
        self.rua1 = tk.Label(self.container1, text="Rua:", width=38, background="#fafafa")
        self.rua1["font"]=("Arial", "12")
        self.rua1.grid(row=3, column=3)
        self.rua2 = tk.Entry(self.container1, width=50)
        self.rua2.grid(row=4, column=3)
        self.salto3 = tk.Label(self.container1, text="", width=20, background="#fafafa")
        self.salto3.grid(row=5, column=2)
        self.numero1 = tk.Label(self.container1, text="Número:", width=38, background="#fafafa")
        self.numero1["font"]=("Arial", "12")
        self.numero1.grid(row=6, column=1)
        self.numero2 = tk.Entry(self.container1, width=50)
        self.numero2.grid(row=7, column=1)
        self.bairro1 = tk.Label(self.container1, text="Bairro:", width=38, background="#fafafa")
        self.bairro1["font"]=("Arial", "12")
        self.bairro1.grid(row=6, column=3)
        self.bairro2 = tk.Entry(self.container1, width=50)
        self.bairro2.grid(row=7, column=3)
        self.salto4 = tk.Label(self.container1, text=" ", width=20, background="#fafafa")
        self.salto4.grid(row=8, column=4)
        self.cidade1 = tk.Label(self.container1, text="Cidade:", width=38, background="#fafafa")
        self.cidade1["font"]=("Arial", "12")
        self.cidade1.grid(row=9, column=1)
        self.cidade2 = tk.Entry(self.container1, width=50)
        self.cidade2.grid(row=10, column=1)
        self.complemento1 = tk.Label(self.container1, text="Complemento:", width=38, background="#fafafa")
        self.complemento1["font"]=("Arial", "12")
        self.complemento1.grid(row=9, column=3)
        self.complemento2 = tk.Entry(self.container1, width=50)
        self.complemento2.grid(row=10, column=3)
        self.salto4 = tk.Label(self.container1, text=" ", width=20, background="#fafafa")
        self.salto4.grid(row=11, column=0)
        self.adultos1 = tk.Label(self.container1, text="Número de Adultos:", width=38, background="#fafafa")
        self.adultos1["font"]=("Arial", "12")
        self.adultos1.grid(row=12, column=1)
        self.adultos2 = tk.Entry(self.container1, width=50)
        self.adultos2.grid(row=13, column=1)
        self.criancas1 = tk.Label(self.container1, text="Número de Criancas:", width=38, background="#fafafa")
        self.criancas1["font"]=("Arial", "12")
        self.criancas1.grid(row=12, column=3)
        self.criancas2 = tk.Entry(self.container1, width=50)
        self.criancas2.grid(row=13, column=3)
        self.salto5 = tk.Label(self.container1, text=" ", width=20, background="#fafafa")
        self.salto5.grid(row=14, column=2)
        self.data1 = tk.Label(self.container1, text="Data:", width=38, background="#fafafa")
        self.data1["font"]=("Arial", "12")
        self.data1.grid(row=15, column=1)
        self.data2 = tk.Entry(self.container1, width=50)
        self.data2.grid(row=16, column=1)
        self.salto6 = tk.Label(self.container1, text=" ", width=20, background="#fafafa")
        self.salto6.grid(row=17, column=4)
        self.salto7 = tk.Label(self.container1, text=" ", width=20, background="#fafafa")
        self.salto7.grid(row=18, column=4)
        self.salto8 = tk.Label(self.container1, text=" ", width=20, background="#fafafa")
        self.salto8.grid(row=19, column=4)

        self.espaco1 = tk.Label(self.container2, text="                                                                                       ")
        self.espaco1.pack(side=tk.LEFT)

        self.voltar = tk.Button(self.container2, text="Voltar",
                                   command=lambda: self.controller.show_frame('cadClientMaior'))
        self.voltar["font"] = ("bold", "12")
        self.voltar['padx'] = 10
        self.voltar['pady'] = 10
        self.voltar.pack(side=tk.LEFT)

        self.espaco2 = tk.Label(self.container2, text="                                                                                                                                       ")
        self.espaco2.pack(side=tk.LEFT)

        #self.continuar = tk.Button(self.container2, text="Continuar", command=lambda: self.controller.show_frame('vendProd'))
        self.continuar = tk.Button(self.container2, text="Continuar",
                                   command=lambda: self.Insere(self.tipo2.get(),self.rua2.get(),self.numero2.get(),self.bairro2.get(),
                                                               self.complemento2.get(),self.adultos2.get(),self.criancas2.get(),self.data2.get()))
        self.continuar["font"] = ("bold", "12")
        self.continuar['padx'] = 10
        self.continuar['pady'] = 10
        self.continuar.pack(side=tk.LEFT)

"""
Example(root).pack(side="top", fill="both", expand=True)
#root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
root.title('Inserir Tipo')
root.resizable(width=False, height=False)
root.geometry('1150x600')
root.mainloop()
"""