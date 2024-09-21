def menu():
    print('-' * 50)
    print(f'{'MENU PRINCIPAL': >31}')
    print('-' * 50)
    print('\033[33m1 \033[34m- Ver pessoas cadastradas\033[0m')
    print('\033[33m2 \033[34m- Cadastrar novas pessoas\033[0m')
    print('\033[33m3 \033[34m- Sair do Sistema\033[0m')
    print('-' * 50)
    while True:
        try:
            escolha = int(input('\033[33mEscolha uma opção:\033[0m '))
        except:
            print('\033[31mERRO: Digite um número válido!\033[0m')
        else:
            if 1 <= escolha <= 3:
                return escolha
            else:
                print('\033[31mERRO: Digite um número válido!\033[0m')

def view():
    print('-' * 50)
    print(f'{'LISTA DE PESSOAS CADASTRADAS': >39}')
    print('-' * 50)
    try:
        file = open(r'C:\VSCODE\cadastros.txt', 'r')
    except:
        file = open(r'C:\VSCODE\cadastros.txt', 'a')
        file = open(r'C:\VSCODE\cadastros.txt', 'r')
        
    leitura = file.readlines()
    file.close()

    new_leitura = []
    for i in leitura:
        new_leitura.append(i.replace('\n', ''))
    
    for j, k in enumerate(new_leitura):
        if (j + 1) % 2 == 0:
            print(f'{k} anos')
        else:
            print(f'{k: <40}', end='')

def cadastrar():
    nome = input('Digite o nome: ')

    while True:
        try:
            idade = int(input('Digite a idade: '))
        except:
            print('ERRO: Digite uma idade válida!')
        else:
            idade = idade
            break

    arquivo = open(r'C:\VSCODE\cadastros.txt', 'a')
    arquivo.write(f'{nome}\n')
    arquivo.write(f'{str(idade)}\n')
    arquivo.close()
    print(f'Novo cadastro de {nome} adicionado')
