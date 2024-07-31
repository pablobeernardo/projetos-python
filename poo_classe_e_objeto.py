#Exemplo bicicletaria

#metodo construtor
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Bibi!")
    
    def parar(self):
        print("Freando a bicicleta!")
        print("Bicicleta parada!")

    def correr(self):
        print("Pedalando a bicicleta!")
        print("Bicicleta em movimento!") 

    def __str__(self):
        return f"{self.cor}, {self.modelo}, {self.ano}, {self.valor}"

b1 = Bicicleta("vermelha", "Caloi", 2020, 500.00)
b2 = Bicicleta("azul", "Monark", 2021, 800.00)

b1.buzinar()
b1.parar()
b1.correr()

b2.buzinar()
b2.parar()
b2.correr()

print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b2.cor, b2.modelo, b2.ano, b2.valor)


#desafio
#mplemente uma classe ConversorTemperatura que converte temperaturas de Celsius para Fahrenheit. A classe deve incluir um método chamado celsius_para_fahrenheit que realiza o cálculo de conversão. A fórmula para converter de Celsius para Fahrenheit é:
#Fahrenheit=(Celsius×95)+32Fahrenheit=(Celsius×59​)+32
#Você também deverá criar uma instância do conversor e utilizar essa instância para realizar a conversão.

#: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:
class ConversorTemperatura:
    def celsius_para_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

# Entrada do usuário
celsius = float(input())

# : Crie uma instância do conversor:
conversor = ConversorTemperatura()


fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)