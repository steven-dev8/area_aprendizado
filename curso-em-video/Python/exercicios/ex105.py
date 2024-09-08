from time import sleep

def nota(*num, sit=False):
    """
    """
    dicionario = {
        'total':len(num),
        'maior':max(num),
        'menor':min(num),
        'media':sum(num)/len(num)
    }
    if sit:
        if dicionario['media'] < 5:
            dicionario['situação'] = 'RUIM'
        elif dicionario['media'] < 7:
            dicionario['situação'] = 'RAZOAVEL'
        else:
            dicionario['situação'] = 'BOA'
        print(dicionario)
    else:
        print(dicionario)

    return dicionario

nota(10, 9, 7, 9)
help(nota)