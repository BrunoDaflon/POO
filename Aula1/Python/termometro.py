# Estrutruado

#temp = float(input("Digite a temperatura: "))
#if temp < 36:
#    print("Hipotermia")
#elif temp >= 36 and temp <= 36.5:
#    print("Normal")
#elif temp > 36.5 and temp <= 37.5:
#    print("Pré-Febre")
#else:
#    print("Febre")


# Função
'''
def termometro():
    temp = float(input("Digite a temperatura: "))
    if temp < 36:
        print("Hipotermia")
    elif temp >= 36 and temp <= 36.5:
        print("Normal")
    elif temp > 36.5 and temp <= 37.5:
        print("Pré-Febre")
    else:
        print("Febre")

termometro()
'''
# class sem atributos
'''
class Termometro:
    def termometro():
        temp = float(input("Digite a temperatura: "))
        if temp < 36:
            print("Hipotermia")
        elif temp >= 36 and temp <= 36.5:
            print("Normal")
        elif temp > 36.5 and temp <= 37.5:
            print("Pré-Febre")
        else:
            print("Febre")

Termometro.termometro()
'''

# Definiu a classe
class Temperatura:
    # Define o método construtor e atributos
    def __init__(self):
        self.hipotermia = "Hipotermia"
        self.normal = "Normal"
        self.pre_febre = "Pré-Febre"
        self.febre = "Febre"
 
    def termometro(self):
        temperatura_da_pessoa = float(input('Digite a temperatura aferida: '))
 
        if temperatura_da_pessoa < 36:
            print(f'{temperatura_da_pessoa}°C é uma temperatura de {self.hipotermia}')
        elif 36 <= temperatura_da_pessoa <= 37:
            print(f'{temperatura_da_pessoa}°C é uma temperatura de {self.normal}')
        elif 37.1 <= temperatura_da_pessoa <= 37.5:
            print(f'{temperatura_da_pessoa}°C é uma temperatura de {self.pre_febre}')
        else:
            print(f'{temperatura_da_pessoa}°C é uma temperatura de {self.febre}')
 
 
temperatura = Temperatura()
temperatura.termometro()
 