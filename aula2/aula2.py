class Pessoa:
     def __init__(self, nome, genero, cpf):
          self.nome = nome
          self.genero = genero
          self.cpf = cpf

pessoa1 = Pessoa("Bruno", "M", 123456789)
print(pessoa1.genero)