from random import shuffle

print('Sorteio de alunos')
a = str(input('Digite o nome do aluno1: '))
b = str(input('Digite o nome do aluno2: '))
c = str(input('Digite o nome do aluno3: '))
d = str(input('Digite o nome do aluno4: '))
list = [a, b, c, d]
shuffle(list)
print(f'O aluno escolhido foi o: {list}')