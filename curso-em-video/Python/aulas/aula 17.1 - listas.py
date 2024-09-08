val = []
val.append(1)
val.append(4)
val.append(7)
val.append(12)

for contagem,valores in enumerate(val): #enumerate() é usado tanto para obter o índice e o valor da lista
    print(f'Na posição {contagem} está o item ({valores})')

#Adicionando listas em outras variáveis
a = [1, 4, 7, 8]
c = a #"c" vai se igualar ao "a"
b = a[:] #"b" vai receber todos os valores da lista "a"

b[1] = 9
c[2] = 9

print(f'Lista A {a}')
print(f'Lista B {b}')
print(f'Lista C {c}')