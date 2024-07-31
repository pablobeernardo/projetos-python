#set - elimina os elementos duplicados
set([1, 2, 3, 4, 5, 1, 2, 3]) #{1, 2, 3, 4, 5}
set("abacaxi")  #{'a', 'b', 'c', 'i', 'x'}
set(("palio", "gol", "uno", "gol"))  #{'palio', 'gol', 'uno'}

#convertendo o set pra uma lista
numero = {1, 2, 3, 4, 5}

numero = list(numero)
print(numero) #[1, 2, 3, 4, 5]

#metodos de set

#union - une dois sets
numeros1 = {1, 2, 3, 4, 5}
numeros2 = {4, 5, 6, 7, 8}

uniao = numeros1.union(numeros2)
print(uniao) #{1, 2, 3, 4, 5, 6, 7, 8}

#intersection - retorna os elementos em comum entre dois sets
intersecao = numeros1.intersection(numeros2)
print(intersecao) #{4, 5}

#difference - retorna os elementos que estão no set1 e não estão no set2
diferenca = numeros1.difference(numeros2)
print(diferenca) #{1, 2, 3}

#symmetric_difference - retorna os elementos que estão nos dois sets, mas não em ambos
diferenca_simetrica = numeros1.symmetric_difference(numeros2)
print(diferenca_simetrica) #{1, 2, 3, 6, 7, 8}

#issubset - verifica se um set é subconjunto de outro
subconjunto = {1, 2}
print(subconjunto.issubset(numeros1)) #True

#issuperset - verifica se um set é superconjunto de outro
superconjunto = {1, 2, 3, 4, 5, 6, 7, 8}
print(superconjunto.issuperset(numeros1)) #True

#isdisjoint - verifica se dois sets não tem elementos em comum
numeros3 = {6, 7, 8}
print(numeros1.isdisjoint(numeros3)) #True

#add - adiciona um elemento ao set
numeros1.add(6)
print(numeros1) #{1, 2, 3, 4, 5, 6}

#remove - remove um elemento do set
numeros1.remove(6)
print(numeros1) #{1, 2, 3, 4, 5}

#discard - remove um elemento do set, mas não gera erro se o elemento não existir
numeros1.discard(6)
print(numeros1) #{1, 2, 3, 4, 5}

#pop - remove um elemento aleatório do set
numeros1.pop()
print(numeros1) #{2, 3, 4, 5}

#clear - remove todos os elementos do set
numeros1.clear()

#copy - retorna uma cópia do set
numeros1 = {1, 2, 3, 4, 5}
copia = numeros1.copy()

