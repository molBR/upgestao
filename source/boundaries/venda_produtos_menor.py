from Tkinter import *
from source.entities import database as db

class Application:
    def __init__(self):
        self.top = None
        self.bd = db.Database()
        self.cor1 = '#D32F2F'

    def CloseWindow(self):
        self.top.destroy()
        self.top = None

    def GetWindow(self):
        return self.top


    def FazTela(self):

        self.top = Toplevel()
        self.top.title('Guts\' Orçamento - Valor final')
        container1 = Frame(self.top)
        self.espaco0 = Label(self.container1, text="          ")
        self.espaco0.grid (row=0, column=0)
        self.valor_final1 = Label(self.container1, text="Valor Final:")
        self.valor_final1['font'] = ['bold']
        self.valor_final1.grid(row=1, column=1)
        self.valor_final2 = Entry(self.container1)
        self.valor_final2["width"] = 25
        self.valor_final2['font'] = ['bold']
        self.valor_final2.grid(row=2, column=1)
        self.espaco1 = Label(self.container1, text="          ")
        self.espaco1.grid(row=3, column=2)
        self.ok = Button(self.container1, text="OK", bg=self.cor1)
        self.ok['font']=['bold']
        self.ok['fg']='white'
        self.ok['padx'] = 2
        self.ok['pady'] = 2
        self.ok.grid(row=4, column=1)
        self.espaco2 = Label(self.container1, text="          ")
        self.espaco2.grid(row=5, column=0)

root = Tk()
Application(root)
root.title('Valor Final')
root.mainloop()