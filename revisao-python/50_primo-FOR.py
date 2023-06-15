numero = int(input("Digite um número: "))
contador_primo = 0

for c in range (1, numero + 1): 
    if numero % c == 0:
        contador_primo += 1
    print(c, end=" => ")
print("Acabou!!!")
print(f"O número {numero} foi dividido {contador_primo} vezes.")

if contador_primo == 2:
    print("É um número PRIMO.")
else:
    print("É um número NÃO PRIMO.")

