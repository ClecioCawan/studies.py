numero = int(input("Digite um número: "))

par = numero % 2 #Um número dividido por 2 e o seu resto for 0 ele é par

if par == 0:
    print(f"O número {numero} é PAR.")

else: #Caso seja difrente de zero, ou seja, 1
    print(f"O número {numero} é ÍMPAR.")