"""Exercício 2: Calculadora Simples
Crie uma classe Calculadora que tenha os seguintes métodos:

adicionar(a, b): retorna a soma de a e b.
subtrair(a, b): retorna a diferença entre a e b.
multiplicar(a, b): retorna o produto de a e b.
dividir(a, b): retorna o quociente de a por b.
Desafio: Crie um objeto Calculadora e use-o para realizar as quatro operações (adição, subtração, multiplicação e divisão) com diferentes valores."""

class Calculadora():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def somar(self):
        return self.a + self.b 

    def subtrair(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        if self.b == 0:
            return 'Erro! Divisão por 0 inválida'
        else:
            return self.a / self.b

a = float(input(''))
b = float(input(''))

objeto1 = Calculadora(a, b)

print(f'A soma de {objeto1.a} + {objeto1.b} = {objeto1.somar()}')
print(f'A subtração de {objeto1.a} - {objeto1.b} = {objeto1.subtrair()}')
print(f'A multiplicação {objeto1.a} * {objeto1.b} = {objeto1.multiplicar()}')
print(f'A divisão de {objeto1.a} / {objeto1.b} = {objeto1.dividir()}')