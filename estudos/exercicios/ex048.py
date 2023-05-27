#-------------------SOMA de números impares multiplos de 3----------- #
soma = 0 #Acumulador
contador = 0 # Contador

for c in range(1, 501, 2):

    if c % 3 == 0: # Se o laço (c) for ímpar(divisivel(%) por 3)
        
        soma += c # O acumulador vai somar (acumular) os números
        # soma = soma + c
        contador += 1 # O contador vai achar um número multiplo de 3 e contar mais 1
        # contador = contador + 1

print(f'A soma de todos os {contador} valores é {soma}')
# -----------------------FIM----------------------------------------- #
