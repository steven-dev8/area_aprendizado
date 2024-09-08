num = int(input('Digite um número de 0 - 9999: '))

u = num // 1 % 10
d = num // 10 % 10

print(f'O número {num}')
print(f'UNIDADE: {u}')
print(f'DEZENA:{d}')
print(f'CENTENA: {num[1]}')
print(f'MILHAR: {num[0]}')