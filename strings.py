curso = "pyTHon"

# Converter a minúsculas
print(curso.lower())

# Converter a maiúsculas
print(curso.upper())

# Converter a primeira letra de cada palavra em maiúsculas
print(curso.title())

nome = "   José da Silva   "

# Remover espaços em branco à direita
print(nome.rstrip())

# Remover espaços em branco à esquerda
print(nome.lstrip())

# Remover espaços em branco à direita e à esquerda
print(nome.strip())

titulo = "Estudo"

# Centralizar o texto
print(titulo.center(20, '-'))

print(".".join(titulo))

#metodo format
nome = "José"
idade = 30
profissao = "Programador"

print("Olá, meu nome é {} e tenho {} anos. Sou {}.".format(nome, idade, profissao))
print("Olá, meu nome é {0} e tenho {1} anos. Sou {2}.".format(nome, idade, profissao))
print(f"Olá, meu nome é {nome} e tenho {idade} anos. Sou {profissao}.")

#fatiamento de strings
nome = "José da Silva"

print(nome[0]) #J - exibe o primeiro caractere
print(nome[0:4]) #José - exibe os caracteres da posição 0 até a posição 3
print(nome[5:]) #da Silva - exibe os caracteres da posição 5 até o final
print(nome[:4]) #José - exibe os caracteres do início até a posição 3
print(nome[-5:]) #Silva - exibe os 5 últimos caracteres
print(nome[::2]) #Jsd ilv - exibe os caracteres pulando de 2 em 2
print(nome[::-1]) #avliS ad ésoJ - exibe os caracteres em ordem reversa
print(nome[0:10:2]) #Js aSv - exibe os caracteres da posição 0 até a posição 9 pulando de 2 em 2