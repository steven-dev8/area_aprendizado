def leiaInt():

    while True:
        numero = input('\033[0mDigite um número: ')

        if numero.isnumeric():
            return numero
        else:
            print('\033[31mERRO! Digite um número inteiro')

number = leiaInt()
print(f'Você acabou de digitar o número {number}')