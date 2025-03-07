class Banco:
    def __init__(self, banco, agencia, conta, cliente, cpf):
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.cliente = cliente
        self.cpf = cpf
        self.saldo = 0
        self.caixinha = 0
        self.tempo_investimento = None
        self.taxa_juros = 0.005
        self.senha = None
    

    def definir_senha(self, new_senha):
        if self.senha == None:
            self.senha = new_senha
            print("Sua senha foi definida!")
        elif self.senha != None:
            decisao = input("Você já possuí uma senha definida, deseja mudara a senha mesmo assim?").lower()
            if decisao == "sim":
                self.senha = new_senha
        else:
            print("Escolha errada!")

    # método de apresentação
    def __str__(self):
        return f"""
Cliente {self.cliente} cadastrado com sucesso:
Conta: {self.conta}
Agencia: {self.agencia}
Banco: {self.banco}
        """
    # deposito
    def deposito(self, valor):
        if isinstance(valor, (int, float)):
            self.saldo += valor
            print(f"Saldo atualizado com sucesso no valor de R${float(valor)}.")
    # saque
    def saque(self, senha, valor):
        if self.senha == senha and self.saldo >= valor and isinstance(valor, (int, float)):
            self.saldo -= valor
            print(f"Saque realizado no valor de: {float(valor)}")
        else:
            print("Valor ou senha incorreta, tente novamente!")
    
    # Pix
    def pix(self, destinatario, valor):
        if isinstance(valor, (int, float)) and self.saldo >= valor:
            self.saldo -= valor
            destinatario.saldo += valor
            print(
                f"""
Pix realizado no valor de R${valor}
De: {self.cliente}
Para: {destinatario.cliente}
                """
            )

    # Caixinha
    def caixinha_invest(self, valor, tempo_meses):
        if isinstance(valor, (int, float)) and self.saldo >= valor:
            self.saldo -= valor
            self.caixinha += valor
            self.tempo_investimento = tempo_meses
            print(f"Valor de R${float(valor)} transferido para caixinha por {tempo_meses} meses")
        else:
            print(f"Valor digitado de forma errada ou saldo menor que o valor definido R${float(valor)}")
    
    def calcular_rendimento(self):
        if self.tempo_investimento is not None and self.caixinha > 0:
            # Juros compostos:  M = C *(1+i)^t
            montante = self.caixinha * (1 + self.taxa_juros) ** self.tempo_investimento
            rendimento = montante - self.caixinha
            self.caixinha = montante
            print(f"Rendimento da caixinha apo´s {self.tempo_investimento} meses: R${rendimento:.2f}")
            self.tempo_investimento = None
        else:
            print("Não existe inventimento no momento!")

    # Extrato
    def extrato(self):
        print(
            f"""
------------------------------------
Conta: {self.conta}
Agencia: {self.agencia}
Saldo: {self.saldo}
Cliente: {self.cliente}
------------------------------------
            """
        )