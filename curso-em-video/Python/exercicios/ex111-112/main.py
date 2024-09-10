from utilidadesCeV import moeda, dados

valor = dados.leiaDinheiro('Digite o preço: R$')
print(moeda.resumo(valor, 10, 30))
