class Conta:
    def __init__(self, nome_cliente, numero_conta, agencia, senha):
        self.nome_cliente = nome_cliente
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.saldo = 0.0
        self.limite_cheque_especial = 500.0
        self.limite_cartao = 1000.0
        self.__pix = None
        self.__senha = senha

    def cadastrar_pix(self, chave_pix):
        self.__pix = chave_pix

    def cadastrar(self):
        print("Conta cadastrada com sucesso.")

    def autenticar(self, senha):
        return senha == self.__senha

    def pix(self, chave_origem, valor, conta_destino):
        if self.__pix == chave_origem and self.saldo >= valor:
            self.saldo -= valor
            conta_destino.depositar(valor)

    def cheque_especial(self, valor):
        if valor <= self.limite_cheque_especial:
            self.saldo += valor
            self.limite_cheque_especial -= valor

    def cartao_credito(self, valor):
        if valor <= self.limite_cartao:
            self.saldo += valor
            self.limite_cartao -= valor

    def depositar(self, valor):
        self.saldo += valor

    def debito(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def get_saldo(self):
        return self.saldo

    def get_pix(self):
        return self.__pix

    def set_senha(self, nova_senha):
        self.__senha = nova_senha


class Loja:
    def __init__(self):
        self.catalogo = []

    def adicionar_produto(self, produto, valor):
        self.catalogo.append((produto, valor))

    def remover_produto(self, produto):
        self.catalogo = [item for item in self.catalogo if item[0] != produto]

    def listar_produtos(self):
        for i, item in enumerate(self.catalogo):
            print(f"{i+1}. Produto: {item[0]}, Preço: R${item[1]:.2f}")

    def oferecer_promocao(self):
        print("Promoção: leve 3, pague 2 (só que não, rs)")

    def realizar_venda(self):
        print("Venda genérica realizada (essa será sobrescrita na loja física).")


class LojaFisica(Loja):
    def __init__(self):
        super().__init__()
        self._desconto = None

    def oferecer_promocao(self, desconto):
        self._desconto = desconto
        print(f"Promoção aplicada: {desconto}% de desconto nos produtos.")

    def realizar_venda(self, metodo, conta, item_index, produto):
        if 0 <= item_index < len(self.catalogo):
            nome_produto, preco = self.catalogo[item_index]
            if nome_produto != produto:
                print("Produto não corresponde ao índice.")
                return
            if self._desconto:
                preco *= (1 - self._desconto / 100)
            if metodo == "debito":
                conta.debito(preco)
            elif metodo == "pix":
                conta.pix(conta.get_pix(), preco, conta)
            elif metodo == "credito":
                conta.cartao_credito(preco)
            elif metodo == "cheque":
                conta.cheque_especial(preco)
            print(f"Venda realizada: {produto} por R${preco:.2f}")
        else:
            print("Índice do produto inválido.")


conta1 = Conta("Brunão", "12345", "0001", "senha123")
conta1.depositar(1000.0)
conta1.cadastrar_pix("brunao@pix")

loja = LojaFisica()

loja.adicionar_produto("Camisa", 150.0)
loja.adicionar_produto("Calça", 200.0)
loja.adicionar_produto("Tênis", 350.0)

print("\nProdutos na loja")
loja.listar_produtos()

loja.oferecer_promocao(10)

print("\nRealizando venda")
loja.realizar_venda("debito", conta1, 0, "Camisa")

print("\nSaldo final da conta")
print(f"R${conta1.get_saldo():.2f}")
