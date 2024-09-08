DADOS = []
MEDIA_IDADE = 0
QUEST = ''

while QUEST != 'N':
    PESSOA = {
        'nome': input('Nome: '),
        'sexo': input('Sexo [M/F]: ').upper()[0],
        'idade': int(input('Idade: '))
    }

    MEDIA_IDADE = MEDIA_IDADE + (PESSOA['idade'])
    DADOS.append(PESSOA)

    QUEST = input('Deseja adicionar mais alguém? [S/N]: ').upper()[0]

MEDIA_IDADE /= len(DADOS)

print('-=' * 20)
print(f'Foram cadastradas {len(DADOS)} pessoas.')
print(f'A média de idade do grupo é {MEDIA_IDADE} anos')
print('-=' * 20)

print('As mulheres do grupo são ', end='')
for i in range(len(DADOS)):
    if DADOS[i]['sexo'] == 'F':
        print(f'Nome: {DADOS[i]['nome']}; Idade: {DADOS[i]['idade']}', end=' ')
print()

print('As pessoas com idade acima da média é ')
for i in range(len(DADOS)):
    if DADOS[i]['idade'] > MEDIA_IDADE:
        print(f'Nome: {DADOS[i]['nome']}; Sexo: {DADOS[i]['sexo']}; Idade = {DADOS[i]['idade']}')
