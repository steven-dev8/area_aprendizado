from random import randint

dados = {
    input('Nome do jogador 1: '):[randint(1, 6)],
    input('Nome do jogador 2: '):[randint(1, 6)],
    input('Nome do jogador 3: '):[randint(1, 6)],
    input('Nome do jogador 4: '):[randint(1, 6)],
}

for i, j in dados.items():
    print(f'Jogador {i} tirou {j}')
print('-=' * 30)

# dict transforma os meus dados de volta em um dicionário. dados.items() retorna uma lista de keys e values para serem ordenados.
# key=lambda item: item[1] especifica que a ordenação deve ser feita com base nos values (item[1]) dos pares, caso seja com keys o item tem que ser (item[0]).
new_dados = dict(sorted(dados.items(), key=lambda item: item[1]))

k = 1
print(' == RANKING DOS JOGADORES == ')
for i, j in new_dados.items():
    print(f'{k}° lugar: Jogador {i} com {j}.')
    k += 1

new_dados = dict(sorted(dados.items(), key=lambda item: item[1], reverse=True))

k = 1
print(' == RANKING DOS JOGADORES REVERSE == ')
for i, j in new_dados.items():
    print(f'{k}° lugar: Jogador {i} com {j}.')
    k += 1