contador = 0
soma = 0
for c in range (0, 7):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0: #Se for par
        contador += 1
        soma += numero
print(f"Foram registrados {contador} números pares e a soma entre eles é de {soma}")
