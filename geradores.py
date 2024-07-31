# geradores sao uma forma mais simples de criar iteradores, 
# não armazenam todos os valores em memória, mas sim geram os valores sob demanda

#ao inves de utilizar a palavra reservada return, utilizamos a palavra reservada yield

#exemplo de gerador
def meu_gerador(numeros: list[int]):
   for numero in numeros: 
         yield numero * 2

for i in meu_gerador(numeros=[1,2,3,4,5]):
    print(i)