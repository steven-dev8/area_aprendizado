extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
           'catorze', 'quinze', 'dezeseis','dezesete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número de 0 a 20: '))

while numero < 0 or numero > 20:
    numero = int(input('Tente novamente. Digite um número de 0 a 20: '))
print(f'O número escolhido é {extenso[numero]}')
