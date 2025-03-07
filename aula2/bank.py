class Banco:
    def __init__(self, agencia, conta, nome):
        self.banco = "Saqua da Eng - Software"
        self.agencia = agencia
        self.conta = conta
        self.nome = nome
        self.saldo = 0

    def __str__(self):
        return f"O cliente: {self.nome} foi cadastrado!"
    
    def deposito(self, valor):
        if valor > 0 or isinstance(valor, (int, float)):
            self.saldo = valor
            print(f"O deposito de R${valor} foi realizado na conta de {self.nome}")
    
    def pix(self, destinatario, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destinatario.saldo += valor
            print(
                f"""
-------------------------
Banco: {self.banco}
Valor transferido: {valor}
De: {self.nome}
Para: {destinatario.nome} Banco: {destinatario.banco}
-------------------------
                """
            )
    
    def extrato(self):
        print(
            f"""
-------------------------
Cliente: {self.nome}
Conta: {self.conta}
Agencia: {self.agencia}
Saldo: {self.saldo}
-------------------------
            """
        )