#alguns exemplos de listas em python

frutas = ["laranja", "banana", "abacaxi", "melancia"]

frutas = []

letras = list("abacaxi")

numeros = list(range(10))

carro = ["Ford", "Fiesta", "2019", "Preto", 42000]

# acessando elementos da lista

frutas = [0] #laranja
frutas = [1] #banana
frutas = [-1] #melancia
frutas = [-3] #banana

# matriz
matriz = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

# acessando elementos da matriz
matriz[0][0] #1
matriz[1][1] #5
matriz[2][2] #9

#fatiamendo de listas
lista = ["p", "y", "t", "h", "o", "n"]

lista[0:2] #['p', 'y'] - exibe os elementos da posição 0 até a posição 1
lista[:2] #['p', 'y'] - exibe os elementos do início até a posição 1
lista[2:] #['t', 'h', 'o', 'n'] - exibe os elementos da posição 2 até o final
lista[-1] #n - exibe o último elemento
lista[:-1] #['p', 'y', 't', 'h', 'o'] - exibe todos os elementos menos o último
lista[::2] #['p', 't', 'o'] - exibe os elementos pulando de 2 em 2
lista[::-1] #['n', 'o', 'h', 't', 'y', 'p'] - exibe os elementos em ordem reversa

#percorrendo listas
for fruta in frutas:
    print(fruta)

#enumerate
for indice, fruta in enumerate(frutas):
    print(indice, fruta)

#filtrando listas
numeros = [30, 4, 7, 11, 15, 22]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
# ou entao de um jeito mais pythonico
pares = [numero for numero in numeros if numero % 2 == 0]
#mesmo exemplo elevado ao quadrado
quadrados = [numero ** 2 for numero in numeros if numero % 2 == 0]

#metodos de listas

#append - adiciona um elemento ao final da lista
lista = []
lista.append("Python")
print(lista) #['Python']

#clear - remove todos os elementos da lista
lista = ["Python"]
lista.clear()
print(lista) #[]

#copy - retorna uma cópia da lista
lista = ["Python", 10, 3.14]
copia = lista.copy()
print(copia) #['Python', 10, 3.14]

#count - retorna a quantidade de vezes que um elemento aparece na lista
lista = ["Python", 10, 3.14, "Python"]
print(lista.count("Python")) #2

#extend - adiciona os elementos de uma lista a outra lista
lista = ["Python"]
lista.extend([10, 3.14])
print(lista) #['Python', 10, 3.14]

#index - retorna a posição de um elemento na lista
lista = ["Python", 10, 3.14]
print(lista.index(10)) #1

#pop - remove o ultimo elemento da lista ou um elemento em uma posição específica
lista = ["Python", 10, 3.14]
lista.pop()
print(lista) #['Python', 10]

lista.pop(0)
print(lista) #[10]

#remove - remove a primeira ocorrência de um elemento na lista ou remove um elemento em uma posição específica
lista = ["Python", 10, 3.14]
lista.remove()
print(lista) #[10, 3.14]

lista.remove(10)
print(lista) #['Python', 3.14]

#reverse - inverte a ordem dos elementos da lista
lista = ["Python", 10, 3.14]
lista.reverse()
print(lista) #[3.14, 10, 'Python']

#sort - ordena os elementos da lista
lista = [10, 3, 7, 1, 5]
lista.sort()
print(lista) #[1, 3, 5, 7, 10]

lista.sort(reverse=True)
print(lista) #[10, 7, 5, 3, 1]

lista = ["Python", "Java", "C", "JavaScript"]
lista.sort()
print(lista) #['C', 'Java', 'JavaScript', 'Python']

lista.sort(key=lambda x: len(x))
print(lista) #['C', 'Java', 'Python', 'JavaScript']

list.sort(key=lambda x: len(x), reverse=True)
print(lista) #['JavaScript', 'Python', 'Java', 'C']

#len - retorna o tamanho da lista
lista = ["Python", 10, 3.14]
print(len(lista)) #3



