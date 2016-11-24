from Tkinter import *
import cadastro_produto_menor as cpm
root=Tk()

# funcao para teste

def Teste():
    print("Testado")

# menu principal

menu = Menu(root)
root.config(menu=menu)

subMenu1 = Menu(menu)
menu.add_cascade(label="Arquivo", menu=subMenu1)
subMenu1.add_command(label="Novo", command=Teste)
subMenu1.add_command(label="Salvar", command=Teste)
subMenu1.add_separator()
subMenu1.add_command(label="Sair", command=Teste)

subMenu2 = Menu(menu)
menu.add_cascade(label="Editar", menu=subMenu2)
subMenu2.add_command(label="Copiar", command=Teste)
subMenu2.add_command(label="Colar", command=Teste)
subMenu2.add_command(label="Cortar", command=Teste)

subMenu3 = Menu(menu)
menu.add_cascade(label="Visualizar", menu=subMenu3)
subMenu3.add_command(label="Ferramentas", command=Teste)
subMenu3.add_command(label="Arquivo Recente", command=Teste)

# abas de opcoes

cor1 = '#D32F2F'

toolbar = Frame(root, bg=cor1)

opcao1 = Button(toolbar, text="   Doces   ", bg=cor1,  command=Teste)
opcao1['font']=('bold')
opcao1['fg']='white'
opcao1.pack(side=LEFT, padx=2, pady=2)
opcao2 = Button(toolbar, text="Salgados", bg=cor1, command=Teste)
opcao2['font']=('bold')
opcao2['fg']='white'
opcao2.pack(side=LEFT, padx=2, pady=2)
opcao3 = Button(toolbar, text="  Massas  ", bg=cor1, command=Teste)
opcao3['font']=('bold')
opcao3['fg']='white'
opcao3.pack(side=LEFT, padx=2, pady=2)
opcao4 = Button(toolbar, text="  Bebidas  ", bg=cor1, command=Teste)
opcao4['font']=('bold')
opcao4['fg']='white'
opcao4.pack(side=LEFT, padx=2, pady=2)
opcao5 = Button(toolbar, text="   Outros   ", bg=cor1, command=Teste)
opcao5['font']=('bold')
opcao5['fg']='white'
opcao5.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# barra de 'status'

status = Label(root, text="Estado: Normal", bg="white", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# informacoes gerais

class Janela:
    def __init__(self,instancia_Tk):

        instancia_Tk.title('Programa Guts')

        self.container1 = Frame(instancia_Tk)
        self.container2 = Frame(instancia_Tk)
        self.container3 = Frame(instancia_Tk)
        self.container4 = Frame(instancia_Tk)
        self.container5 = Frame(instancia_Tk)
        self.container6 = Frame(instancia_Tk)
        self.container7 = Frame(instancia_Tk)
        self.container8 = Frame(instancia_Tk)
        self.container9 = Frame(instancia_Tk)
        self.container10 = Frame(instancia_Tk)
        self.container11 = Frame(instancia_Tk)
        self.container12 = Frame(instancia_Tk)
        self.container13 = Frame(instancia_Tk)
        self.container14 = Frame(instancia_Tk)
        self.container15 = Frame(instancia_Tk)
        self.container16 = Frame(instancia_Tk)
        self.container17 = Frame(instancia_Tk)
        self.container18 = Frame(instancia_Tk)
        self.container1.pack()
        self.container2.pack()
        self.container3.pack()
        self.container4.pack()
        self.container5.pack()
        self.container6.pack()
        self.container7.pack()
        self.container8.pack()
        self.container9.pack()
        self.container10.pack()
        self.container11.pack()
        self.container12.pack()
        self.container13.pack()
        self.container14.pack()
        self.container15.pack()
        self.container16.pack()
        self.container17.pack()
        self.container18.pack()

        self.objeto1 = Label(self.container1, text="Codigo:")
        self.objeto1["font"]=["bold"]
        self.objeto1.pack(side=LEFT)
        self.espaco1 = Label(self.container1, text="                                               ")
        self.espaco1.pack(side=LEFT)
        self.objeto2 = Label(self.container1, text="Nome:")
        self.objeto2["font"]=["bold"]
        self.objeto2.pack(side=LEFT)
        self.espaco2 = Label(self.container1, text="                                               ")
        self.espaco2.pack(side=LEFT)
        self.espaco3 = Label(self.container1, text="                                               ")
        self.espaco3.pack(side=LEFT)
        self.objeto3 = Label(self.container1, text="Valor:")
        self.objeto3["font"]=["bold"]
        self.objeto3.pack(side=LEFT)
        self.espaco4 = Label(self.container1, text="                                               ")
        self.espaco4.pack(side=LEFT)

        self.salto1 = Label(self.container2, text="")
        self.salto1.pack()
        self.salto2 = Label(self.container3, text="")
        self.salto2.pack()
        self.salto3 = Label(self.container4, text="")
        self.salto3.pack()
        self.salto4 = Label(self.container5, text="")
        self.salto4.pack()
        self.salto5 = Label(self.container6, text="")
        self.salto5.pack()
        self.salto6 = Label(self.container7, text="")
        self.salto6.pack()
        self.salto7 = Label(self.container8, text="")
        self.salto7.pack()
        self.salto8 = Label(self.container9, text="")
        self.salto8.pack()
        self.salto9 = Label(self.container10, text="")
        self.salto9.pack()
        self.salto10 = Label(self.container11, text="")
        self.salto10.pack()
        self.salto11 = Label(self.container12, text="")
        self.salto11.pack()
        self.salto12 = Label(self.container13, text="")
        self.salto12.pack()
        self.salto13 = Label(self.container14, text="")
        self.salto13.pack()
        self.salto14 = Label(self.container15, text="")
        self.salto14.pack()
        self.salto15 = Label(self.container16, text="")
        self.salto15.pack()

        self.objeto4 = Button(self.container17, text="Inserir",command=cpm.Help) 
        self.objeto4["font"] = ("Arial", "10")
        self.objeto4['padx'] = 10
        self.objeto4.pack(side=LEFT)
        self.espaco5 = Label(self.container17, text="    ")
        self.espaco5.pack(side=LEFT)
        self.objeto5 = Button(self.container17, text="Editar")
        self.objeto5["font"] = ("Arial", "10")
        self.objeto5['padx'] = 10
        self.objeto5.pack(side=LEFT)
        self.espaco6 = Label(self.container17, text="    ")
        self.espaco6.pack(side=LEFT)
        self.objeto6 = Button(self.container17, text="Excluir")
        self.objeto6["font"] = ("Arial", "10")
        self.objeto6['padx'] = 10
        self.objeto6.pack(side=LEFT)
        self.espaco7 = Label(self.container17, text="    ")
        self.espaco7.pack(side=LEFT)
        self.objeto7 = Label(self.container17, text="Pesquisar:")
        self.objeto7["font"] = ("Arial", "10")
        self.objeto7.pack(side=LEFT)
        self.objeto8 = Entry(self.container17)
        self.objeto8["width"] = 25
        self.objeto8["font"] = ("Arial", "10")
        self.objeto8.pack(side=LEFT)

Janela(root)
##root.iconbitmap(r'icon.ico') # so funciona se a imagem estiver dentro dessa pasta
root.resizable(width=False, height=False)
root.geometry('750x450')
root.mainloop()