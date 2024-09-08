import math

print('Calculadora de Ângulo de seno, cosseno e tangente')
val = float(input('Digite o Ângulo: '))
sen = math.sin(math.radians(val))
cos = math.cos(math.radians(val))
tan = math.tan(math.radians(val))
print(f'Ângulo de {val} \n'
      f'Seno: {sen:.3f} \n'
      f'Cosseno {cos:.3f} \n'
      f'Tangente {tan:.3f} \n')
