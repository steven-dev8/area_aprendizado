import moeda

valor = float(input('Digite um valor: '))

#Exercício 109
print(moeda.aumentar(valor, 30, True))
print(moeda.diminuir(valor, 20, True))
print(moeda.dobro(valor))
print(moeda.metade(valor))

#Exercício 110
print(moeda.resumo(valor, 30, 20))