"""
LISTAS COMPOSTAS
"""
pessoas = [] #Cria variável que contém uma lista chamado pessoas

dados1 = ['Ana', '25'] #Lista com dados de alguém
pessoas.append(dados1[:]) #Adiciona essa lista de dados dentro de outra lista 

dados1 = ['Carlos','18'] 
pessoas.append(dados1[:]) 

dados1 = ['Sofia', '32'] 
pessoas.append(dados1[:]) 

print(pessoas) #Imprime todas as listas dentro da lista pessoas