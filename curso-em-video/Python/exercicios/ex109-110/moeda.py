#Exercício 109
def aumentar(moeda, porcentagem, condition=False):
    porcentagem = 1 + (porcentagem / 100)

    if condition:
        return f'R${(moeda * porcentagem):.2f}'
    
    return moeda * porcentagem

def diminuir(moeda, porcentagem, condition=False):
    porcentagem = 1 - (porcentagem / 100)

    if condition:
        return f'R${(moeda * porcentagem):.2f}'
    
    return moeda * porcentagem

def dobro(moeda, condition=False):
    if condition:
        return f'R${(moeda * 2):.2f}'
    
    return moeda * 2

def metade(moeda, condition=False):
    if condition:
        return f'R${(moeda / 2):.2f}'
    
    return moeda / 2

#Exercício 110

def resumo(moeda, aumentar, diminuir):
    aumento = 1 + (aumentar / 100)
    reducao = 1 - (diminuir / 100)

    return (f'{'RESUMO DO VALOR': >20}\n'
            f'Preço analisado: R${(moeda):.2f}\n'
            f'Dobro do preço: R${(moeda * 2):.2f}\n'
            f'Metade do preço: R${(moeda / 2):.2f}\n'
            f'{aumentar}% de aumento: R${(moeda * aumento):.2f}\n'
            f'{diminuir}% de redução: R${(moeda * reducao):.2f}\n'
            )