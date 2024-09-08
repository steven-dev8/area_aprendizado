# Def é a minha palavra-chave que define minha função.
def soma(a, b): # 'a' e 'b' são meus dois parâmetros
    som = a + b
    print(som)


soma(1, 2) #Retorna a soma de a + b

# Essa função desempacota (recebe multiplos valores) valores e depois imprime eles
def contador(* num): #'*' índica que não tem um número definido de parâmetros a ser definido
    for i in num:
        print(i, end=' ')
    print('end')


contador(1, 5, 67, 2, 4, 5)
contador(3, 2, 6, 7, 2)
contador('oi', 3)

# Essa função pega uma lista e retorna o valor de uma lista com os valores dobrados.
def dobra(a):
    for i in range(len(a)):
        a[i] *= 2 #Você consegue fazer uma operação aritmetica de valor de uma lista apenas indicando o seu índice.
    print(a)


dobra([2, 4, 6])