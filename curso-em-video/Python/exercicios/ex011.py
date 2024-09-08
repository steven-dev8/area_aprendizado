print('Calculadora de tinta por m² de uma área')
tn = input('Qual cor ou tipo de tinta que você deseja pintar a área? ')
n1 = float(input('Digite a largura da área em metros: '))
n2 = float(input('Digite a altura da área em metros: '))
n3 = (n1 * n2) / 2
print(f'Você precisara de {n3:.1f} litros de tinta {tn} para pintar {n1 * n2}m²')
