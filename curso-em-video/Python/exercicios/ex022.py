name = str(input('Digite um nome completo: '))
print(f'MAIÚSCULO: {name.upper()}')
print(f'minúsculo: {name.lower()}')

log = name.replace(' ', '')
name = name.split()

print(f'O nome possui {len(log)} caracteres')
print(f'O primeiro nome possui {len(name[0])} caracteres')
