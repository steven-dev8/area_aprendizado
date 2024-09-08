express = str(input('Digite a expressão: '))
lista = []

for simb in express:
    if simb == '(':
        lista.append(simb)
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(simb)
            break
        
if len(lista) == 0:
    print('A expressão está correta')
else:
    print('A expressão está errada')