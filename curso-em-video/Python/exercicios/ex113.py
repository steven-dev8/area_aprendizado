def leiaInt():
    while True:
        try:
            inteiro = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número inteiro válido!\033[0m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário não informou o valor.\033[0m')
            return 0
        else:
            return inteiro

def leiaFloat():
    while True:
        try:
            real = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número real válido!\033[0m')
        except KeyboardInterrupt:
            print('\033[31mO usuário não informou o valor.\033[0m')
            return 0
        else:
            return real

print(leiaFloat(), leiaInt())