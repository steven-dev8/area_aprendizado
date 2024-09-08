"""
Exercício 4: Sistema de Biblioteca
Crie uma classe Livro que represente um livro em uma biblioteca. A classe deve ter os seguintes atributos e métodos:

Atributos:
titulo: O título do livro.
autor: O autor do livro.
ano: O ano de publicação do livro.
disponivel: Um booleano que indica se o livro está disponível para empréstimo.

Métodos:
emprestar(): Marca o livro como emprestado e retorna uma mensagem indicando se o empréstimo foi bem-sucedido ou não (se o livro já estiver emprestado).
devolver(): Marca o livro como disponível e retorna uma mensagem indicando que o livro foi devolvido.
exibir_informacoes(): Retorna uma string com as informações do livro, incluindo se está disponível ou não.
"""

class Livro():
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return f'Emprestimo bem-sucedido do {self.titulo} de {self.autor}'
        else:
            return f'{self.titulo} de {self.autor} está indisponivel, pois já está emprestado. '
        
    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            return f'{self.titulo} de {self.autor} foi devolvido.'
        else:
            return f'{self.titulo} de {self.autor} está disponivel.'
    
    def exibir_informacoes(self):
        return f'{self.titulo} de {self.autor} do ano {self.ano} está {'disponivel' if self.disponivel else 'indisponivel'}'
    
livro1 = Livro('1984', 'George Orwell', 1949)
livro2 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)

print(livro1.exibir_informacoes())
print(livro1.emprestar())
print(livro1.emprestar())
print(livro1.devolver())
print(livro1.devolver())

print(livro2.exibir_informacoes())
print(livro2.emprestar())
print(livro2.exibir_informacoes())