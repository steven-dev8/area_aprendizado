matriz = [[], [], []]
linha = coluna =0

while True:
    matriz[linha].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))
    coluna += 1

    if coluna == 3:
        linha += 1
        coluna = 0
    if linha == 3:
        break

print('-=' * 20)
print(f'[  {matriz[0][0]}  ][  {matriz[0][1]}  ][  {matriz[0][2]}  ]')
print(f'[  {matriz[1][0]}  ][  {matriz[1][1]}  ][  {matriz[1][2]}  ]')
print(f'[  {matriz[2][0]}  ][  {matriz[2][1]}  ][  {matriz[2][2]}  ]')