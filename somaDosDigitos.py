import math 

n = int(input("Digite um número: "))

soma = 0

while n > 0:
	soma = soma + (n % 10)
	n = n // 10

print(soma)