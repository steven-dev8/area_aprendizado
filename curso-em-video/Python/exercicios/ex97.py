def escreva(txt):
    tam = len(txt) + 4
    print('+' * tam)
    print(f'{txt.rjust(tam - 2, ' ')}')
    print('+' * tam)

escreva(input())