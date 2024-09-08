cont = 0
palavras = ('cebola', 'alho', 'cenoura', 'arroz')
vogais = ('a', 'e', 'i', 'o', 'u')

while True:
    print(f'A palavra "{palavras[cont]}" tem as vogais: ', end='')
    for i in range(0,len(vogais)):
        if vogais[i] in palavras[cont]:
            print(vogais[i], end=' ')
    print()
    
    cont += 1
    if cont == 4:
        break