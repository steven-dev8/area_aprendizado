class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def detalhes_pessoa(self):
          print(f'NOME: {self.nome}')
          print(f'IDADE: {self.idade}')

pessoa1 = Pessoa('Cecilia', 18)

pessoa1.detalhes_pessoa()