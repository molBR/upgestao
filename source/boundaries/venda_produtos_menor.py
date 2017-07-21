# encoding: utf-8
from Tkinter import *
import os
from source.entities import database as db

class Application:
    def __init__(self):
        self.top = None
        self.cor1 = '#D32F2F'
        self.vt = StringVar()
        self.desconto = StringVar()

    def CloseWindow(self):
        self.top.destroy()
        self.top = None

    def GetWindow(self):
        return self.top

    def insereTudo(self,bd,venda,controller):
        self.desconto.set(float(self.vt.get()) - float(venda.getCusto_diversos().get()))
        venda.setValor_total(self.vt)
        venda.setSubtrair(self.desconto)
        bd.insertVenda(venda)
        controller.show_frame("cadClientMaior")
        self.CloseWindow()



    def calculaTotal(self,v1):
        #try:
            self.vt.set(float(self.valor_espaco2.get()) + float(v1.getCusto_diversos().get()))
        #except Exception as e:
         #   return
        #else:
            #self.vt = valor
            self.v2.set(str(self.vt.get()))


    def FazTela(self,bd,venda,controller):

        if(self.top!=None):
            self.CloseWindow()
            self.FazTela(bd,venda)

        self.top = Toplevel()
        self.top.title('Guts\' Orçamento - Valor final')
        self.container1 = Frame(self.top)
        self.container1.grid(row=0,column=0)
        self.espaco0 = Label(self.container1, text="          ")
        self.espaco0.grid (row=0, column=0)
        self.valor_espaco1 = Label(self.container1, text="Valor Espaco")
        self.valor_espaco1['font'] = ['bold']
        self.valor_espaco1.grid(row=1, column=1)
        self.v1 = StringVar()
        self.v1.set("0")
        self.valor_espaco2 = Entry(self.container1,textvariable = self.v1)
        self.valor_espaco2["width"] = 25
        self.valor_espaco2['font'] = ['bold']
        self.valor_espaco2.grid(row=2, column=1)
        self.photo = PhotoImage(file=os.getcwd() + "/source/images/repeat.gif")
        self.calcular = Button(self.container1, width=20, height=20, image=self.photo, relief=FLAT,
                                  command=lambda: self.calculaTotal(venda))
        self.calcular.grid(row=1, column=2)
        self.valor_final1 = Label(self.container1, text="Valor Final:")
        self.valor_final1['font'] = ['bold']
        self.valor_final1.grid(row=3, column=1)
        self.v2 = StringVar()
        self.v2.set(venda.getCusto_diversos().get())
        self.valor_final2 = Entry(self.container1,textvariable = self.v2)
        self.valor_final2["width"] = 25
        self.valor_final2['font'] = ['bold']
        self.valor_final2.grid(row=4, column=1)
        self.espaco1 = Label(self.container1, text="          ")
        self.espaco1.grid(row=5, column=2)
        self.ok = Button(self.container1, text="OK", bg=self.cor1, command=lambda: self.insereTudo(bd,venda,controller))
        self.ok['font']=['bold']
        self.ok['fg']='white'
        self.ok['padx'] = 2
        self.ok['pady'] = 2
        self.ok.grid(row=6, column=1)
        self.espaco2 = Label(self.container1, text="          ")
        self.espaco2.grid(row=7, column=0)
        self.calculaTotal(venda)

        self.top.protocol("WM_DELETE_WINDOW", lambda: self.CloseWindow())