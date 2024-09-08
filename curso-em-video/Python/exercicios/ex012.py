print('Lojinha do Araújo')
name = input('Qual o nome do produto? ')
a = float(input('Digite o valor original do produto para calcular o preço final: '))
b = a * 90 / 100
c = a * 8 / 100 + a
print(f'"{name}" \n Pagando a vísta com 10% de desconto saíra por R${b:.2f} \n Pagando parcelado com 8% de aumento '
      f'saíra por R${c:.2f}')
