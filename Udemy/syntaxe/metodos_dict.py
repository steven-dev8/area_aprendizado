def espaco():
    print()


# pop(key) : remove uma chave do dicionario
d = {'a': 1, 'b': 2, 'c': 3}
valor = d.pop('b')
print(valor)  # Saída: 2
print(d)      # Saída: {'a': 1, 'c': 3}

espaco()

# dict.get(key, default=None) : retorna o valor associado a chave, e caso ela não exista, 
# retorna o valor especificado em default, sem alterar o dicionario
d = {'a': 1, 'b': 2, 'c': 3}
valor = d.get('d', 'Não existe')
print(valor)
print(d)

espaco()

# dict.setdefault(key, default=None) : retorna o valor associado a chave, e caso ela não exista, adiciona o valor 
# especificado em default no dicionario
d = {'a': 1, 'b': 2, 'c': 3}
valor = d.setdefault('d', '4')
print(valor)
print(d)

espaco()

# dict.copy() ; faz uma cópia rasa, objetos mutáveis dentro do dicionário original continuam compartilhados entre a cópia e o original.
# Alterações em objetos mutáveis afetam ambos.
d = {'a': 1, 'b': 2, 'c': 3}
d_copy = d.copy()
print(f'original: {d}')
print(f'cópia: {d_copy}')

espaco()

# dict.update(outro_dicionario) : atualiza o dicionario, sobrescrevendo os items que já existem e adicionando items que ainda não existe
# no dicionario principal
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'c': 4, 'd': 5}
d1.update(d2)
print(f'dicionário atualizado: {d1}')

espaco()

# dict.popitem() : remove o último item do dicionario
d1 = {'a': 1, 'b': 2, 'c': 3}
d1.popitem()
print(d1)
