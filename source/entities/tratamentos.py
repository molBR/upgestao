# encoding: utf-8

from datetime import datetime

import cliente as cl
import produto as pr
import venda as ve


#Classes criadas para caracterizar os erros do programa - Não utilizadas no momento

class Erro(Exception):
    def __init__(self, expression='null', message='null'):
        self.expression = expression
        self.message = message

class ErroEntrada(Erro):
   def __init__(self, expression='null', message='null'):
        self.expression = expression
        self.message = message

class ErroIntegridade(Erro):
   def __init__(self, expression='null', message='null'):
       self.expression = expression
       self.message = message

#Tratamento de dados
def ProdutosReceive(id, nome, valor, tipo,bd):
    try:
        VerificaDigit(id)
        VerificaAlpha(nome)
        VerificaComma(valor)
        VerificaTipo(tipo)
    except Erro as e:
        raise e             #Apenas repassando os possiveis erros para o nivel superior
    else:
        nome = TrataStr(nome)
        valor = TrataValor(valor)
        agora = datetime.now().strftime('%d/%m/%y - %H:%M:%S')
        if (tipo == "Doce"): tipo = 1
        if (tipo == "Salgado"): tipo = 2
        if (tipo == "Massa"): tipo = 3
        if (tipo == "Bebida"): tipo = 4
        if (tipo == "Outro"): tipo = 5
        p1 = pr.Produto(id, nome, valor, agora, tipo)
        return p1
#fim

def ClientesReceive(nome,endereco,telefone,email):
    try:
        verificaArroba(email)
        verificaTamTel(telefone)
    except Erro as e:
        raise e
    else:
        agora = datetime.now().strftime('%d/%m/%y - %H:%M:%S')
        c1 = cl.Cliente(None,nome,agora,endereco,telefone,email)
        return c1

def EventosReceive(tipo,Clientes,rua,numero,bairro,complemento,adultos,criancas,data):
    try:
        VerificaDigit(numero)
        VerificaDigit(adultos)
        VerificaDigit(criancas)
    except Erro as e:
        raise e
    else:
        agora = datetime.now().strftime('%d/%m/%y - %H:%M:%S')
        t1 = ve.Venda(0,Clientes.getNome(),tipo,adultos,criancas,Clientes.getEndereco(),Clientes.getTelefone(),
                      Clientes.getEmail(),data,agora,None,None,None,None)
        return t1

def verificaArroba(email):
    print len(email)
    for i in range(0,len(email)):
        if(email[i]=='@'):
            return True
    raise ErroEntrada(email,"O e-mail não tem '@'")

def verificaTamTel(telefone):
    print "bbb"
    if len(telefone)>15:
        raise ErroEntrada(telefone, "Tamanho do telefone é inválido")
    else: return True

def swapComma2Dot(valor):
    auxValue = ''
    for i in range(len(valor)):
        if (valor[i] == ','):
            auxValue+= '.'
        else:
            auxValue+= valor[i]
    return auxValue

def swapDot2Comma(valor):
    auxValue = ''
    for i in range(len(valor)):
        if (valor[i] == '.'):
            auxValue+= ','
        else:
            auxValue+= valor[i]
    return auxValue

def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i].getprodInfo()[0] < righthalf[j].getprodInfo()[0]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist

#Recebe um id, faz a consulta no bd cria um objeto com as info do produto.
def ObjetivaProduto(id, bd):
    x = bd.selectProdutoId(id)
    p1 = pr.Produto(x[0],x[1],x[2],x[3],x[4])
    return p1

#Checa se existe um produto com o id
def ProdutosCheck(valor,bd):
    VerificaDigit(valor)
    if (not bd.ExistsProduto(valor)):
        raise ErroIntegridade(valor, "O ID digitado: \"" + str(valor) + "\" não existe no atual banco de dados. Por favor, digite novamente.")

#Tratamento do valor
def VerificaComma(valor):
    for i in range(len(valor)):
        if (not valor[i].isdigit()):
            if (valor[i] != ","):
                raise ErroEntrada(valor, "O valor deve apresentar apenas números e vírgula(s).")
    return True

#Verifica se a string eh um numero
def VerificaDigit(valor):
    if (valor.isdigit()):
        return True
    else:
        raise ErroEntrada(valor, "O texto deve apenas ser composto por números.")

#Verifica se a string tem somente letras
def VerificaAlpha(nome):
    if (nome.isalpha()):
        return True
    else:
        raise ErroEntrada(nome, "O texto deve apenas ser composto por letras.")

#Verifica se o produto eh de uma categoria valida
def VerificaTipo(tipo):
    if (tipo == "Tipo de produto"):
        raise ErroEntrada(tipo, "O produto digitado não possui uma categoria válida. Por favor, escolha uma categoria.")
    else:
        return True

#Faz o tramento, deixando todas as letras minusculas e colocando a primeira letra maiuscula
def TrataStr(nome):
    nome = nome.lower()
    nome = nome.capitalize()
    return nome

#Faz um tratamento do valor
def TrataValor(valor):
    if (valor.isdigit()):
        valor = valor + ",00"
    return valor

