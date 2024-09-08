name = input('Bem vindo ao Carteira Python, primeiramente queremos saber o seu nome: ')
a = float(input('Informe quantos Reais está disponivel nos seus bancos: '))
b = a / 3.27
print(f'Então {name}, a cotação do Dolar para o Real atualmente é de R$3,27 \n Com R${a} você consegue comprar ${b:.2f}')
