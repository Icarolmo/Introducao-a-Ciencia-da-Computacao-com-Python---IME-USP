def maior_primo(n):
    while n > 0:
        aux = 1
        contador = 0
        while aux <= n:
            if (n % aux == 0):
                contador += 1
            aux += 1
        if (contador == 2):
            return n
        n -= 1


        

