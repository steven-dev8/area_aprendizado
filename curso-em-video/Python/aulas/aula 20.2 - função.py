#Função para imprimir a documentação de outra função
help(len)

print()
#Docstring
def soma(a, b):
    """Faz a soma entre a e b, e imprime na tela o resultado.

    Args:
        a (int): um valor inteiro 
        b (int): outro valor inteiro
    Função criada por Steven
    """
    print(a + b)

help(soma)

print()
#Parâmetros opcionais 
def somatorio(a=0, b=0, c=0):
    s = a + b + c
    print(s)

somatorio(2, 2) #Vai imprimir a soma de a + b, sem precisar informar o valor de c.

print()
#Escopo de variáveis 
def esp(a):
    a = 5 #Escopo local
    print(f'O "a" dentro vale {a}')


a = 2 #Escopo global
esp(a)
print(f'O "a" fora vale {a}')

print()
#Escopo de variáveis GLOBAL
def glob(b):
    global a #O valor "a" da viriável local, vai para o valor a da variável global
    a = 5 #Escopo local
    b = 7
    print(f'O "a" dentro vale {a}')
    print(f'O "b" dentro vale {b}')


a = 2 #Escopo global
glob(a) #O "a" agora vai valer 5, pois o valor será substituido pelo valor da variável local
print(f'O "a" fora vale {a}')

#Retorno
def funcao(a=0, b=0, c=0):
    s = a + b + c
    return s #Retorna a variável "s" para outra variável 

r1 = funcao(1,2,4) 
r2 = funcao(1,6,2)
r3 = funcao(8,3,7)

print(r1, r2, r3)