list_store = ('Camisa', 79.90, 'Short', 26.90, 'Sapato Nike', 499.90, 'Moletom', 79.90, 'Calça Jeans Lacosta', 299.90,
               'Sandalia Havaianas', 69.90, 'Chapeu Cut Hair', 39.90, 'Relogio Outlet', 599.90, 'Moletom Canguru', 199.90)

for c in range(0, len(list_store), 2):
    print(f'{list_store[c]:.<30}R${list_store[c+1]:.2f}')