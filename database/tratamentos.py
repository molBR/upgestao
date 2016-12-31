import database as db
import produto as pr
from datetime import datetime


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



def ObjetivaProduto(id, bd):
    x = bd.selectProdutoId(id)
    p1 = pr.Produto(x[0],x[1],x[2],x[3],x[4])
    return p1

def ProdutosCheck(valor,bd):
    try:
        VerificaDigit(valor)
        if (not bd.ExistsProduto(valor)):
            raise Exception()
    except:
        raise Exception()


def VerificaComma(valor):
    for i in range(len(valor)):
        if (not valor[i].isdigit()):
            if (valor[i] != ","):
                raise Exception(valor)
    return True


def VerificaDigit(valor):
    if (valor.isdigit()):
        return True
    else:
        raise Exception(valor)


def VerificaAlpha(nome):
    if (nome.isalpha()):
        return True
    else:
        raise Exception(nome)


def VerificaTipo(tipo):
    if (tipo == "Tipo de produto"):
        raise Exception(tipo)
    else:
        return True


def TrataStr(nome):
    nome = nome.lower()
    nome = nome.capitalize()
    return nome


def TrataValor(valor):
    if (valor.isdigit()):
        valor = valor + ",00"
    return valor

