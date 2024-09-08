geral = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2
    geral.append([[nome,[nota1, nota2],media]])

    quest = input('Deseja continuar? [S/N] ').upper()[0]
    if quest == 'N':
        break
print('-=' * 30)
print('No. NOME               MEDIA')
print('-' * 30)

for pos, nome in enumerate(geral):
    print(f'{pos}   {nome[0][0]: <18} {nome[0][2]}')

while True:
    num = int(input('Mostrar a notas de qual aluno? [999 - PARAR]: '))
    if num == 999:
        break

    print(f'Notas de {geral[num][0][0]} são {geral[num][0][1]}')
