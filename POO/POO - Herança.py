class roupa():
    def __init__(self, marca, tecido):
        self.marca = marca.upper()
        self.tecido = tecido.lower()
        self.aspecto_la = ['Isolamento Térmico', 'Absorção de Umidade:', 'Elasticidade e Durabilidade']
        self.aspecto_poliester = ['Durabilidade','Resistência a Rugas','Secagem Rápida']

    def info_geral(self):
        print(f'MARCA: {self.marca}')
        print(f'TECIDO: {self.tecido}')

class informacao(roupa):
    def caracteristicas(self):
        if self.tecido in ['lã', 'la']:
            print('Caracteristicas da lã')
            for i in self.aspecto_la:
                print(f' ·{i}')
        elif self.tecido in ['poliester', 'polister']:
            print('Caracteristicas do polister')
            for i in self.aspecto_poliester:
                print(f' ·{i}')
        else:
            print('TECIDO NÃO LISTADO')

    def tipo_marca(self):
        print(f'A marca do produto é {self.marca}')
    
    def tipo_tecido(self):
        if self.tecido in ['polister', 'poliester']:
            print('O poliéster é uma fibra sintética produzida a partir de polímeros derivados do petróleo.')
        if self.tecido in ['la', 'lã']:
            print('O tecido de lã é um material natural obtido principalmente a partir do pelo de animais, como ovelhas, cabras (caxemira), lhamas, alpacas e coelhos (angorá).')


marca = input('Qual a marca do produto? ')
print('TECIDOS: lã ou poliester')
tecido = input('Qual o tipo do tecido? ')

tecido = informacao(marca, tecido)

tecido.tipo_marca()
tecido.tipo_tecido()
tecido.caracteristicas()