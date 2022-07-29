import math

print("Calcularemos a distância entre dois pontos no plano cartesiano")
print("utilizaremos a fórmula da distância: d(x,y) = raiz de (x1 - x2)² + (y1 - y2)²")
x1 = float(input("Insira o valor de x1: "))
y1 = float(input("Insira o valor de y1: "))
x2 = float(input("Agora insira o valor de x2: "))
y2 = float(input("e por fim o valor de y2: "))
 
print()

distancia =  math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))


if distancia >= 10 : 
	print("longe")
else: 
	print("perto")


	