from Carro import Carro as Car

carro1 = Car("Fiat", "Uno com escada em cima", 2009, "Branco", "XTS85GH")
carro2 = Car("VW", "Gol quadrado", 2007, "Vermelho", "GH12HF")
print(carro1)
carro1.ligar_carro()
for i in range(30):
    carro1.acelerar()

for i in range(30):
    carro1.freiar()

for i in range(5):
    carro1.acelerar(True)


# print(carro1)
# print()
# print(carro2)

#Usando o cadastro de vendas
# carro3 = Car.cadastro_venda()
# print(carro1, carro2)

# carro2.ligar_carro()
# for i in range(5):
#     carro2.acelerar()
#     carro2.contador_marcha()

# for i in range(13):
#     carro2.freiar()
#     carro2.contador_marcha()
# for i in range(2):
#     carro2.freiar()
# for i in range(1):
#     carro2.re_no_carro()
