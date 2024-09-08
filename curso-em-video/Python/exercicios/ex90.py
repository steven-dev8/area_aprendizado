aluno = {}

aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Media: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print(f'Nome: {aluno['nome']}')
print(f'Média: {aluno['media']}')
print(f'Situação: [{aluno['situacao']}]') 