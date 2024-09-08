def fatorial(a=0, show=False):
    """Calcula o fatorial de um número

    Args:
        a (int, opcional): O número a ser calculado.
        show (bool, opcional): Mostra ou não a conta.
        return (retorno): O valor do fatorial de um número a.
    """
    FATORIAL = 1

    if show:
        for i in range(a , 0, -1):
            if i > 1:
                print(f'{i}', end = ' x ') 
                FATORIAL *= i
            else:
                print(f'{i} = {FATORIAL}')
                FATORIAL *= i
        return FATORIAL
        
    

print('-' * 30)
fatorial(10, show=True)