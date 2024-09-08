matriz = [[], [], []]
linha_atual = coluna_atual = soma = soma_pares = 0

while linha_atual != 3:
    matriz[linha_atual].append(int(input(f'Digite um valor para [{linha_atual}, {coluna_atual}]: ')))
    coluna_atual += 1

    if coluna_atual == 3:
        linha_atual += 1
        coluna_atual = 0

for x in range(3):
    for y in range(3):
        if matriz[x][y] % 2 == 0:
            soma_pares += matriz[x][y]

for i in range(3):
    soma += matriz[i][2]

print('-=' * 20)
for linha in matriz:
    print(f'[  {linha[0]}  ][  {linha[1]}  ][  {linha[2]}  ]')

print(f'A soma de todos os valores pares digitados é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')