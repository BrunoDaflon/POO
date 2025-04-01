class Pessoa:
    def __init__(self, nome, cpf, altura, idade, profissao, salario):
        self.nome = nome
        self.__cpf = cpf
        self.altura = altura
        self.idade = idade
        self.profissao = profissao
        self.__salario = salario

    def mostra_cpf(self):
        return self.__cpf

    def mostra_salario(self):
        return self.__salario
    
    def habilidade(self):
        pass

pessoa1 = Pessoa("Bruno", "111.111.111-11" , 1.76, 31, "Desenvolvedor de Software", 9000.00)

cpf = pessoa1.mostra_cpf()

pessoa1.habilidade()

# print(f"{cpf[:4]}......{cpf[7:]}")

print(
    f"""
A pessoa cadastrada é {pessoa1.nome},
CPF: {cpf[:4]}...{cpf[8:]}
de altura {pessoa1.altura},
aos {pessoa1.idade} anos de idade,
Sua profissão é {pessoa1.profissao}
e ganha {pessoa1.mostra_salario()}
    """
)

#Public não tem "_"
#private tem 2 "__"
#protect tem 1 "_"