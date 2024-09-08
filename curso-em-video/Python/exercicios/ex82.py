my_list = []
imp_list = []
pares_list = []
check = True

while check:
    op = ''
    number = int(input('Número: '))

    my_list.append(number)
    if number % 2 == 0:
        pares_list.append(number)
    else:
        imp_list.append(number)

    while op != 'S' and op != 'N':
        op = input('Deseja continuar? [S/N] ').upper()[0]
        if op == 'N':
            check = False

print('-=' * 12)
print(f'Lista completa: {my_list}')
print(f'Lista com números ímpares: {imp_list}')
print(f'Lista com números pares: {pares_list}')