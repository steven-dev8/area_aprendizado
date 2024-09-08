from time import sleep

def contador(a, b, c):
    print(f'Contagem de {a} até {b} de {c} em {c}')
    
    if c == 0:
        c = 1
    elif c < 0:
        c *= -1

    if a < b:
        for i in range(a, b + 1, c):
            print(i, end=' ', flush=True)
            sleep(0.1)
        print('FIM')
    elif a > b:
        for i in range(a + 1, b, -c):
            print(i - 1, end=' ', flush=True)
            sleep(0.1)
            
        print('FIM')
    print('-=' * 20)


contador(0, 10, 1)
contador(10, 0, 1)

print('Agora é sua vez de personalizar a contagem!')

INICIO = int(input('Início: '))
FIM = int(input('Fim: '))
PASSO = int(input('Passo: '))

contador(INICIO, FIM, PASSO)