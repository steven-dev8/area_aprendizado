DADOS = []

while True:
    print('-' * 40)
    PLAYER = {
        'nome': input('Nome do jogador: ').capitalize(),
        'gols': []
    }

    TOTAL = 0
    PARTIDA = int(input('Quantidade de partidas: '))

    for i in range(PARTIDA):
        GOLS = int(input(f'Total de gols da {i+1} partida: '))

        PLAYER['gols'].append(GOLS)
        TOTAL += GOLS

    PLAYER['total'] = TOTAL
    DADOS.append(PLAYER)

    QUEST = input('Deseja continuar? [S/N] ').upper()[0]
    if QUEST == 'N':
        break

print('-=' * 20)
print('COD  NOME           GOLS          TOTAL')
for i in range(len(DADOS)):
    print(f'{i: <4} {DADOS[i]['nome']: <14} {str(DADOS[i]['gols']): <13} {DADOS[i]['total']}')

while True:
    SELECT_PLAYER = int(input('Mostrar dados de qual jogador? [999 - PARAR]: '))
    if SELECT_PLAYER < len(DADOS):
        print(f'--LEVANTAMENTO DO JOGO {DADOS[SELECT_PLAYER]['nome']}--')
        for i, j in enumerate(DADOS[SELECT_PLAYER]['gols']):
            print(f'No jogo {i+1} fez {j} gols.')
    else:
        if SELECT_PLAYER == 999:
            break
        else:
            print('Digite um jogador válido.')