"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja 
enviado para o parâmetro, o valor padrão será
usado.
"""

def soma(x: int, y: int, z=None): # z vai receber None se não for enviado um argumento para z
    if z is not None: # 'is not' tradução: não é
        print(x + y + z)
    else:
        print(x + y)

soma(1, 2)
soma(1, 5, 5)