from Tkinter import *

root=Tk()

cor1 = '#D32F2F'

# funcao para teste
def Teste():
    print("Testado")
#fim

# opcoes do droplist
OPTIONS = [
    "Tipo de produto",
    "Doce",
    "Salgado",
    "Massa",
    "Bebida",
    "Outro"
    ]
#fim

# criacao e posicao dos widgets
info = Frame(root)
info.grid(sticky=N+S+W+E)

salto1 = Label(info, text="       ")
salto1.grid(row=0, column=0)

nome1 = Label(info, text="Nome:")
nome1['font']=['bold']
nome1.grid(row=1, column=1, sticky=W)

nome2 = Entry(info)
nome2["width"]=40
nome2.grid(row=2, column=1)
nome = nome2.get() #pesquisado = o que foi escrito no "Entry / barra de pesquisa"

salto2 = Label(info, text="")
salto2.grid(row=3, column=0)

valor1 = Label(info, text="Valor:")
valor1['font']=['bold']
valor1.grid(row=4, column=1, sticky=W)

valor2 = Entry(info)
valor2["width"]=40
valor2.grid(row=5, column=1)
valor = valor2.get() #pesquisado = o que foi escrito no "Entry / barra de pesquisa"

salto3 = Label(info, text="")
salto3.grid(row=6, column=0)

variable = StringVar(info)
variable.set(OPTIONS[0])

droplist = apply(OptionMenu, (info, variable) + tuple(OPTIONS))
droplist.grid(row=7, column=1)

salto4 = Label(info, text="")
salto4.grid(row=8, column=0)

pronto = Button(info, text="Pronto", bg=cor1, bd=3, command=Teste)
pronto['font']=['bold']
pronto['fg']='white'
pronto.grid(row=9, column=1)

salto5 = Label(info, text="")
salto5.grid(row=10, column=1)

espaco1 = Label(info, text="       ")
espaco1.grid(row=10, column=2)
#fim

# barra de "status"
status = Label(info, text="Estado: Normal", bg="white", bd=1, relief=SUNKEN, anchor=W)
status.grid(row= 11, column=0, sticky=S+W+E, columnspan=3)
#fim

# formatacao da janela
root.title('Cadastro do Produto')
    #root.iconbitmap(r'c:\Python27\DLLs\icon.ico')
root.resizable(width=False, height=False)
root.geometry('298x276')
root.mainloop()
#fim