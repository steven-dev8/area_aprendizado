# sets(conjuntos) em python, são os mesmos conjuntos ensinado na matemática 
# sets em python são mutáveis e iteráveis, mas recebe apenas valores imutáveis

meu_set = set() # Atribui um conjunto para a variável meu_set
meu_set = {'Steven', 1, 2, 3}
print(meu_set)

# métodos úteis add, update, clear, discard
# sets são eficientes para remover itens duplicados de itéraveis

numeros = [1, 2, 3, 4, 4, 4, 4, 4, 4, 5, 6, 6, 6]
set_numeros = set(numeros)
set_numeros.add('add') # set.add(valor) adiciona o valor ao set por inteiro
print(set_numeros)

set_numeros.update('OI') # set.update(valor) adiciona o valor ao set de forma iterável
print(set_numeros)

set_numeros.clear() # set.clear() limpa todos os itens do set
print(set_numeros)

set_numeros = {'Luiz', 1 ,2 ,3 ,4}
set_numeros.discard('Luiz') # set.discard(valor) remove o item do set
print(set_numeros)

# Operadores úteits:
# união | união (union) une dois sets em um só
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set_union = set1 | set2
print(f'{set1} | {set2} = {set_union}')

# intersecção & (intersection) - Itens que são comum entre os sets
set1 = {'Ana', 'João', 'Maria'}
set2 = {'Maria', 'Carlos', 'Sofia'}
set_inter = set1 & set2
print(f'{set1} & {set2} = {set_inter}')

# diferença - Itens presentes apenas no set da esquerda que não são comuns entre os sets
set_dif = set1 - set2
print(f'{set1} - {set2} = {set_dif}')

# diferença simétrica - Itens que não são comuns entre os sets
dif_simetrica = set1 ^ set2
print(f'{set1} ^ {set2} = {dif_simetrica}')
