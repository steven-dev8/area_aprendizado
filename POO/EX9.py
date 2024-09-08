"""
Crie uma classe ContaBancaria com os seguintes atributos:

titular: nome do titular da conta.
saldo: saldo atual da conta (começa em zero).
Adicione os seguintes métodos:

depositar(valor): adiciona o valor ao saldo da conta.
sacar(valor): subtrai o valor do saldo da conta, se houver saldo suficiente. Se o saldo for insuficiente, exiba uma mensagem de erro.
exibir_saldo(): exiba o saldo atual da conta.
Desafio: Crie um objeto ContaBancaria para um titular de sua escolha, faça um depósito, tente sacar um valor maior que o saldo, e depois exiba o saldo atual.
"""

class ContaBancaria():
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, valor):
        if valor < 0:
            return 'O valor do deposito deve ser positivo.'
        self.saldo += valor
        return f'Deposito realizado, saldo atual R${self.saldo:.2f}'
    
    def sacar(self, valor):
        if valor < 0:
            return 'O valor do saque deve ser positivo'
        if self.saldo < valor:
            return 'Saldo insuficiente para o saque.'
        else:
            self.saldo -= valor
            return f'Saque no valor de R${valor:.2f} realizado com sucesso'
            
    def exibir_saldo(self):
        return f'Saldo atual é de R${self.saldo:.2f}'

conta1 = ContaBancaria('Steven')

print(conta1.depositar(1000))
print(conta1.sacar(999))
print(conta1.exibir_saldo())