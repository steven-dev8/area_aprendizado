from random import randint 
from time import sleep

dados = [] 

qnt_jogos = int(input('Quantos jogos você quer que sorteie: '))

while len(dados) < qnt_jogos: 
    jogo = []

    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)

    dados.append(jogo) 

print(f'-=-=-=-=Sorteando {qnt_jogos} jogos-=-=--==')
for num_jogo, jogos in enumerate(dados):
    print(f'Jogo {num_jogo+1}: {sorted(jogos)}')
    sleep(1)
print('-=-=-=-=-=-=BOA SORTE-=--=-==-=-=')