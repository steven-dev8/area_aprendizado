lista = []

for c in range(0, 5):
    valor = int(input('Valor: '))
    
    if c == 0:
        lista.append(valor)
        print('O valor foi adicionado no final da lista...')
        
    if c > 0:
        check = 0
        for pos in range (len(lista)):
            if valor > lista[pos]:
                check += 1

        if check == len(lista):
            print('O valor foi adicionado no final da lista...')
            lista.append(valor)
        else:
            lista.insert(check, valor)
            print(f'O valor foi adicionado na posição {check}')
                  
print(lista)