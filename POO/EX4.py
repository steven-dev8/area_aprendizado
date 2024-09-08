"""Descrição: Crie uma classe base Forma com um método area. Em seguida, crie duas classes derivadas, Retangulo e Circulo, que implementam o método area para calcular a área do retângulo e do círculo, respectivamente."""

class Forma():
    def area(self):
        raise NotImplementedError

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        print(f'A área do retângulo é {(self.largura * self.altura):.2f}m^2')

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.141592

    def area(self):
        print(f'A área do circulo é {self.pi * (self.raio ** 2):.2f}m^2')

def calcular_area(parametro):
    parametro.area()

circulo = Circulo(2)
ratangulo = Retangulo(2,2)

calcular_area(circulo)
calcular_area(ratangulo)