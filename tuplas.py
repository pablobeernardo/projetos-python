#tupla é parecido com lista, mas é imutável

#criando uma tupla
tupla = (1, 2, 3, 4, 5)
print(tupla) #(1, 2, 3, 4, 5)

letras = tuple('Python')
print(letras) #('P', 'y', 't', 'h', 'o', 'n')

#tupla com um único elemento
tupla = (1,) #não esqueça da vírgula
print(tupla) #(1,)

#tupla sem parênteses
tupla = 1, 2, 3, 4, 5 #não é necessário usar parênteses
print(tupla) #(1, 2, 3, 4, 5)

#tupla com diferentes tipos de dados
tupla = (1, 'Python', 3.14) #int, str, float
print(tupla) #(1, 'Python', 3.14)

#tupla aninhada
tupla = (1, (2, 3), (4, 5)) #tupla dentro de tupla
print(tupla) #(1, (2, 3), (4, 5))

#tupla com range
tupla = tuple(range(10)) #converte range para tupla
print(tupla) #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

#tupla com listas
tupla = tuple([1, 2, 3, 4, 5]) #converte lista para tupla
print(tupla) #(1, 2, 3, 4, 5)

#tupla com strings
tupla = tuple('Python') #converte string para tupla
print(tupla) #('P', 'y', 't', 'h', 'o', 'n')

#fatiamendo de tuplas
tupla = ("p", "y", "t", "h", "o", "n")

print(tupla[0:2]) #('p', 'y') - exibe os elementos da posição 0 até a posição 1
print(tupla[:2]) #('p', 'y') - exibe os elementos do início até a posição 1
print(tupla[2:]) #('t', 'h', 'o', 'n') - exibe os elementos da posição 2 até o final
print(tupla[-1]) #n - exibe o último elemento
print(tupla[:-1]) #('p', 'y', 't', 'h', 'o') - exibe todos os elementos menos o último
print(tupla[::2]) #('p', 't', 'o') - exibe os elementos pulando de 2 em 2
print(tupla[::-1]) #('n', 'o', 'h', 't', 'y', 'p') - exibe os elementos em ordem reversa


#metodos de tuplas

#count - conta o número de ocorrências de um elemento
tupla = (1, 2, 2, 3, 4, 2)
print(tupla.count(2)) #3

#index - retorna o índice da primeira ocorrência de um elemento
tupla = (1, 2, 3, 4, 5)
print(tupla.index(3)) #2

#len - retorna o número de elementos da tupla
tupla = (1, 2, 3, 4, 5)
print(len(tupla)) #5