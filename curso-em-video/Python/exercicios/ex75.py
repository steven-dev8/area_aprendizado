pares = 0

a = (int(input('Digite o 1 número: ')),
     int(input('Digite o 2 número: ')),
     int(input('Digite o 3 número: ')),
     int(input('Digite o 4 número: ')))

print('='*35)
print(f'Você digitou os valores {a}')
print(f'O número 9 aparece {a.count(9)} vezes')

if 3 in a:
    print(f'O número 3 aparece na posição {a.index(3)+1}')
else:
    print('Não há valores 3 na tupla')
print(f'Os valores pares digitados foram ', end='')

for c in range(0, len(a)):
    if a[c] % 2 == 0:
        print(f'{a[c]}', end=' ')
print()
print('='*35)