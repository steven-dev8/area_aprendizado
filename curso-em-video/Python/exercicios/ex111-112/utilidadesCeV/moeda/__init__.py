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

    dobro = (str((f'{(moeda * 2):.2f}'))).replace('.', ',')
    metade = (str(f'{(moeda / 2):.2f}')).replace('.', ',')
    aumento = (str(f'{(moeda * aumento):.2f}')).replace('.', ',')
    reducao = (str(f'{(moeda * reducao):.2f}')).replace('.', ',')

    return (f'{'RESUMO DO VALOR': >20}\n'
            f'Preço analisado: R${(str(moeda)).replace('.', ',')}\n'
            f'Dobro do preço: R${dobro}\n'
            f'Metade do preço: R${metade}\n'
            f'{aumentar}% de aumento: R${aumento}\n'
            f'{diminuir}% de redução: R${reducao}\n'
            )