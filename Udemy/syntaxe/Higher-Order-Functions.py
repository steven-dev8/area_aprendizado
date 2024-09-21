"""
Higher Order Functions - Funções de primeira ordem
"""

# Funções como Argumentos
def dobro(x: int):
    return x * 2


lista_numeros = [1, 2, 3, 4]
numeros_dobrados = list(map(dobro, lista_numeros)) # map(função, iterável) cria uma iteração de cada item do iterável com a função e retorna um iterável
print(numeros_dobrados)

# Funções como retorno
def string(arg: str):
    def multi_string(x: int):
        return arg * x
    return multi_string

# minha_string recebe/transforma uma função com argumento x já declarado
minha_string = string('Olá mundo ')
# minha_string, como função, recebe argumento y que retorna a multiplicação do argumento x com y.
print(minha_string(5))
