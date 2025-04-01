# Definindo um método construtor
class Animal:
    # Método construtor
    def __init__(self, nome, genero,idade,especie):
        self.nome = nome      
        self.genero = genero
        self.idade = idade
        self.especie = especie


    #Método de apresentação
    #Método de classe
    def __str__(self):
        return f"""
O animal é um(a) {self.nome} {self.genero},  tem {self.idade} anos de idade, sua especie é {self.especie}.
"""
    # Método de instancia
    @classmethod
    def cadastrar_animal(cls):
        nome = input("Animal: ")
        especie = input("Insira a espécie: ")
        return cls(nome,especie)
    