"""
Listas ao contrário das Tuplas, são modificaveis, então você pode adicionar e remover itens
quando quiser.
"""
#Listas
print('Listas')

listas = [1, 2, 3] #As listas utiliza colchetes entre seus itens
print(f'Lista: {listas}')

listas.append(4) #Adiciona um novo item a lista. Ex: a lista tinha 3 itens e foi adiciona o item 4 a lista
print(f'Lista: {listas}')

listas.insert(0,0) #Adiciona um novo item a lista a partir da posição que eu especificar no primeiro valor. Ex: Na posição 0 da lista foi adicionado o número 0
print(f'Lista: {listas}')

#Eliminar elementos da lista
del listas[0] #Remove o elemento que está na posição 0 da minha lista
print(f'Lista: {listas}')

listas.pop(3) #Remove o terceiro elemento da minha lista. OBS:Utilizada sem o especificar o índice, removerá o ultimo elemento da lista
#Ex. Remove o terceiro valor da lista, no caso o 4 que está na posição 3
print(f'Lista: {listas}')

listas.remove(3) #Remove o item especificado dentro do parênteses, no caso irá remover o item 3 da lista
print(f'Lista: {listas}')

if 2 in listas: #Se 2 estiver contido em "listas"
    listas.remove(2) #Apague o item "2"
print(f'Lista: {listas}')

if len(listas) == 1: #Se a leitura de lista tiver apenas um item
    #Adiciona 4 itens a lista
    listas.append(2)
    listas.append(3)
    listas.append(4)
    listas.append(5)
print(f'Lista: {listas}')
print('-=' * 30)
#Gerar/organizar listas
print('Gerar/organizar listas')

valores = list(range(4,10)) #Gera itens com números de 4 a 9 em forma de lista dentro da váriavel "valores"
print(f'Lista: {valores}')

print('*Lista desordenada')

valores = [6, 3, 1, 8, 2, 9]
print(f'Lista: {valores}')

print('*Lista ordenada')
valores.sort() #Ordena a lista de acordo em (1, 2, 3) ou (A, B, C)
print(valores)

print('*Lista ordenada inversa')
valores.sort(reverse=True) #Ordena a lista de forma decrescente

len(valores) #Ler quantos itens tem na lista
print(f'A variável "valores" possui {valores} itens')