print('DESCUBRA O TRIÂNGULO')

a = float(input('INFORME O VALOR DO PRIMEIRO LADO: '))
b = float(input('INFORME O VALOR DO SEGUNDO LADO: '))
c = float(input('INFORME O VALOR DO TERCEIRO LADO: '))

if a > 0 or b > 0 or c > 0 and a < (c+b) and b < (a+c) or c < (b+c):
    if a == b == c:
        print('O TRIÂNGULO É EQUILÁTERO')
    elif a != c == b or b != c == a or c != b == c:
        print('O TRIÂNGULO É ISÓSCELE')
    else:
        print('O TRIÂNGULO É ESCALENO')
else:
    print('NÃO É UM TRIÂNGULO')
