texto = input('Digite um texto: ')

def conta_vogais(texto):
    VOGAIS = 'AEIOU'
    contagem = 0

    for letra in texto:
        if letra.upper() in VOGAIS:
            contagem += 1

    print(f'O texto digitado possui {contagem} vogais.')


conta_vogais(texto)