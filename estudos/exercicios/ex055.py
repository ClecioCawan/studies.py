# ----------------MAIOR E MENOR EM UMA SEQUÊNCIA---------------------- #
peso_maior = 0 # contador de maior
peso_menor = 0 # contador de menor

for c in range (1, 6):
    peso_pess = float(input(f'Digite o peso da {c} pessoa: '))

    if c == 1: # analizador de maior e menor
        peso_maior = peso_pess
        peso_menor = peso_pess

    elif peso_pess > peso_maior:
        peso_maior = peso_pess
    
    elif peso_pess < peso_menor:
        peso_menor = peso_pess

print(f'A pessoa mais pesada foi {peso_maior}')
print(f'A pessoa menos pesada foi {peso_menor} ')
