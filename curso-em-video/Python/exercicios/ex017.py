'''import math

print('Calculadora da Hipotenusa')
b = float(input('qual o comprimento do cateto oposto: '))
c = float(input('qual o comprimento do cateto adjacente: '))
print(f'O valor do comprimento da Hipotenusa é '
      f'{math.sqrt(math.pow(b, 2) + math.pow(c,2)):.2f}')'''

import math

print('Calcule a Hipotenusa')
a = float(input('Digite o cateto oposto: '))
b = float(input('Digite o cateto adjacente: '))
c = math.hypot(a, b)
print(f'O valor da Hipotenusa é {c:.2f}')
