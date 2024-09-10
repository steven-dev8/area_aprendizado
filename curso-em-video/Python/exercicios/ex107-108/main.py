import moeda

valor = float(input('Digite o valor da moeda: '))

print(f'Aumentando 50% de {moeda.conversao(valor)} é {moeda.conversao(moeda.aumentar(valor, 50))}')
print(f'Diminuindo 15% de {moeda.conversao(valor)} é {moeda.conversao(moeda.diminuir(valor, 15))}')
print(f'O dobro de {moeda.conversao(valor)} é {moeda.conversao(moeda.dobro(valor))}')
print(f'A metade de {moeda.conversao(valor)} é {moeda.conversao(moeda.metade(valor))}')