dados = []
nome_maior_peso = []
nome_menor_peso = []

while True:
    people = []
    people.append(input('Nome: '))
    people.append(float(input('Peso: ')))
    dados.append(people[:])
    
    if len(dados) == 1:
        maior_peso = menor_peso = people[1]
    else:
        if people[1] > maior_peso:
            maior_peso = people[1]
        if people[1] < menor_peso:
            menor_peso = people[1]

    check = input('Deseja adicionar mais alguem? [S/N]').upper()[0]
    if check == 'N':
        break

for pos in dados:
    if pos[1] == maior_peso:
        nome_maior_peso.append(pos[0])
    if pos[1] == menor_peso:
        nome_menor_peso.append(pos[0])

print(f'FORAM REGISTRADAS {len(dados)} PESSOAS')
print(f'O maior peso é {maior_peso}Kg. Pesos de {nome_maior_peso}')
print(f'O menor peso é {menor_peso}Kg. Pesos de {nome_menor_peso}')
