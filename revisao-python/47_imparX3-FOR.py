contador = 0
soma = 0
for c in range (1, 501, 2): #Cotador de impar (NÃO PRECISA DO "if c % 2 == 1")
    if c % 2 == 1 and c % 3 == 0:
        contador += 1 #Contador de números
        soma += c #somatório de números que o resto é 1, que é multiplo de 3 com resto 0
print(f"{contador} números são ímpares e multiplos de 3, e a soma deles é igual a {soma}")
