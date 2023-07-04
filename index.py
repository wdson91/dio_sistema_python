# Classe que representa a conta bancária
class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.historico = []

    def deposito(self, valor):
        self.saldo += valor
        self.historico.append(f"Depósito: +{valor}")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: -{valor}")
        else:
            print("Saldo insuficiente para o saque.")

    def extrato(self):
        print("Extrato:")
        for transacao in self.historico:
            print(transacao)
        print(f"Saldo atual: {self.saldo}")


# Exemplo de uso do sistema bancário
conta = ContaBancaria()

conta.deposito(1000)
conta.saque(500)
conta.deposito(200)
conta.saque(1500)  # Saldo insuficiente

conta.extrato()
