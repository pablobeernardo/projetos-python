#Desenvolva uma função em Python que recebe uma tupla de números inteiros e retorna a soma de todos os elementos dessa tupla. A função deve ser capaz de lidar com tuplas de qualquer tamanho, contanto que todos os elementos sejam números inteiros. O objetivo é praticar a manipulação de tuplas e a utilização de funções em Python.
#Explicação de Resolução:
#1. Converta cada string na "lista_strings" em um número inteiro utilizando a função "int()".
#2. Use a função "map()" para aplicar a função "int()" a cada elemento da "lista_strings".
#3. Armazene o resultado em uma variável chamada "elementos".

def soma_tupla(tupla):
    return sum(tupla)


elementos = (map(int, input().split()))

resultado = soma_tupla(elementos)
print(f"A soma dos elementos da tupla é: {resultado}")

#Descrição
#Desenvolva uma função que receba duas listas de números inteiros separados por espaço e retorne uma lista contendo apenas os elementos que são comuns a ambas as listas, sem duplicatas.
#Detalhamento:Função elementos_comuns: 1. Crie a função que converte cada elemento das listas lista1 e lista2 para inteiro usando map(int, lista) antes de convertê-los em conjuntos (set) e encontrar a interseção entre eles. Isso garante que tratemos os elementos corretamente como números inteiros e não como strings.

def elementos_comuns(lista1, lista2):
    lista1 = set(map(int, lista1))
    lista2 = set(map(int, lista2))
    return list(lista1.intersection(lista2))

#Descrição: O desafio consiste em adicionar à função contar_caracteres um dicionário vazio chamado contador para armazenar as contagens de caracteres. Vamos iterar através de cada caractere na string string. Para cada caractere, verifique se ele já está presente no dicionário contador. Se estiver, incremente o valor associado a essa chave. Caso contrário, adicione a chave ao dicionário com valor inicial 1. Neste dicionário, as chaves são os caracteres presentes na string e os valores correspondem à contagem de vezes que cada caractere aparece.

def contar_caracteres(string):
    contador = {}
    for caractere in string:
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1
    return contador
