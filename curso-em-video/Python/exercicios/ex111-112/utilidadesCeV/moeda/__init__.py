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

def resumo(moeda, aumentar, diminuir):
    aumento = 1 + (aumentar / 100)
    reducao = 1 - (diminuir / 100)

    dobro = (str(((moeda * 2)))).replace('.', ',')
    metade = (str(moeda / 2)).replace('.', ',')
    aumento = (str(moeda * aumento)).replace('.', ',')
    reducao = (str(moeda * reducao)).replace('.', ',')

    return (f'{'RESUMO DO VALOR': >20}\n'
            f'Preço analisado: R${(str(moeda)).replace('.', ',')}\n'
            f'Dobro do preço: R${dobro}\n'
            f'Metade do preço: R${metade}\n'
            f'{aumentar}% de aumento: R${aumento}\n'
            f'{diminuir}% de redução: R${reducao}\n'
            )