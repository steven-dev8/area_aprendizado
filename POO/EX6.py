"""Descrição: Crie uma classe base Conta com um método saldo e depositar. Em seguida, crie duas classes derivadas, ContaCorrente e ContaPoupanca, que implementam o método saldo para retornar o saldo com base nas regras específicas de cada tipo de conta."""

class Conta():
    def __init__(self, saldo):
        self.saldo_atual = saldo

    def depositar(self, valor):
        self.saldo_atual += valor
    
    def saldo(self):
        raise NotImplementedError('Este metodo...')

class ContaCorrente(Conta):
    def azul(self):
        return self.saldo_atual - 20

class ContaPoupanca(Conta):
    def saldo(self):
        return (self.saldo_atual * 1.005)

conta1 = ContaCorrente(1000)
conta2 = ContaPoupanca(1000)

conta1.depositar(400)
conta2.depositar(1000)

print(conta1.saldo())
print(conta2.saldo())