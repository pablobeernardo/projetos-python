#Polimorfismo
#Mesmo metodo em classes diferentes, com comportamentos diferentes

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal voando...")

class Pinguim(Passaro):
    def voar(self):
        print("Pinguim não voa...")

def plano_de_voo(passaro):
    passaro.voar()

#Polimorfismo - mesmo método em classes diferentes, com comportamentos diferentes
plano_de_voo(Pardal()) #Pardal voando...
plano_de_voo(Pinguim()) #Pinguim não voa...