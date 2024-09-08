print('DESCUBRA QUAL ATLETA VOCÊ É')
idade = int(input('INFORME A IDADE DO ATLETA: '))
if idade < 10:
    print('O ATLETA É MIRIM')
elif idade < 15:
    print('O ATLETA É INFANTIL')
elif idade < 20:
    print('O ATLETA É JUNIOR')
elif idade < 21:
    print('O ATLETA É SÊNIOR')
else:
    print('O ATLETA É MASTER')
