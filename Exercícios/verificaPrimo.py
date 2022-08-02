import math 

n = int(input("Digite um número inteiro: "))

verific = 0
cont = 1

while cont <= n/2:
	if( n % cont == 0):
		verific += 1
	cont += 1

if( verific == 1 ):
	print("primo")

else:
	print("não primo")

