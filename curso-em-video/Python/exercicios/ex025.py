print('SUA CIDADE COMEÇA COM SANTOS?')

city = str(input('Qual o nome da sua cidade: ')).capitalize()

city1 = city[:6]

if city1 == 'Santos':
    print('Sim')
else:
    print('Não')
