from time import sleep

def maior(* num):
    sleep(0.3)
    print('-=' * 20)
    print('Analisando os valores passados...')
    print(*num, sep=' ', end=' ')
    print(f'Foram informado {len(num)} valores ao todo. ')
    print(f'O maior valor informado foi {max(num)}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)