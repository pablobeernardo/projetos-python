conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 1000

if conta_normal:
    if saldo >= saque:
        saldo -= saque
        print('Saque efetuado com sucesso!')
    else:
        if saldo + cheque_especial >= saque:
            saldo -= saque
            print('Saque efetuado com sucesso!')
        else:
            print('Saldo insuficiente!')

elif conta_universitaria:
    if saldo >= saque:
        saldo -= saque
        print('Saque efetuado com sucesso!')
    else:
        print('Saldo insuficiente!')

else:
    print('Tipo de conta inválido!')