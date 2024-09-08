number = [[], []]

for i in range(7):
    numero = int(input(f'Número {i+1}: '))

    if numero % 2 == 0:
        number[0].append(numero)
    else:
        number[1].append(numero)

number[0].sort()
number[1].sort()

print(f'Os valores ímpares digitados foram {number[1]}')
print(f'Os valores pares digitados foram {number[0]}')
