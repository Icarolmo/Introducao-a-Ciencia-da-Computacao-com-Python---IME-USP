numero = int(input("Digite um número inteiro: "))

dezena = numero%10000
dezena = dezena%1000
dezena = dezena%100
dezena = dezena//10

print("O dígito das dezenas é", dezena)