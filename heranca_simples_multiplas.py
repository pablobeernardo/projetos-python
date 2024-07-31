#conceito de herança simples em python

class veiculo:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Bibi!")
    
    def parar(self):
        print("Freando o veiculo!")
        print("Veiculo parado!")
    
    def __str__(self) -> str:
        return f"{self.cor}, {self.modelo}, {self.ano}, {self.valor}"

class bicicleta(veiculo):
    pass    

class carro(veiculo):
    pass

b1 = bicicleta("vermelha", "Caloi", 2020, 500.00) #objeto herdado da classe veiculo
b2 = carro("azul", "Monark", 2021, 800.00) #objeto herdado da classe veiculo

b1.buzinar()
b1.parar()

b2.buzinar()
b2.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b2.cor, b2.modelo, b2.ano, b2.valor)


#herança multipla em python

class animal:
    def __init__(self, num_patas, habitat):
        self.num_patas = num_patas
        self.habitat = habitat
    
    def comer(self):
        print("Comendo...")
    
    def dormir(self):
        print("Dormindo...")


class mamifero(animal):
    def __init__(self, num_patas, habitat, especie):
        super().__init__(num_patas, habitat)
        self.especie = especie
    
    def amamentar(self):
        print("Amamentando...")

class ave(animal):
    def __init__(self, num_patas, habitat, especie):
        super().__init__(num_patas, habitat)
        self.especie = especie
    
    def voar(self):
        print("Voando...")

class ornitorrinco(mamifero, ave):
    def __init__(self, num_patas, habitat, especie):
        super().__init__(num_patas, habitat, especie)

o1 = ornitorrinco(4, "aquático", "Ornithorhynchus anatinus")
o1.comer()
o1.dormir()

class gato(mamifero):
    def __init__(self, num_patas, habitat, especie):
        super().__init__(num_patas, habitat, especie)

g1 = gato(4, "terrestre", "Felis catus")
g1.comer()
g1.dormir()


