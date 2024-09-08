my_list = []
cont_1 = cont_2 = 0

expres = input('Digite a expressão: ')

for i in range(0, len(expres)):
    my_list.append(expres[i])

read = len(expres) // 2

for aspa1 in range(read):
    if my_list[aspa1] == '(':
        cont_1 += 1
    if my_list[aspa1] == ')':
        cont_2 += 1

for aspa2 in range(read, len(my_list)):
    if my_list[aspa2] == ')':
        cont_2 += 1
    if my_list[aspa1] == '(':
        cont_1 += 1

if cont_1 == cont_2:
    print('A expressão está correta!')
else:
    print('A sua expressão está errada!')