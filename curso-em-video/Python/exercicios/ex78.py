lista = []
cont = cont1 = 0

for n in range(0, 5):
    a = int(input(f'Digite um valor para a posição {n}: '))
    lista.append(a)

lista1 = lista[:]
lista.sort()

print(f'O menor valor da lista é {lista[0]} que estão nas posições: ', end='')
for c, v in enumerate(lista1):
    if lista[0] == v:
        print(c, end='...')

print()
        
print(f'O maior valor da lista é {lista[4]} que estão nas posições: ', end='')
for c, v in enumerate(lista1):
    if lista[4] == v:
        print(c, end='...')
