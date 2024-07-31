#iteradores em python
#significa que voce pode percorrer todos os elementos de um objeto, como uma lista, tupla, dicionario, etc.
#os metodos mais comuns de iteradores sao: __iter__ e __next__

#exemplo de iterador
class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador([1,2,3,4,5]):
    print(i)

        