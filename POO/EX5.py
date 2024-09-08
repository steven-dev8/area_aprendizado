"""Descrição: Crie uma classe base Veiculo com um método tipo_combustivel. Em seguida, crie duas classes derivadas, Carro e Motocicleta, que implementam o método tipo_combustivel para retornar o tipo de combustível usado pelo veículo."""

class Veiculo():
    def tipo_combustivel(self):
        raise NotImplementedError

class Carro(Veiculo):
    def tipo_combustivel(self):
        self.veiculo = 'Carro'
        self.combustivel = 'Etanol'

class Motocicleta(Veiculo):
    def tipo_combustivel(self):
        self.veiculo = 'Motocicleta'
        self.combustivel = 'Gasolina'

def combustivel(veiculo):
    veiculo.tipo_combustivel()
    print(f'O combustivel do/a {veiculo.veiculo} é {veiculo.combustivel}')

veiculo1 = Carro()
veiculo2 = Motocicleta()

combustivel(veiculo1)
combustivel(veiculo2)