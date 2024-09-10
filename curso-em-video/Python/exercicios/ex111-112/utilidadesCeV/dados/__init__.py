def leiaDinheiro(string):
    while True:
        number = input(string)

        if ',' in number:
            number_save = number.replace(',', '')
            valid = number_save.isnumeric()
            number = number.replace(',', '.')
        elif '.' in number:
            number_save = number.replace('.', '')
            valid = number_save.isnumeric()
        else:
            valid = number.isnumeric()

        if valid:
            number = float(number)
            return number
        else:
            print(f'Erro: {number} é um preço invalido!')
            