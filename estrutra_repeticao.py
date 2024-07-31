#for serve para repetir um bloco de código para cada item de uma sequência
texto = input('Digite um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra.upper())

else:
    print('o Else serve para executar no final do loop for.')

#range serve para criar uma sequência de números

for numero in range(10):
    print(numero, end=' ')

#exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=' ')

#while serve para repetir um bloco de código enquanto uma condição for verdadeira
while True:
    numero = int(input('Digite um número: '))

    if numero == 0:
        break

    print(f'O número digitado foi {numero}.')