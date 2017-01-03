import Tkinter as Tkin
from database import database as db
import cadastro_produto_menor as cpm
from database import tratamentos as tr
import tkMessageBox
import cadastro_produto_deletar as cpd
import cadastro_produto_editar_1 as cpe

#Criacao dos objetos TopLevel a serem utilizados"
bd = db.Database(0) #banco de dados
tm = cpm.TelaMenor() #inserir
td = cpd.TelaMenorDel() #deletar
te = cpe.TelaMenorEdit1() #editar



#Nao sei descrever o que e isso, tem que perguntar pro luquinha mito
root=Tkin.Tk()


menu = Tkin.Menu(root)
root.config(menu=menu)

def Teste():
    print "testei"

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


cor1 = '#52bbeb'
toolbar = Tkin.Frame(root, bg=cor1)




# barra de 'status'
status = Tkin.Label(root, text="Estado: Rodando", bg="white", bd=1, relief=Tkin.SUNKEN, anchor=Tkin.W)
status.pack(side=Tkin.BOTTOM, fill=Tkin.X)
# fim

class Example(Tkin.Frame):

#Botoes de selecao das categorias de produtos
    def todos_apertado(self):
        self.todos.config(relief=Tkin.SUNKEN, background=self.cor2)
        self.doces.config(relief=Tkin.RAISED, background=self.cor1)
        self.salgados.config(relief=Tkin.RAISED, background=self.cor1)
        self.massas.config(relief=Tkin.RAISED, background=self.cor1)
        self.bebidas.config(relief=Tkin.RAISED, background=self.cor1)
        self.outros.config(relief=Tkin.RAISED, background=self.cor1)
        self.populate(bd.selectProduto())

    def doces_apertado(self):
        self.todos.config(relief=Tkin.RAISED, background=self.cor1)
        self.doces.config(relief=Tkin.SUNKEN, background=self.cor2)
        self.salgados.config(relief=Tkin.RAISED, background=self.cor1)
        self.massas.config(relief=Tkin.RAISED, background=self.cor1)
        self.bebidas.config(relief=Tkin.RAISED, background=self.cor1)
        self.outros.config(relief=Tkin.RAISED, background=self.cor1)
        self.populate(bd.selectProdutoDoces())

    def salgados_apertado(self):
        self.todos.config(relief=Tkin.RAISED, background=self.cor1)
        self.doces.config(relief=Tkin.RAISED, background=self.cor1)
        self.salgados.config(relief=Tkin.SUNKEN, background=self.cor2)
        self.massas.config(relief=Tkin.RAISED, background=self.cor1)
        self.bebidas.config(relief=Tkin.RAISED, background=self.cor1)
        self.outros.config(relief=Tkin.RAISED, background=self.cor1)
        self.populate(bd.selectProdutoSalgados())

    def massas_apertado(self):
        self.todos.config(relief=Tkin.RAISED, background=self.cor1)
        self.doces.config(relief=Tkin.RAISED, background=self.cor1)
        self.salgados.config(relief=Tkin.RAISED, background=self.cor1)
        self.massas.config(relief=Tkin.SUNKEN, background=self.cor2)
        self.bebidas.config(relief=Tkin.RAISED, background=self.cor1)
        self.outros.config(relief=Tkin.RAISED, background=self.cor1)
        self.populate(bd.selectProdutoMassas())

    def bebidas_apertado(self):
        self.todos.config(relief=Tkin.RAISED, background=self.cor1)
        self.doces.config(relief=Tkin.RAISED, background=self.cor1)
        self.salgados.config(relief=Tkin.RAISED, background=self.cor1)
        self.massas.config(relief=Tkin.RAISED, background=self.cor1)
        self.bebidas.config(relief=Tkin.SUNKEN, background=self.cor2)
        self.outros.config(relief=Tkin.RAISED, background=self.cor1)
        self.populate(bd.selectProdutoBebidas())

    def outros_apertado(self):
        self.todos.config(relief=Tkin.RAISED, background=self.cor1)
        self.doces.config(relief=Tkin.RAISED, background=self.cor1)
        self.salgados.config(relief=Tkin.RAISED, background=self.cor1)
        self.massas.config(relief=Tkin.RAISED, background=self.cor1)
        self.bebidas.config(relief=Tkin.RAISED, background=self.cor1)
        self.outros.config(relief=Tkin.SUNKEN, background=self.cor2)
        self.populate(bd.selectProdutoOutros())
    # fim

#Construtor
    def __init__(self, root):
        self.todos = Tkin.Button(toolbar, text="   Todos   ", bg=cor1, command=self.todos_apertado)
        self.todos['font'] = ('bold')
        self.todos['fg'] = 'white'
        self.todos.pack(side=Tkin.LEFT, padx=1, pady=1)
        self.doces = Tkin.Button(toolbar, text="   Doces   ", bg=cor1, command=self.doces_apertado)
        self.doces['font'] = ('bold')
        self.doces['fg'] = 'white'
        self.doces.pack(side=Tkin.LEFT, padx=1, pady=1)
        self.salgados = Tkin.Button(toolbar, text="Salgados", bg=cor1, command=self.salgados_apertado)
        self.salgados['font'] = ('bold')
        self.salgados['fg'] = 'white'
        self.salgados.pack(side=Tkin.LEFT, padx=1, pady=1)
        self.massas = Tkin.Button(toolbar, text="  Massas  ", bg=cor1, command=self.massas_apertado)
        self.massas['font'] = ('bold')
        self.massas['fg'] = 'white'
        self.massas.pack(side=Tkin.LEFT, padx=1, pady=1)
        self.bebidas = Tkin.Button(toolbar, text=" Bebidas ", bg=cor1, command=self.bebidas_apertado)
        self.bebidas['font'] = ('bold')
        self.bebidas['fg'] = 'white'
        self.bebidas.pack(side=Tkin.LEFT, padx=1, pady=1)
        self.outros = Tkin.Button(toolbar, text="   Outros   ", bg=cor1, command=self.outros_apertado)
        self.outros['font'] = ('bold')
        self.outros['fg'] = 'white'
        self.outros.pack(side=Tkin.LEFT, padx=1, pady=1)

        toolbar.pack(side=Tkin.TOP, fill=Tkin.X)
        self.cor1 = '#52bbeb'
        self.cor2 = '#E94545'
        self.container1 = Tkin.Frame(root)
        self.container2 = Tkin.Frame(root)
        self.container1.pack(fill=Tkin.X)
        self.container2.pack(side=Tkin.BOTTOM, fill=Tkin.X, padx=15, pady=15)
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
        self.inserir = Tkin.Button(self.container2, text="Inserir", command=lambda:self.inserindo(bd))
        self.inserir["font"] = ("Arial", "10")
        self.inserir['padx'] = 10
        self.inserir.pack(side=Tkin.LEFT)
        self.espaco2 = Tkin.Label(self.container2, text="             ")
        self.espaco2.pack(side=Tkin.LEFT)
        self.editar = Tkin.Button(self.container2, text="Editar", command=lambda:self.editando(bd))
        self.editar["font"] = ("Arial", "10")
        self.editar['padx'] = 10
        self.editar.pack(side=Tkin.LEFT)
        self.espaco2 = Tkin.Label(self.container2, text="             ")
        self.espaco2.pack(side=Tkin.LEFT)
        self.excluir = Tkin.Button(self.container2, text="Excluir", command=lambda:self.deletando(bd))
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
        self.ok = Tkin.Button(self.container2, text="Ok", command=lambda:self.pesquisando(self.pesquisar2.get()))
        self.ok["font"] = ("Arial", "10")
        self.ok['padx'] = 10
        self.ok.pack(side=Tkin.LEFT)
# fim
        self.canvas = None
# tabela dos itens


        self.todos_apertado()

#funcao que cria o canvas, deve ser chamada toda vez que o mesmo e atualizado
    def createCanvas(self):
        Tkin.Frame.__init__(self, root)
        self.canvas = Tkin.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = Tkin.Frame(self.canvas, background="#f0f0f0")
        self.vsb = Tkin.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)
#fim

#Funcao que deleta o canvas, sempre utilizado para atualiza-lo
    def deleteCanvas(self):
        if self.canvas != None:
            self.canvas.destroy()
            self.vsb.destroy()
            self.canvas = None
        return
#fim

#Funcao chamada sempre que o botao inserir e apertado
    def inserindo(self,bd):
        tm.FazTela(bd)
        if(tm.GetWindow()!=None):
            tm.GetWindow().wait_window()
        self.populate(bd.selectProduto())
#fim

#Funcao chamada sempre que o botao editar eh apertado
    def editando(self,bd):
        te.FazTela(bd)
        if(te.GetWindow()!=None):
            te.GetWindow().wait_window()
        self.populate(bd.selectProduto())
#fim

#Funcao chamada sempre que o botao deletar eh apertado
    def deletando(self, bd):
        td.FazTela(bd)
        if (td.GetWindow() != None):
            td.GetWindow().wait_window()
        self.populate(bd.selectProduto())
#fim

#Funcao chamada sempre que o botao pesquisar eh apertado
    def pesquisando(self,id):
        if id == "":
            self.populate(bd.selectProduto())
            return
        else:
            try:
                tr.VerificaDigit(id)
            except:
                tkMessageBox.showerror("Erro encontrado", "Digite valores validos!")
            else:
                self.todos_apertado()
                self.populate(bd.selectProdutoId(self.pesquisar2.get()))

#Funcao que popula o canvas de dados, ele recebe por parametro os dados e formata-o
    def populate(self,info):
        '''Put in some fake data'''
        cor1 = '#ffffff'
        cor2 = '#52bbeb'
        self.deleteCanvas()
        self.createCanvas()

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

#detalhes que o luquinha majna
Example(root).pack(side="top", fill="both", expand=True)
#root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
root.title('Programa Guts')
root.resizable(width=False, height=True)
#root.geometry('755x450')
root.attributes("-fullscreen", True)
root.mainloop()
#fim