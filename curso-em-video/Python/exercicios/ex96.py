def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área é de {area}m²')

print('-=' * 15)
print('CONTROLE DE TERRENO'.rjust(24, ' '))
print('-=' * 15)

L = float(input('LARGURA (m): '))
C = float(input('COMPRIMENTO (m): '))

area(L, C)