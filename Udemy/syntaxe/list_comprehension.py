"""
List comprehension é uma versão compacta de uma lista usando o iterador for
"""

# Cria uma lista com números de 0 a 9
lista = [i for i in range(10)] # o primeiro i é o que vai ser adicionado na lista
print(lista)

#Cria uma lista com cada elemento da string/lista
string = 'ola, mundo'
lista = [j for j in string]
print(lista)

"""
List comprehension com condicionais
"""

# condicionais de mapeamento (map)
sobremesas = ["bolo", "pudim", "sorvete", "fruta"]
resultado = [f'{sobremesa} é doce' if sobremesa in ["bolo", "pudim", "sorvete"] else f'{sobremesa} não é doce!' for sobremesa in sobremesas]
print(resultado) # OBS: O if sempre é acompanhados com else, ambos ficam antes do for (parecido com operação ternária)

# condicionais de filtragem (filter)
apenas_doce = [sobremesa for sobremesa in sobremesas if sobremesa in ['bolo', 'pudim', 'sorvete']]
print(apenas_doce) # OBS: O if fica depois do for e não vem acompanhado de else

"""
Mapeamento: cria uma nova lista modificando os elementos, mas sem remover ou adicionar elementos a mais na lista
Filter: uma condicional, se caso ela seja verdadeira, adiciona o item na lista
"""

# Ex2 de mapeamento
lista = [i*2 
         if i > 5 else i
         for i in range(10)
         ]
print(lista)