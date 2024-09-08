my_list = []
check = True

while check:
    option = ''
    number = int(input('Number: '))
    my_list.append(number)
    
    while option != 'S' and option != 'N':
        option = input('Deseja continuar? [S/N] ').upper()[0]
        if option == 'N':
            check = False
    
print('-=' * 12)
my_list.sort(reverse=True)
print(f'Foram digitados {len(my_list)} números')
print('Os valores da lista são:', end =' ')
print(*my_list, sep=' ')

if 5 in my_list:
    print('A lista possui pelo menos um número 5')
else:
    print('A lista não possui número 5')