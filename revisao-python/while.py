numero = 1
par = impar = 0 # 2 valores assumen o valor "0"

while numero != 0:
    numero = int(input("Digite um número: "))
    if numero != 0: # para o zero "0" não contar como valor
        if numero % 2 == 0:
            #par
            par += 1 # contador par
        else:
            #impar
            impar += 1 #contador impar
print(f"Você digitou {par} números PARES e {impar} números IMPARES.")
