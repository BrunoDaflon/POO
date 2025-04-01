class Student:
    # definindo o nosso método construtor e atributos
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grades(self,grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len (self.grades)
    
    @property
    def is_passing(self):
        return self.get_average_grade() >=60
    
    @classmethod
    def main(cls):
        students = []

        while True:
            print("1 - Adicionar Aluno")
            print("2 - Adicionar Nota")
            print("3 - Verificar Aprovação")
            print("4 - Listar alunos")
            print("5 - Sair")
            choice = int(input("Escolha a opção: "))

            if choice == 1:
                name = input("Nome do aluno: ")
                age = int(input("Idade do aluno: "))
                student = cls(name,age)
                students.append(student)
                print("Aluno Adicionado!")

            elif choice == 2:
                if not students:
                    print("Nenhum aluno cadastrado!")
                    continue
                for idx, student in enumerate(students):
                    print(f"{idx+1} - {student.name}")
                student_idx = int(input("Escolha o número do aluno: ")) -1

                if 0 <= student_idx < len(students):
                    grade = float(input("Nota do aluno: "))
                    students[student_idx].add_grades(grade)
                    print("Nota adicionada!")
                else:
                    print("Indice de aluno inválido!")

            elif choice == 3:
                if not students:
                    print("Nenhum aluno cadastrado!")
                    continue
                for student in students:
                    average_grade = student.get_average_grade()
                    if average_grade >= 6.0:
                        status = "Aprovado"
                    else:
                        status = "Reprovado"
                    print(f"{student.name} - Média: {average_grade} - Status: {status}")

            elif choice == 4:
                if not students:
                    print("Nenhum aluno encontrado!")
                for student in students:
                    print(f"Nome: {student.name} - Idade: {student.age} - Nota: {student.grades}")
                

            elif choice == 5:
                print("Saindo...")
                print("Obrigado por usar o nosso sistema")
                print("Até a proxima")
                break
            else:
                print("Opção inválida, tente novamente!")

estudante = Student.main()