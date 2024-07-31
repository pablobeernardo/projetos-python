#passagem_parametros.py
# Decoradores, Iteradores e Geradores

def mensagem(nome):
    print("executando mensagem")
    return f"Olá, {nome}"

def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá, {nome}, espero que você esteja bem!"

def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)

print(executar(mensagem, "José"))
print(executar(mensagem_longa, "Maria"))


#### funcao interna

def mensagem():
    print("executando mensagem")
    
    def mensagem_interna():
        print ("Olá")
    
    def mensagem_interna_longa():
        print("Olá, espero que você esteja bem!")
    
    mensagem_interna()
    mensagem_interna_longa()

mensagem()

#retornar funcao
def calculadora(operacao):
    def soma(a,b):
        return a + b
    
    def subtracao(a,b):
        return a - b
    
    def multi(a,b):
        return a * b
    
    def div(a,b):
        return a / b
    
    if operacao == "soma":
        return soma
    elif operacao == "subtracao":
        return subtracao
    elif operacao == "multiplicacao":
        return multi
    elif operacao == "divisao":
        return div
    
print(calculadora('soma')(2,3))
print(calculadora('subtracao')(2,3))
print(calculadora('multiplicacao')(2,3))
print(calculadora('divisao')(2,3))

#acucar sintatico
def meu_decorador(funcao):  
    def funcao_interna():   
        print("faz algo antes de executar a funcao")
        funcao()
        print("faz algo depois de executar a funcao")

    return funcao_interna

@meu_decorador #decorador
def minha_funcao(): 
    print("executando minha funcao")

minha_funcao() #executando minha funcao


#args e kwargs

def meu_decorador(funcao):  
    def funcao_interna(*args, **kwargs):   
        print("faz algo antes de executar a funcao")
        funcao(*args, **kwargs)
        print("faz algo depois de executar a funcao")

    return funcao_interna

@meu_decorador 
def minha_funcao(nome): 
    print(f"Olá mundo {nome}")

minha_funcao('João') 

#Decorador retorna funcao

#para fazer introspecção, ou seja, para acessar os atributos e métodos de um objeto, é necessário retornar a função interna do decorador.
# import functools
def meu_decorador(funcao):
    # @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("faz algo antes de executar a funcao")
        resultado = funcao(*args, **kwargs)
        print("faz algo depois de executar a funcao")
        return resultado
    
    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá, {nome}! {outro_argumento}")
    return nome.upper() 

resultado = ola_mundo("João", "Tudo bem?")
print(resultado)