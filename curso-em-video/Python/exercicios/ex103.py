def ficha(txt='', gol=''):
    if txt == '':
        txt = '<desconhecido>'
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0

    print(f'O jogador {txt} fez {gol} gol(s) no campeonato')

print('-' * 30)
PLAYER = input('Nome do jogador: ')
GOL = input('Número de gols: ')

ficha(PLAYER, GOL)