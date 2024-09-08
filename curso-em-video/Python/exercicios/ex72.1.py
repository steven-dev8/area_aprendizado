count = 0
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    select = ''
    numero = int(input('Digite um número entre 0 a 20: '))

    if 0 <= numero and 20 >= numero:
        print(f'O número digitado foi o {extenso[numero]}')
        while select not in ('S','N'):
            select = input('Deseja continuar? [S/N] ').upper().strip()
            if 'N' in select:
                count += 1
                break
            
    if count == 1:
        break