import Tkinter as Tkin
from database import database as db
import cadastro_produto_menor as cpm
bd = db.Database(0)
tm = cpm.TelaMenor()
# funcao de teste
def Teste():
    print("Testado")
# fim

#funcao de destaque das abas
def todos_apertado():
    todos.config(relief=SUNKEN, background=cor2)
    doces.config(relief=RAISED, background=cor1)
    salgados.config(relief=RAISED, background=cor1)
    massas.config(relief=RAISED, background=cor1)
    bebidas.config(relief=RAISED, background=cor1)
    outros.config(relief=RAISED, background=cor1)

def doces_apertado():
    todos.config(relief=RAISED, background=cor1)
    doces.config(relief=SUNKEN, background=cor2)
    salgados.config(relief=RAISED, background=cor1)
    massas.config(relief=RAISED, background=cor1)
    bebidas.config(relief=RAISED, background=cor1)
    outros.config(relief=RAISED, background=cor1)
def salgados_apertado():
    todos.config(relief=RAISED, background=cor1)
    doces.config(relief=RAISED, background=cor1)
    salgados.config(relief=SUNKEN, background=cor2)
    massas.config(relief=RAISED, background=cor1)
    bebidas.config(relief=RAISED, background=cor1)
    outros.config(relief=RAISED, background=cor1)
def massas_apertado():
    todos.config(relief=RAISED, background=cor1)
    doces.config(relief=RAISED, background=cor1)
    salgados.config(relief=RAISED, background=cor1)
    massas.config(relief=SUNKEN, background=cor2)
    bebidas.config(relief=RAISED, background=cor1)
    outros.config(relief=RAISED, background=cor1)
def bebidas_apertado():
    todos.config(relief=RAISED, background=cor1)
    doces.config(relief=RAISED, background=cor1)
    salgados.config(relief=RAISED, background=cor1)
    massas.config(relief=RAISED, background=cor1)
    bebidas.config(relief=SUNKEN, background=cor2)
    outros.config(relief=RAISED, background=cor1)
def outros_apertado():
    todos.config(relief=RAISED, background=cor1)
    doces.config(relief=RAISED, background=cor1)
    salgados.config(relief=RAISED, background=cor1)
    massas.config(relief=RAISED, background=cor1)
    bebidas.config(relief=RAISED, background=cor1)
    outros.config(relief=SUNKEN, background=cor2)
#fim

root=Tkin.Tk()

# menu principal
menu = Tkin.Menu(root)
root.config(menu=menu)

subMenu1 = Tkin.Menu(menu)
menu.add_cascade(label="Arquivo", menu=subMenu1)
subMenu1.add_command(label="Novo", command=Teste)
subMenu1.add_command(label="Salvar", command=Teste)
subMenu1.add_separator()
subMenu1.add_command(label="Sair", command=root.destroy)

subMenu2 = Tkin.Menu(menu)
menu.add_cascade(label="Editar", menu=subMenu2)
subMenu2.add_command(label="Copiar Tudo", command=Teste)
subMenu2.add_command(label="Copiar", command=Teste)
subMenu2.add_command(label="Colar", command=Teste)
subMenu2.add_command(label="Cortar", command=Teste)

subMenu3 = Tkin.Menu(menu)
menu.add_cascade(label="Visualizar", menu=subMenu3)
subMenu3.add_command(label="Ferramentas", command=Teste)
subMenu3.add_command(label="Arquivo Recente", command=Teste)
# fim

# abas de opcoes
cor1 = '#CC2828'
cor2 = '#E94545'

toolbar = Tkin.Frame(root, bg=cor1)

todos = Tkin.Button(toolbar, text="   Todos   ", bg=cor1,  command=todos_apertado)
todos['font']=('bold')
todos['fg']='white'
todos.pack(side=Tkin.LEFT, padx=1, pady=1)
doces = Tkin.Button(toolbar, text="   Doces   ", bg=cor1,  command=doces_apertado)
doces['font']=('bold')
doces['fg']='white'
doces.pack(side=Tkin.LEFT, padx=1, pady=1)
salgados = Tkin.Button(toolbar, text="Salgados", bg=cor1, command=salgados_apertado)
salgados['font']=('bold')
salgados['fg']='white'
salgados.pack(side=Tkin.LEFT, padx=1, pady=1)
massas = Tkin.Button(toolbar, text="  Massas  ", bg=cor1, command=massas_apertado)
massas['font']=('bold')
massas['fg']='white'
massas.pack(side=Tkin.LEFT, padx=1, pady=1)
bebidas = Tkin.Button(toolbar, text=" Bebidas ", bg=cor1, command=bebidas_apertado)
bebidas['font']=('bold')
bebidas['fg']='white'
bebidas.pack(side=Tkin.LEFT, padx=1, pady=1)
outros = Tkin.Button(toolbar, text="   Outros   ", bg=cor1, command=outros_apertado)
outros['font']=('bold')
outros['fg']='white'
outros.pack(side=Tkin.LEFT, padx=1, pady=1)

toolbar.pack(side=Tkin.TOP, fill=Tkin.X)
# fim



# barra de 'status'
status = Tkin.Label(root, text="Estado: Rodando", bg="white", bd=1, relief=Tkin.SUNKEN, anchor=Tkin.W)
status.pack(side=Tkin.BOTTOM, fill=Tkin.X)
# fim

class Example(Tkin.Frame):


    def __init__(self, root):

        self.container1 = Tkin.Frame(root)
        self.container2 = Tkin.Frame(root)
        self.container1.pack(fill=Tkin.X)
        self.container2.pack(side=Tkin.BOTTOM, fill=Tkin.X, padx=15, pady=15)

#"cabecalho" da tabela dos itens
        self.objeto1 = Tkin.Label(self.container1, text="Codigo:")
        self.objeto1["font"] = ["bold"]
        self.objeto1.pack(side=Tkin.LEFT)
        self.objeto2 = Tkin.Label(self.container1, text="                                        ")
        self.objeto2["font"] = ["bold"]
        self.objeto2.pack(side=Tkin.LEFT)
        self.objeto3 = Tkin.Label(self.container1, text="Nome:")
        self.objeto3["font"] = ["bold"]
        self.objeto3.pack(side=Tkin.LEFT)
        self.objeto4 = Tkin.Label(self.container1, text="                                                       ")
        self.objeto4["font"] = ["bold"]
        self.objeto4.pack(side=Tkin.LEFT)
        self.objeto5 = Tkin.Label(self.container1, text="Valor:")
        self.objeto5["font"] = ["bold"]
        self.objeto5.pack(side=Tkin.LEFT)
        self.objeto6 = Tkin.Label(self.container1, text="                                              ")
        self.objeto6["font"] = ["bold"]
        self.objeto6.pack(side=Tkin.LEFT)
# fim

# espaco com "inserir", "editar", "excluir" e "pesquisar"

        self.espaco1 = Tkin.Label(self.container2, text="             ")
        self.espaco1.pack(side=Tkin.LEFT)
        self.inserir = Tkin.Button(self.container2, text="Inserir", command=lambda:self.help(bd))
        self.inserir["font"] = ("Arial", "10")
        self.inserir['padx'] = 10
        self.inserir.pack(side=Tkin.LEFT)
        self.espaco2 = Tkin.Label(self.container2, text="             ")
        self.espaco2.pack(side=Tkin.LEFT)
        self.editar = Tkin.Button(self.container2, text="Editar", command=Teste)
        self.editar["font"] = ("Arial", "10")
        self.editar['padx'] = 10
        self.editar.pack(side=Tkin.LEFT)
        self.espaco2 = Tkin.Label(self.container2, text="             ")
        self.espaco2.pack(side=Tkin.LEFT)
        self.excluir = Tkin.Button(self.container2, text="Excluir", command=Teste)
        self.excluir["font"] = ("Arial", "10")
        self.excluir['padx'] = 10
        self.excluir.pack(side=Tkin.LEFT)
        self.espaco3 = Tkin.Label(self.container2, text="             ")
        self.espaco3.pack(side=Tkin.LEFT)
        self.pesquisar1 = Tkin.Label(self.container2, text="Pesquisar: ")
        self.pesquisar1["font"] = ("Arial", "10")
        self.pesquisar1.pack(side=Tkin.LEFT)
        self.pesquisar2 = Tkin.Entry(self.container2)
        self.pesquisar2["width"] = 25
        self.pesquisar2["font"] = ("Arial", "10")
        self.pesquisar2.pack(side=Tkin.LEFT)
        pesquisado = self.pesquisar2.get()  # pesquisado = o que foi escrito no "Entry / barra de pesquisa"
        self.espaco4 = Tkin.Label(self.container2, text=" ")
        self.espaco4.pack(side=Tkin.LEFT)
        self.ok = Tkin.Button(self.container2, text="Ok", command=Teste)
        self.ok["font"] = ("Arial", "10")
        self.ok['padx'] = 10
        self.ok.pack(side=Tkin.LEFT)
# fim

# tabela dos itens
        Tkin.Frame.__init__(self, root)
        self.canvas = Tkin.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = Tkin.Frame(self.canvas, background="#f0f0f0")
        self.vsb = Tkin.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.populate()

    def help(self,bd):
        tm.FazTela(bd)
        self.populate()
    def populate(self):
        info = bd.selectProduto()
        '''Put in some fake data'''
        cor1 = '#ffffff'
        cor2 = '#808080'

        for row in range(len(info)):
            if row % 2 == 0:
                t=info[row][0]
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor1, fg='black', font="bold", width=25)
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=0)
            else:
                t=info[row][0]
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor2, fg='black', font="bold", width=25)
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=0)
        for row in range(len(info)):
            if row % 2 == 0:
                t=info[row][1]
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor1, fg='black', font="bold", width=30)
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
            else:
                t=info[row][1]
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor2, fg='black', font="bold", width=30)
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=1)
        for row in range(len(info)):
            if row % 2 == 0:
                t="R$ " + str(info[row][2])
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor1, fg='black', font="bold", width=25)
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)
            else:
                t="R$ " + str(info[row][2])
                ent = Tkin.Entry(self.frame, state='readonly', readonlybackground=cor2, fg='black', font="bold", width=25)
                var = Tkin.StringVar()
                var.set(t)
                ent.config(textvariable=var, relief='flat')
                ent.grid(row=row, column=2)


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
# fim


Example(root).pack(side="top", fill="both", expand=True)
#root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
root.title('Programa Guts')
root.resizable(width=False, height=True)
#root.geometry('755x450')
root.attributes("-fullscreen", True)
root.mainloop()
