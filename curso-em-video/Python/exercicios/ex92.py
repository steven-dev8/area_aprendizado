from datetime import datetime
ANO_ADD_APOSENTADORIA = 35

DADOS = {
    'nome': input('Nome: '),
    'idade': datetime.now().year - int(input('Ano de nascimento: ')),
    'ctps': int(input('Carteira de Trabalho (0 - NÃO POSSUI): '))
}

if DADOS['ctps'] != 0:
    DADOS['contratação'] = int(input('Ano de contratação: '))
    DADOS['salario'] = float(input('Salário: '))
    DADOS['aposentadoria'] = (DADOS['contratação'] + DADOS['idade'] + ANO_ADD_APOSENTADORIA) - datetime.now().year

for i, j in DADOS.items():
    print(f'{i} tem valor de {j}')