#manipulando_arquivos

#abrir e fechar arquivos
#open() -> na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que é o nome do arquivo a ser lido. Essa função retorna um objeto do tipo arquivo que pode ser utilizado para leitura ou escrita.
#close() -> fecha o arquivo
#exemplo:
file = open('arquivo.txt', 'r') #abre o arquivo para leitura
print(file.read()) #lê o conteúdo do arquivo
print(file.readline()) #lê a primeira linha do arquivo
print(file.readlines()) #lê todas as linhas do arquivo
print(file.read(10)) #lê os 10 primeiros caracteres do arquivo


file = open('arquivo.txt', 'w') #abre o arquivo para escrita
print(file.write('Escrevendo no arquivo')) #escreve no arquivo


file = open('arquivo.txt', 'a') #abre o arquivo para anexar conteúdo
print(file.write('Anexando conteúdo ao arquivo')) #anexa conteúdo ao arquivo


file.close() #fecha o arquivo

#gerenciar arquivos
#with -> é uma forma de gerenciar recursos que são utilizados em um bloco de código. Ele garante que os recursos sejam liberados ao final do bloco, mesmo que ocorra uma exceção.
#exemplo:
with open('arquivo.txt', 'r') as file:
    print(file.read())

#manipulando arquivos csv
#csv -> é um formato de arquivo que armazena dados separados por vírgula. Ele é muito utilizado para armazenar dados em tabelas.
#exemplo:
import csv

with open('arquivo.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Idade', 'Sexo'])
    writer.writerow(['Maria', 25, 'Feminino'])
    writer.writerow(['João', 30, 'Masculino'])

with open('arquivo.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


#manipulando arquivos json
#json -> é um formato de arquivo que armazena dados em formato de texto. Ele é muito utilizado para armazenar dados em objetos.
#exemplo:
import json

dicionario = {
    'Nome': 'Maria',
    'Idade': 25,
    'Sexo': 'Feminino'
}

with open('arquivo.json', 'w') as file:
    json.dump(dicionario, file)

with open('arquivo.json', 'r') as file:
    dicionario = json.load(file)
    print(dicionario)

