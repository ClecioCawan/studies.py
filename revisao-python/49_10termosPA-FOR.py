termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao dessa P.A: "))
decimo = termo + (10 - 1) * razao #Formúla para calcular o ultimo termo de uma P.A
soma = 0
for c in range (termo, decimo + razao, razao):
    print(c, end= " => ")
    soma += c
print(f"Acabou!\nA soma de todos os termos dessa P.A é de {soma}")
