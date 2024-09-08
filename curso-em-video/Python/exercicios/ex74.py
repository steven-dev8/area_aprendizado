from random import sample

a = tuple(sample(range(10), 5))

print(f'Os números escolhidos: {a}')
print(f'O maior valor é {max(a)} e o menor {min(a)}')