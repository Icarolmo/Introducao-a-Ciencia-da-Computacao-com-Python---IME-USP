import math

numero = int(input("Digite um número inteiro: "))
nAdjacente = False

nAnt = numero % 10
numero = numero // 10
nPos = numero % 10



while numero > 0 and not nAdjacente:
	if nAnt == nPos:
		nAdjacente = True
		
	else:
		nAnt = numero % 10
		numero = numero // 10
		nPos = numero % 10

if nAdjacente: 
	print("sim")
else:
	print("não")
	



		
	