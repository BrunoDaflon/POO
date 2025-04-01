class Contar:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 1

class MathHelper:
    @staticmethod
    def add(x,y):
        return x + y
    
class Student:
    def __init__(self,age):
        self.__age = age    # __age muda ele pra privado
    
    @property
    def get_age(self):
        return self.__age
    

    def age_setter(self,value):
        if value >= 0:
            self.__age = value
        

estudante = Student(1)
print(estudante.get_age)
estudante.age_setter(30)
print(estudante.get_age)