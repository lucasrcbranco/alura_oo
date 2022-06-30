class Conta:
    def __init__(
            self,
            numero: str,
            titular: str,
            saldo: float = 0,
            limite: float = 1000):
        self.__titular = titular
        self.__numero = numero
        self.__limite = limite
        self.saldo = saldo
        self.__codigo_banco = "001"

    def extrato(self):
        print(f"O saldo da conta de número {self.__numero} é R$ {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print(f"Falha ao realizar o saque.")

    def realizar_transferencia(self, conta, valor):
        self.sacar(valor)
        conta.depositar(valor)

    def receber_transferencia(self, conta, valor):
        conta.sacar(valor)
        self.depositar(valor)

    # getter
    @property
    def codigo_banco(self):
        return self.__codigo_banco

    # static method
    @staticmethod
    def codigo_banco():
        return "001"

contaLucas: Conta = Conta("123", "Lucas")
contaJhen: Conta = Conta("321", "Jhennifer")
contaLucas.realizar_transferencia(contaJhen, 20)

contaLucas.extrato()
contaJhen.extrato()
print(Conta.codigo_banco())