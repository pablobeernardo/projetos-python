MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Digite sua idade: '))

if idade >= MAIOR_IDADE:
    print('Você pode tirar sua CNH.')

elif idade == IDADE_ESPECIAL: 
    print('Você pode tirar sua CNH, mas não pode dirigir.')

else:
    print('Você ainda não pode tirar sua CNH.')    