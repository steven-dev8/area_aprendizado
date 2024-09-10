#Exercício 107
def aumentar(moeda, porcentagem):
    porcentagem = (porcentagem / 100) + 1
    return moeda * porcentagem

def diminuir(moeda, porcentagem):
    porcentagem = 1 - (porcentagem / 100)
    return moeda * porcentagem

def dobro(moeda):
    return moeda * 2

def metade(moeda):
    return moeda / 2

#Exercício 108
def conversao(moeda):
    return f'R${moeda}'