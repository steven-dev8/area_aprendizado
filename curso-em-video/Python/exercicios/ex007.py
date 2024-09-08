prof = input('Digite o seu nome por favor: ')
print(f'Seja bem vindo {prof} ao sistema de calculadora de notas')
mat = input('Qual matéria você deseja calcular a nota? ')
aluno = input('Qual o nome do aluno? ')
n1 = int(input(f'Digite a primeira nota de {mat}: '))
n2 = int(input(f'Digite a segunda nota de {mat}: '))
final = (n1+n2)/2
print(f'{aluno} , a média final de {mat} é {final}.')
