# defini uma classe
class Pessoa:
    # definindo o nosso metodo construtor e os atributos
    def __init__(self, nome, sobrenome, idade, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf

    # Método
    def comprimentar(self):
        var = input("Digite algo: ")
        if var == "Olá" or var == "OLá" or var == "olá":
            print(f"Ele quer dizer: {var}")
        else:
            print("Opção errada")
    
    def reclamar(self):
        print(f"{self.nome} não gostou do que esta acontecendo!")

# definindo um objeto
pessoa1 = Pessoa("Zé", "das Coves", 40, 1234567800)

pessoa2 = Pessoa("João", "das Coves", 35, 1234567800)

print(f"A pessoa definida é {pessoa1.nome, pessoa1.sobrenome}")

print(pessoa1.comprimentar())

print(pessoa2.comprimentar())

print(pessoa2.reclamar())