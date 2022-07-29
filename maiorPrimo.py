def maior_primo(n):
	if n < 2:
		return print("Erro: número menor que 2")
	
	cont = n
	while (cont > n/2):
		cont2 = 2
		while (cont2 <= n/2):
			if cont % cont2 == 0:
				verificador = 1
			cont2 += 1
		if verificador == 0:
			return cont
		else:
			cont -= 1
	

num = int(input("Insira um numero: "))

print(maior_primo(num))

	
	
		
		
		 
		