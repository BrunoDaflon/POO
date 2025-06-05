#Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"""
        Nome: {self.nome}, idade {self.idade}
"""
    
#Classe Aluno
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso
        self.nota = 0

    def apresentar(self):
        return f"""
        {super().apresentar()}, Matricula {self.matricula}, curso: {self.curso}.
"""
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, departamento):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.departamento = departamento

    def apresentar(self):
        return f"""
        {super().apresentar()}, Disciplina: {self.disciplina}, Departamento: {self.departamento}.
"""
    def conversar(self, aluno):
        print(f"O professor {self.nome} e o aluno {aluno.nome} estão conversando sobre a matéria de {self.disciplina}.")

    def gerar_nota(self, aluno, nota):
        print(f"{self.nome} deu {nota} pontos para o aluno {aluno.nome}.")
        aluno.nota += nota
        print(f"{aluno.nome}: {aluno.nota}")

#Classe anêmica e polifórmica
class ApresentarTodos:
    def mostrar(self, pessoa):
        print(pessoa.apresentar())

#Apresentando Aluno e Professor
aluno1 = Aluno("Bruno", 31, "123", "Engenharia de Software")
professor1 = Professor("Diego", 40, "POO", "Programação")

#Classe Polifórmica
apresentando = ApresentarTodos()
apresentando.mostrar(aluno1)
apresentando.mostrar(professor1)

#Interação Professor com o aluno
professor1.conversar(aluno1)

#Professor atribuindo nota ao aluno
professor1.gerar_nota(aluno1, 6.5)
professor1.gerar_nota(aluno1,8.5)
