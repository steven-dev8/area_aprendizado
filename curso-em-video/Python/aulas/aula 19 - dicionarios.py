dados = {'nome':'Carlos','idade':'18'} #Nomeia o índice. Ex: 'Carlos' terá como índice 'nome'
print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'M' #Cria um novo índice com o valor 'M'
print(dados['sexo'])

del dados['idade'] #Deleta o índice junto com o seu válor
print(dados) #Dados 

#Cria um dicionario
filme = {
    'titulo':'Arcane',
    'ano':'2022',
    'diretor':'Riot Games'
}
print(filme.values()) #Imprime os valores do dicionario
print(filme.keys()) #Imprime as chaves/índice 
print(filme.items()) #Imprime os dois

for k, v in filme.items(): #Imprime a chave e os valores do dicionario
    print(f'O {k} é {v}') 

print('-=' * 30)

LISTA = [{
    'username':'angelo123',
    'password':'123'
}, {
    'username':'clara22',
    'password':'223'
}, {
    'username':'loran3',
    'password':'2234'
}]

for users in LISTA:
    print(f'Usuário: {users['username']} Senha: {users['password']}')

"""
Para copiar dicionarios dentro de lista, utilizasse a função dict.copy
Ex: lista.append(dict.copy)
"""

#Função sun() soma qualquer iterável, como listas com numeros, tuplas e números
