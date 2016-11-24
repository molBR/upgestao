from Tkinter import *

def Teste():
    print("Testado")
def Help():
    root=Tk()

    cor1 = '#D32F2F'

    # funcao para teste


    # opcoes do droplist

    OPTIONS = [
        "Tipo de produto",
        "Doce",
        "Salgado",
        "Massa",
        "Bebida",
        "Outro"
    ]

    # criacao e posicao dos widgets

    info = Frame(root)
    info.grid(sticky=N+S+W+E)

    salto1 = Label(info, text="       ")
    salto1.grid(row=0, column=0)

    objeto1 = Label(info, text="Nome:")
    objeto1['font']=['bold']
    objeto1.grid(row=1, column=1, sticky=W)

    objeto2 = Entry(info)
    objeto2["width"]=40
    objeto2.grid(row=2, column=1)

    salto2 = Label(info, text="")
    salto2.grid(row=3, column=0)

    objeto3 = Label(info, text="Valor:")
    objeto3['font']=['bold']
    objeto3.grid(row=4, column=1, sticky=W)

    objeto4 = Entry(info)
    objeto4["width"]=40
    objeto4.grid(row=5, column=1)

    salto3 = Label(info, text="")
    salto3.grid(row=6, column=0)

    variable = StringVar(info)
    variable.set(OPTIONS[0])

    objeto5 = apply(OptionMenu, (info, variable) + tuple(OPTIONS))
    objeto5.grid(row=7, column=1)

    salto4 = Label(info, text="")
    salto4.grid(row=8, column=0)

    objeto6 = Button(info, text="Pronto", bg=cor1, bd=3, command=Teste)
    objeto6['font']=['bold']
    objeto6['fg']='white'
    objeto6.grid(row=9, column=1)

    salto5 = Label(info, text="")
    salto5.grid(row=10, column=1)

    espaco1 = Label(info, text="       ")
    espaco1.grid(row=10, column=2)

    # barra de "status"

    status = Label(info, text="Estado: Normal", bg="white", bd=1, relief=SUNKEN, anchor=W)
    status.grid(row= 11, column=0, sticky=S+W+E, columnspan=3)

    # formatacao da janela

    root.title('Cadastro do Produto')
    ##root.iconbitmap(r'c:\Python27\DLLs\icon.ico')
    root.resizable(width=False, height=False)
    root.geometry('298x276')
    root.mainloop()