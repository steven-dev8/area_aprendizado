"""
Crie uma classe chamada Carro que tenha os seguintes atributos:

marca: a marca do carro.
modelo: o modelo do carro.
ano: o ano de fabricação.
Adicione também os seguintes métodos:

acelerar(): exiba uma mensagem dizendo que o carro está acelerando.
frear(): exiba uma mensagem dizendo que o carro está freando.
Desafio: Crie dois objetos Carro com atributos diferentes e use os métodos acelerar e frear para cada um deles.
"""

class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def acelerar(self):
        print(f'O carro {self.modelo} da marca {self.marca} está acelerando')

    def frear(self):
        print(f'O carro {self.modelo} da marca {self.marca} está freando')
    
objeto1 = Carro('Wolkswagen','Colora','2000')
objeto2 = Carro('Chevrolet', 'Gol', '2010')

objeto1.acelerar()
objeto2.frear()