PLAYER = {
    'nome': input('Nome do jogador: ').capitalize(),
    'gols': []
}

PARTIDA = int(input('Quantidade de partidas: '))

for i in range(PARTIDA):
    GOLS = int(input(f'Total de gols da {i+1} partida: '))
    PLAYER['gols'].append(GOLS)

PLAYER['total'] = sum(PLAYER['gols'])

for i, j in PLAYER.items():
    print(f'O PLAYER {i} tem valor {j}')

print('=' * 20)
print(f'O jogador {PLAYER['nome']} jogou {PARTIDA} partidas.')

for i, j in enumerate(PLAYER['gols']):
    print(f'   => Na partida {i+1}, fez {j} gols.')

print(f'Foi um total de {PLAYER['total']} gols.')