cond = ''
my_list = []

while cond != 'N':
    cond = ''
    add = int(input('Digite um valor: '))

    if add in my_list:
        print(f'Número duplicado, não vou adicionar...')
    else:
        my_list.append(add)
        print(f'Valor adicionado...')

    while cond != 'S' and cond != 'N':
        cond = input('Quer continuar? [S/N]: ').upper()[0]
        
my_list.sort()
print(f'Você digitou os valores {my_list}')
