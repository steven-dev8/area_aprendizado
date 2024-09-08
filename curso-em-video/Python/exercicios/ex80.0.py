lista = []

for c in range(0, 5):
    valor = int(input('Digite um número para adicionar na lista: '))
    
    if c == 0:
        lista.append(valor)
        print('O valor foi adicionado no final da lista...')

    if c == 1:
        if valor > lista[0]:
            lista.append(valor)
            print('O valor foi adicionado no final da lista...')
        else:
            lista.insert(0, valor)
            print('O valor foi adicionado na posição 0')
            
    if c == 2:
        if valor > lista[0]:
            if valor > lista[1]:
                lista.append(valor)
                print('O valor foi adicionado no final da lista...')
            else:
                lista.insert(1, valor)
                print('O valor foi adicionado na posição 1')
        else:
            lista.insert(0, valor)
            print('O valor foi adicionado na posição 0')

    if c == 3:
        if valor > lista[0]:
            if valor > lista[1]:
                if valor > lista[2]:
                    lista.append(valor)
                    print('O valor foi adicionado no final da lista...')
                else:
                    lista.insert(2, valor)
                    print('O valor foi adicionado na posição 2')
            else:
                lista.insert(1, valor)
                print('O valor foi adicionado na posição 1')
        else:
            lista.insert(0, valor)
            print('O valor foi adicionado na posição 0')
    
    if c == 4:
        if valor > lista[0]:
            if valor > lista[1]:
                if valor > lista[2]:
                    if valor > lista[3]:
                        lista.append(valor)
                        print('O valor foi adicionado no final da lista...')
                    else:
                        lista.insert(3, valor)
                        print('O valor foi adicionado na posição 3')
                else:
                    lista.insert(2, valor)
                    print('O valor foi adicionado na posição 2')
            else:
                lista.insert(1, valor)
                print('O valor foi adicionado na posição 1')
        else:
            lista.insert(0, valor)
            print('O valor foi adicionado na posição 0')
print(lista)