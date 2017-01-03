import database as db
import produto as pr
from datetime import datetime

#Tratamento da insercao
def ProdutosRecieve(id, nome, valor, tipo,bd):
    try:
        VerificaDigit(id)
        VerificaAlpha(nome)
        VerificaComma(valor)
        VerificaTipo(tipo)
    except:
        raise Exception()
    else:
        nome = TrataStr(nome)
        valor = TrataValor(valor)
        agora = datetime.now().strftime('%H:%M:%S')
        if (tipo == "Doce"): tipo = 1
        if (tipo == "Salgado"): tipo = 2
        if (tipo == "Massa"): tipo = 3
        if (tipo == "Bebida"): tipo = 4
        if (tipo == "Outro"): tipo = 5
        p1 = pr.Produto(id, nome, valor, agora, tipo)
        return p1
#fim

#Recebe um id, faz a consulta no bd cria um objeto com as info do produto.
def ObjetivaProduto(id, bd):
    x = bd.selectProdutoId(id)
    p1 = pr.Produto(x[0],x[1],x[2],x[3],x[4])
    return p1

#Checa se existe um produto com o id
def ProdutosCheck(valor,bd):
    try:
        VerificaDigit(valor)
        if (not bd.ExistsProduto(valor)):
            raise Exception()
    except:
        raise Exception()

#Tratamento do valor
def VerificaComma(valor):
    for i in range(len(valor)):
        if (not valor[i].isdigit()):
            if (valor[i] != ","):
                raise Exception(valor)
    return True

#Verifica se a string eh um numero
def VerificaDigit(valor):
    if (valor.isdigit()):
        return True
    else:
        raise Exception(valor)

#Verifica se a string tem somente letras
def VerificaAlpha(nome):
    if (nome.isalpha()):
        return True
    else:
        raise Exception(nome)

#Verifica se o produto eh de uma categoria valida
def VerificaTipo(tipo):
    if (tipo == "Tipo de produto"):
        raise Exception(tipo)
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

