from random import randint

def sorteia():

    lista = [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]
    print('Sorteando 5 valores da lista: ', end = '')
    print(*lista, sep=' ', end=' ')
    print('PRONTO!')
    return lista

def somapar(lista):
    soma = 0
    for j in lista:
        if j % 2 == 0:
            soma += j
    print(f'Somando os valores pares de {lista}, temos {soma}')

somapar(sorteia())
