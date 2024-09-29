class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # atributo privado
    
    def depositar(self, valor):
        self.__saldo += valor
        print(f"Deposito de R${valor} feito com sucesso!")
    
    def retirar(self, valor):
        self.__saldo -= valor
        print(f"Saque de R${valor} feito com sucesso!")
    
    def consultar_saldo(self):
        return self.__saldo

conta1 = ContaBancaria(100) # iniciando com o valor fixo
print(f"Saldo Inicial: R${conta1.consultar_saldo()}\n")

# Fazendo o depósito
conta1.depositar(150)
print(f"Saldo Atual: R${conta1.consultar_saldo()}\n")

# Fazendo o saque
conta1.retirar(25)
print(f"Saldo Atual: R${conta1.consultar_saldo()}")
