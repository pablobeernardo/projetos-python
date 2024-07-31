#encapsulamento em python

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = "123.456.789-00" #atributo privado
    
    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.__cpf}")
    
    def __exibir_cpf(self): #método privado
        print(f"CPF: {self.__cpf}")

p1 = pessoa("José", 30)
p1.exibir()
#p1.__exibir_cpf() #erro, método privado
print(p1._pessoa__cpf) #acessando o atributo privado
p1._pessoa__exibir_cpf() #acessando o método privado

#propriedades em python

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = "123.456.789-00" #atributo privado
    
    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.__cpf}")
    
    def __exibir_cpf(self): #método privado
        print(f"CPF: {self.__cpf}")
    
    @property #permite acessar o atributo privado
    def cpf(self):
        return self.__cpf
    
    @cpf.setter #altera o valor do atributo privado
    def cpf(self, cpf):
        self.__cpf = cpf

p1 = pessoa("José", 30)
p1.exibir() #exibe o cpf padrão
p1.cpf = "987.654.321-00" #altera o cpf
p1.exibir() #exibe o cpf alterado

