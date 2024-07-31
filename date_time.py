from datetime import date , datetime, timedelta


# Criar um objeto date
d = date(2020, 12, 31)
print(d)

# Acessar os atributos do objeto date
print(d.year)
print(d.month)
print(d.day)

#acessar data atual
data_atual = date.today()
print(data_atual)

#formatar data
data_atual = date.today()
data_formatada = data_atual.strftime("%d/%m/%Y")
print(data_formatada)

#hora atual
hora_atual = datetime.now()
print(hora_atual)

#formatar hora
hora_atual = datetime.now()
hora_formatada = hora_atual.strftime("%H:%M:%S")

print(hora_formatada)

#timedelta
data_atual = date.today()
data_futura = data_atual + timedelta(days=30)
print(data_futura)

#calcular diferença entre datas
data_atual = date.today()
data_futura = date(2021, 12, 31)
diferenca = data_futura - data_atual

print(diferenca.days)

#desafio lava jato - calcular o tempo que um carro vai demorar em minutos para ser lavado de acordo com o tamanho dele 

tipo_carro = "P"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual.strftime("%H:%M:%S")} e ficará pronto às {data_estimada.strftime("%H:%M:%S")}')
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou: {data_atual.strftime("%H:%M:%S")} e ficará pronto às {data_estimada.strftime("%H:%M:%S")}')
elif tipo_carro == "G": 
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou: {data_atual.strftime("%H:%M:%S")} e ficará pronto às {data_estimada.strftime("%H:%M:%S")}')
