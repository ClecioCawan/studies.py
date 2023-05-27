# ---------------- SOMA DOS NÚMEROS PARES ---------------------------- #
soma = 0 #Acumulador
cont = 0 # Contador

for c in range (1, 7):

    n_valor = int(input(f'Digite o valor {c}: '))

    if n_valor % 2 == 0: # Se o valor for par: (divisivel(%) por 2)

        soma += n_valor  #Acumulador
        # soma = soma + n_valor
        
        cont += 1 # Contador
        # cont = cont + 1

print(f'VOCÊ DIGITOU {cont} NÚMEROS PARES E A SOMA ENTRE ELES É {soma}') 
