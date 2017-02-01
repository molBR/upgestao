from Tkinter import *

root = Tk()

cor1 = '#ffffff'
cor2 = '#d32f2f'

# comeco titulo e imagem
frame1 = Frame (root, background=cor1)
frame1.grid(row=0, column=0)

salto1 = Label (frame1, text="                ", bg=cor1)
salto1.grid(row=0, column=0)

salto2 = Label (frame1, text="", bg=cor1)
salto2.grid(row=1, column=0)

titulo = Label (frame1, text="Programa Guts", bg=cor1, fg=cor2)
titulo["font"]=("Arial", "44", "bold")
titulo.grid(row=2, column=1)

salto3 = Label (frame1, text="                ", bg=cor1)
salto3.grid(row=3, column=2)

photo = PhotoImage(file="menu.gif")
logo = Label(frame1, image=photo, bg=cor1)
logo.grid(row=4, column=1)

salto4 = Label (frame1, text="", bg=cor1)
salto4.grid(row=5, column=0)


# fim

# comeco botoes
frame2 = Frame (root, background=cor1)
frame2.grid(row=0, column=1)

salto1 = Label (frame2, text="                       ", bg=cor1)
salto1.grid(row=0, column=0)
salto2 = Label (frame2, text="", bg=cor1)
salto2.grid(row=1, column=0)
salto3 = Label (frame2, text="", bg=cor1)
salto3.grid(row=2, column=0)
salto4 = Label (frame2, text="", bg=cor1)
salto4.grid(row=3, column=0)
salto5 = Label (frame2, text="", bg=cor1)
salto5.grid(row=4, column=0)
salto6 = Label (frame2, text="", bg=cor1)
salto6.grid(row=5, column=0)
salto7 = Label (frame2, text="", bg=cor1)
salto7.grid(row=6, column=0)

venda = Button(frame2, text="        Nova  Venda        ", bg=cor2, fg=cor1, bd=2)
venda["font"]=("Arial", "16", "bold")
venda.grid(row=7, column=1, pady=5)

salto8 = Label (frame2, text="                       ", bg=cor1)
salto8.grid(row=8, column=2)

cadastro = Button(frame2, text="    Cadastrar Cliente    ", bg=cor2, fg=cor1, bd=2)
cadastro["font"]=("Arial", "16", "bold")
cadastro.grid(row=9, column=1, pady=5)

salto9 = Label (frame2, text="", bg=cor1)
salto9.grid(row=10, column=1)

historico = Button(frame2, text="  Historico de Vendas  ", bg=cor2, fg=cor1, bd=2)
historico["font"]=("Arial", "16", "bold")
historico.grid(row=11, column=1, pady=5)

salto10 = Label (frame2, text="", bg=cor1)
salto10.grid(row=12, column=2)

inserir = Button(frame2, text="      Inserir  Produto      ", bg=cor2, fg=cor1, bd=2)
inserir["font"]=("Arial", "16", "bold")
inserir.grid(row=13, column=1, pady=5)

salto11 = Label (frame2, text="", bg=cor1)
salto11.grid(row=14, column=0)
salto12 = Label (frame2, text="", bg=cor1)
salto12.grid(row=15, column=2)
salto13 = Label (frame2, text="", bg=cor1)
salto13.grid(row=16, column=2)
salto14 = Label (frame2, text="", bg=cor1)
salto14.grid(row=17, column=0)
salto15 = Label (frame2, text="", bg=cor1)
salto15.grid(row=18, column=2)
salto16 = Label (frame2, text="", bg=cor1)
salto16.grid(row=19, column=2)
salto17 = Label (frame2, text="", bg=cor1)
salto17.grid(row=20, column=2)
# fim botoes

# barra de 'status'
status = Label(root, text="Estado: Rodando", bg="white", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=1, column=0, sticky=S+W+E, columnspan=2)
# fim

#root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
root.title('Programa Guts')
root.resizable(width=False, height=False)
root.geometry('1061x581')
root.mainloop()