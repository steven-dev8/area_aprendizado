print('CALCULADORA DE NOTAS')
nota_a = float(input('INFORME A PRIMEIRA NOTA: '))
nota_b = float(input('INFORME A SEGUNDA NOTA: '))
media = (nota_a + nota_b) / 2
if media < 5:
    print('\033[1;31mO ALUNO ESTÁ REPROVADO')
elif media < 6.9:
    print('\033[1;33mO ALUNO ESTÁ DE RECUPERAÇÃO')
else:
    print('\033[1;32mO ALUNO ESTÁ APROVADO')
