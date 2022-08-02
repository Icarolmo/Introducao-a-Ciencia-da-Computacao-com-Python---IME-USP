def fatorial(n):
	fat = 1
	while n >= 1:
		fat = fat*n
		n = n - 1
	return fat

def coeficienteBinomial(n,k):
	return (fatorial(n))/(fatorial(k)*fatorial(n-k))


n1 = int(input("Insira o valor de n!: "))
n2 = int(input("Insira o valor de k!: "))

print("o valor do coeficientes binomiais é: ",coeficienteBinomial(n1,n2))

