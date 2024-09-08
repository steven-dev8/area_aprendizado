time = ('Flamengo', 'Palmeiras', 'Santos', 'Corinthians', 'São Paulo', 'Grêmio', 'Internacional', 'Cruzeiro', 
        'Atlético Mineiro', 'Vasco da Gama', 'Botafogo', 'Fluminense', 'Bahia', 'Sport Recife', 
        'Athletico Paranaense', 'Fortaleza', 'Ceará', 'Goiás', 'Chapecoense', 'Coritiba')

print(f'Os times: {time}')
print('-='*20)
print(f'Os 5 primeiros colocados são: {time[0:5]}')
print('-='*20)
print(f'Os últimos 4 colocados da tabela: {time[-4:]}')
print('-='*20)
print(f'Os times em ordem alfábetica: {sorted(time)}')
print('-='*20)
print(f'O time Chapecoense está em {time.index('Chapecoense')+1}º lugar')