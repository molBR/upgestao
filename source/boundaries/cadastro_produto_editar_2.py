# encoding: utf-8

import tkMessageBox
import Tkinter as tk

from source.entities import tratamentos as tr


class ProdutoEdicao():
#Construtor
    def __init__(self):
        self.top = None
        self.OPTIONS = []
        self.cor1 = '#D32F2F'

#Fechamento de janela
    def CloseWindow(self):
        self.top.destroy()
        self.top.quit()
        self.top = None

#Retorna a janela como um objeto
    def GetWindow(self):
        return self.top

#Manda para tratemento para verificacao de erros
    def SendToTR(self,id,nome,valor,tipo,idAntigo,bd):

        try:
            if (int(idAntigo) == int(id)):
                p1 = tr.ProdutosReceive(id, nome, valor, tipo, bd)
            elif(not bd.ExistsProduto(id)):
                p1 = tr.ProdutosReceive(id, nome, valor, tipo, bd)
            else:
                raise tr.ErroEntrada(id, "O ID digitado (" + id + ") já existe no atual banco de dados. Escolha outro Id")
        except tr.Erro as e:
            tkMessageBox.showerror("Erro encontrado", e.message)
        else:
            bd.deleteProduto(idAntigo)
            bd.insertProduto(p1)
        finally:
            self.CloseWindow()

#Criacao de telas
    def FazTela(self, bd, p1):
        if(self.top!=None):
            self.CloseWindow()
            self.FazTela()
        else:
            self.top = tk.Toplevel()
            # opcoes do droplist
            self.OPTIONS = [
                "Tipo de produto",
                "Doce",
                "Salgado",
                "Massa",
                "Bebida",
                "Outro"
                ]
            #fim

            # criacao e posicao dos widgets
            info = tk.Frame(self.top)
            info.grid(sticky=tk.N+tk.S+tk.W+tk.E)

            salto1 = tk.Label(info, text="        ")
            salto1.grid(row=0, column=0)

            id1 = tk.Label(info, text="Código:") #comeco id
            id1['font'] = ['bold']
            id1.grid(row=1, column=1, sticky=tk.W)

            id2 = tk.Entry(info)
            id2.insert(0,p1.getId())
            id2["width"] = 20
            id2["font"] = ("Arial", "10")
            id2.grid(row=2, column=1) #fim id

            salto2 = tk.Label(info, text="")
            salto2.grid(row=3, column=0)

            nome1 = tk.Label(info, text="Nome:") #comeco nome
            nome1['font']=['bold']
            nome1.grid(row=4, column=1, sticky=tk.W)

            nome2 = tk.Entry(info)
            nome2.insert(0,p1.getNome())
            nome2["width"]=40
            nome2["font"] = ("Arial", "10")
            nome2.grid(row=5, column=1) #fim nome

            salto3 = tk.Label(info, text="")
            salto3.grid(row=6, column=0)

            valor1 = tk.Label(info, text="Valor:") #comeco valor
            valor1['font']=['bold']
            valor1.grid(row=7, column=1, sticky=tk.W)

            valor2 = tk.Entry(info)
            valor2.insert(0,p1.getValor_inic())
            valor2["width"]=40
            valor2["font"] = ("Arial", "10")
            valor2.grid(row=8, column=1) #fim valor

            salto4 = tk.Label(info, text="")
            salto4.grid(row=9, column=0)

            variable = tk.StringVar(info) #comeco opcoes
            variable.set(self.OPTIONS[int(p1.getId_categoria())])

            droplist = apply(tk.OptionMenu, (info, variable) + tuple(self.OPTIONS))
            droplist.grid(row=10, column=1) #fim opcoes

            salto5 = tk.Label(info, text="")
            salto5.grid(row=11, column=0)

            #comeco pronto
            pronto = tk.Button(info, text="Pronto", bg=self.cor1, command=lambda: self.SendToTR(str(id2.get()), nome2.get(), valor2.get(), variable.get(),p1.getId(), bd))
            pronto['font']=['bold']
            pronto['fg']='white'
            pronto['padx'] = 1
            pronto['pady'] = 1
            pronto.grid(row=12, column=1) #fim pronto

            salto6 = tk.Label(info, text="        ")
            salto6.grid(row=13, column=2)

            #fim

            # barra de "status"
            status = tk.Label(info, text="Estado: Normal", bg="white", bd=1, relief=tk.SUNKEN, anchor=tk.W)
            status.grid(row= 14, column=0, sticky=tk.S+tk.W+tk.E, columnspan=3)
            #fim

            # formatacao da janela
            self.top.title('Edição do Produto')
                #top.iconbitmap(r'c:\Python27\DLLs\icon.ico')
            self.top.resizable(width=False, height=False)
            self.top.protocol("WM_DELETE_WINDOW", lambda:self.CloseWindow())
            self.top.mainloop()
            #fim
