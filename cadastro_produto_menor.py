from Tkinter import *
from database import database as db
from database import tratamentos as tr
import tkMessageBox
class TelaMenor():
    def __init__(self):
        self.top = None
        self.OPTIONS = []
        self.cor1 = '#D32F2F'

    def CloseWindow(self):
        self.top.destroy()
        self.top.quit()
        self.top = None

    def GetWindow(self):
        return self.top

    def SendToTR(self,id,nome,valor,tipo,bd):
        try:
            if(bd.ExistsProduto(id)):
                raise Exception()
            else:
                p1 = tr.ProdutosRecieve(id,nome,valor,tipo,bd)
        except:
            tkMessageBox.showerror("Erro encontrado", "Digite valores validos!")
        else:
            bd.insertProduto(p1)
        finally:
            self.CloseWindow()


    def FazTela(self,bd):
        if(self.top!=None):
            self.CloseWindow()
            self.FazTela()
        else:
            self.top=Toplevel()
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
            info = Frame(self.top)
            info.grid(sticky=N+S+W+E)

            salto1 = Label(info, text="       ")
            salto1.grid(row=0, column=0)

            #Valor zoado
            id1 = Label(info, text="Id:")
            id1['font'] = ['bold']
            id1.grid(row=1, column=1, sticky=W)


            id2 = Entry(info)
            id2["width"] = 20
            id2.grid(row=2, column=1)
            # fim do valor zoado


            nome1 = Label(info, text="Nome:")
            nome1['font']=['bold']
            nome1.grid(row=3, column=1, sticky=W)

            nome2 = Entry(info)
            nome2["width"]=40
            nome2.grid(row=5, column=1)

            salto2 = Label(info, text="")
            salto2.grid(row=6, column=0)

            valor1 = Label(info, text="Valor:")
            valor1['font']=['bold']
            valor1.grid(row=7, column=1, sticky=W)

            valor2 = Entry(info)
            valor2["width"]=40
            valor2.grid(row=8, column=1)



            salto3 = Label(info, text="")
            salto3.grid(row=9, column=0)

            variable = StringVar(info)
            variable.set(self.OPTIONS[0])

            droplist = apply(OptionMenu, (info, variable) + tuple(self.OPTIONS))
            droplist.grid(row=10, column=1)

            salto4 = Label(info, text="")
            salto4.grid(row=11, column=0)

            pronto = Button(info, text="Pronto", bg=self.cor1, bd=3,command=lambda: self.SendToTR(id2.get(),nome2.get(),valor2.get(),variable.get(),bd))
            pronto['font']=['bold']
            pronto['fg']='white'
            pronto.grid(row=12, column=1)

            salto5 = Label(info, text="")
            salto5.grid(row=13, column=1)

            espaco1 = Label(info, text="       ")
            espaco1.grid(row=14, column=2)
            #fim]

            # barra de "status"
            status = Label(info, text="Estado: Normal", bg="white", bd=1, relief=SUNKEN, anchor=W)
            status.grid(row= 15, column=0, sticky=S+W+E, columnspan=3)
            #fim

            # formatacao da janela
            self.top.title('Cadastro do Produto')
                #top.iconbitmap(r'c:\Python27\DLLs\icon.ico')
            self.top.resizable(width=False, height=False)
            self.top.geometry('500x276')
            self.top.protocol("WM_DELETE_WINDOW", lambda:self.CloseWindow())
            self.top.mainloop()
            #fim
