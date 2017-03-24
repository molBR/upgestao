# encoding: utf-8

from Tkinter import *

root=Tk()

cor1 = '#E6E6E6'
cor2 = '#D32F2F'

info1 = Frame(root)
info1.grid(sticky=N+W+E)

salto1 = Label(info1, text="          ")
salto1.grid(row=0, column=0)

nome1 = Label(info1, text="Nome:")
nome1['font']=['bold']
nome1.grid(row=1, column=1, sticky=W)
nome2 = Entry(info1)
nome2["width"]=40
nome2["font"] = ("Arial", "10")
nome2.grid(row=2, column=1)

salto2 = Label(info1, text="          ")
salto2.grid(row=0, column=2)

endereco1 = Label(info1, text="Endereco:")
endereco1['font']=['bold']
endereco1.grid(row=1, column=3, sticky=W)
endereco2 = Entry(info1)
endereco2["width"]=40
endereco2["font"] = ("Arial", "10")
endereco2.grid(row=2, column=3)

salto3 = Label(info1, text="          ")
salto3.grid(row=0, column=4)

salto4 = Label(info1, text="")
salto4.grid(row=3, column=0)

data1 = Label(info1, text="Data:")
data1['font']=['bold']
data1.grid(row=4, column=1, sticky=W)
data2 = Entry(info1)
data2["width"]=40
data2["font"] = ("Arial", "10")
data2.grid(row=5, column=1)

email1 = Label(info1, text="E-mail:")
email1['font']=['bold']
email1.grid(row=4, column=3, sticky=W)
email2 = Entry(info1)
email2["width"]=40
email2["font"] = ("Arial", "10")
email2.grid(row=5, column=3)

salto5 = Label(info1, text="")
salto5.grid(row=6, column=0)

telefone1 = Label(info1, text="Telefone:")
telefone1['font']=['bold']
telefone1.grid(row=7, column=1, sticky=W)
telefone2 = Entry(info1)
telefone2["width"]=40
telefone2["font"] = ("Arial", "10")
telefone2.grid(row=8, column=1)

celular1 = Label(info1, text="Celular:")
celular1['font']=['bold']
celular1.grid(row=7, column=3, sticky=W)
celular2 = Entry(info1)
celular2["width"]=40
celular2["font"] = ("Arial", "10")
celular2.grid(row=8, column=3)

salto6 = Label(info1, text="")
salto6.grid(row=9, column=0)

festa1 = Label(info1, text="Tipo de Festa:")
festa1['font']=['bold']
festa1.grid(row=10, column=1, sticky=W)
festa2 = Entry(info1)
festa2["width"]=40
festa2["font"] = ("Arial", "10")
festa2.grid(row=11, column=1)

cliente1 = Label(info1, text="Instituicao/Cliente:")
cliente1['font']=['bold']
cliente1.grid(row=10, column=3, sticky=W)
cliente2 = Entry(info1)
cliente2["width"]=40
cliente2["font"] = ("Arial", "10")
cliente2.grid(row=11, column=3)

salto7 = Label(info1, text="")
salto7.grid(row=12, column=0)

npessoas1 = Label(info1, text="Numero de Pessoas:")
npessoas1['font']=['bold']
npessoas1.grid(row=13, column=1, sticky=W)
npessoas2 = Entry(info1)
npessoas2["width"]=40
npessoas2["font"] = ("Arial", "10")
npessoas2.grid(row=14, column=1)

local1 = Label(info1, text="Espaco/Local:")
local1['font']=['bold']
local1.grid(row=13, column=3, sticky=W)
local2 = Entry(info1)
local2["width"]=40
local2["font"] = ("Arial", "10")
local2.grid(row=14, column=3)

salto8 = Label(info1, text="")
salto8.grid(row=15, column=0)

info2 = Frame(root, bg=cor1)
info2.grid(sticky=S+W+E)

espaco1 = Label(info2, text="               ", bg=cor1)
espaco1.grid(row=0, column=0)

pesquisar1 = Label(info2, text="Pesquisar: ", bg=cor1)
pesquisar1["font"]=['bold']
pesquisar1.grid(row=1, column=1)
pesquisar2 = Entry(info2)
pesquisar2["width"] = 40
pesquisar2["font"] = ("Arial", "10")
pesquisar2.grid(row=1, column=2)
espaco2 = Label(info2, text=" ", bg=cor1)
espaco2.grid(row=1, column=3)
ok = Button(info2, text="Ok", bg=cor1)
ok["font"]=['bold']
ok['padx']=1
ok['pady']=1
ok.grid(row=1, column=4)

espaco3 = Label(info2, text="                    ", bg=cor1)
espaco3.grid(row=1, column=5)

pronto = Button(info2, text="Pronto", bg=cor2)
pronto["font"]=['bold']
pronto['fg']='white'
pronto['padx']=1
pronto['pady']=1
pronto.grid(row=1, column=6)

espaco4 = Label(info2, text="                   ", bg=cor1)
espaco4.grid(row=2, column=7)

status = Label(info2, text="Estado: Normal", bg="white", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=3, column=0, sticky=S + W + E, columnspan=8)


#root.iconbitmap(r'C:\Python27\DLLs\icon.ico')
root.title('Dados da Venda')
root.resizable(width=False, height=False)
root.mainloop()