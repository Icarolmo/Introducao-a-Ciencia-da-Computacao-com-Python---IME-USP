def maximo(x,y,z):
	if x > y and x > z:
		return x
	elif y > x and y > z:
		return y
	else: 
		return z

def teste_maximo0():
    assert maximo(999,3,50) == 999
    

