saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Saldo insuficiente"
print(f"{status} ao realizar o saque!")