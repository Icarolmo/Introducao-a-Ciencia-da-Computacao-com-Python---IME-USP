import math

def soma(x,y):
    return x+y
    
def subtracao(x,y):
    return x-y
 
def multiplicacao(x,y):
    return x*y
    
def divisao(x,y):
    return x/y
   
def exponenciacao(x,y):
    return math.pow(x,y)
    
def raizQuadrada(x):
    return math.sqrt(x)

print('OLA ESTA E CALCULADORA COM ALGUMAS OPERACOES SIMPLES')
print('AUTOR: ICARO OLIVEIRA\n\n')


opcao = int(input('Escolha a operacao desejada abaixo.\n1-SOMA\n2-SUBTRACAO\n3-MULTIPLICAO\n4-DIVISAO\n5-EXPONENCIACAO\n6-RAIZ QUADRADA\n0-SAIR\n\nOpcao: '))
while opcao < 0 or opcao > 7:
    print('Valor invalido, por favor insira uma das opcoes validas abaixo')
    opcao = int(input('Escolha a operacao desejada abaixo.\n1-SOMA\n2-SUBTRACAO\n3-MULTIPLICAO\n4-DIVISAO\n5-EXPONENCIACAO\n6-RAIZ QUADRADA\n0-SAIR\n\nOpcao: '))
       
while opcao > 0 and opcao < 7:
    match (opcao):
        case (1):
            num1 = float(input('Insira o primeiro numero a ser somado: '))
            num2 = float(input('Insira o segundo numero a ser somado: '))
            aux = 1
            som = soma(num1,num2)
            while aux != 0:
                print('O resultado da sua soma inicial e', som)
                aux = float(input('Deseja acrescentar a soma?\nSe sim, insira o numero, se nao insira zero: '))
                som += aux
            print('O resultado da sua soma final foi',som)
            
        
        case (2):
            num1 = float(input('Insira o numero a ser subtraido: '))
            num2 = float(input('Insira o numero da subtracao: '))
            aux = 1
            sub = subtracao(num1,num2)
            while aux != 0:
                print('O resultado da sua subtracao inicial e', sub)
                aux = float(input('Deseja acrescentar a subtracao?\nSe sim, insira o numero a subtrair, se nao insira zero: '))
                sub -= aux
            print('O resultado da sua subtracao final foi', sub)
            
            
        case (3):
            num1 = float(input('Insira o numero a ser multiplicado: '))
            num2 = float(input('Insira o multiplicador: '))
            aux = 1
            multi = multiplicacao(num1,num2)
            while aux != 0:
                print('O resultado da sua multiplicacao inicial e',multi)
                aux = float(input('Deseja acrescentar a multiplicacao?\nSe sim, insira o numero a multiplicar o resultado, se nao insira zero: '))
                multi *= aux
            print('O resultado da sua multiplicacao final foi', multi)
            
            
        case (4):
            num1 = float(input('Insira o numerador: '))
            num2 = float(input('Insira o divisor: '))
            aux = 1
            div = divisao(num1,num2)
            while aux != 0:
                div = div / aux
                print('O resultado da sua divisao inicial foi', div)   
                aux = float(input('Deseja acrescentar a divisao?\nSe sim, insira o divisor para dividir o resultado novamente, se nao insira zero: '))      
            print('O resultado da sua divisao final foi', div)
            
            
        case (5):
            num1 = float(input('Insira o numero a ser elevado: '))
            num2 = float(input('Insira o expoente: '))
            aux = 1
            expo = exponenciacao(num1,num2)
            while aux != 0:
                expo = math.pow(expo,aux)
                print('O resultado da exponenciacao inicial e', expo)    
                aux = float(input('Deseja acrescentar a exponenciacao?\nSe sim, insira o expoente que ira elevar o resultado, se nao insira zero: '))
            print('O resultado da sua exponenciacao final foi', expo)
            
            
        case (6):
            num1 = float(input('Insira o numero a ser tirado a raiz quadrada: '))
            rQuadrado = raizQuadrada(num1)  
            print('O valor da raiz quadrada do numero inserido e', rQuadrado)
            
            
        case (0):
            print('Saindo...Ate logo!\n')
            quit()
       
    opcao = int(input('\nInsira a nova operacao desejada. Para sair digire zero.\n1-SOMA\n2-SUBTRACAO\n3-MULTIPLICAO\n4-DIVISAO\n5-EXPONENCIACAO\n6-RAIZ QUADRADA\n0-SAIR\n\nOpcao: '))
        
        
        
    


    
 