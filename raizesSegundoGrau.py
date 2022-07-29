import math

a = float(input("Insira o valor da constante a: "))
b = float(input("Insira o valor da constante b: "))
c = float(input("Insira o valor da constante c: "))

delta = (b**2-4*a*c)

if delta < 0:
	print("esta equação não possui raízes reais")

if delta == 0: 
	bhaskaraP = (-b+math.sqrt(delta)) / (2*a)
	print("a raiz desta equação é",bhaskaraP)

if delta > 0: 
	bhaskaraN = (-b-math.sqrt(delta)) / (2*a)
	bhaskaraP = (-b+math.sqrt(delta)) / (2*a)
	if bhaskaraN > bhaskaraP:
		print("as raízes da equação são:",bhaskaraP,"e",bhaskaraN)
	else: 
		print("as raízes da equação são:",bhaskaraN,"e",bhaskaraP)	
	
	

