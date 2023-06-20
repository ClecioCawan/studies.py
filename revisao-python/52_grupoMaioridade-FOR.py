soma_maior = 0#Contador de maiores
soma_menor = 0#contador de menores

for c in range (1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {c}° pessoa: "))
    idade = 2023 - ano_nascimento 

    if idade >= 18:
        soma_maior += 1 #Calculando a soma das idades Maiores de 18

    if idade < 18:
        soma_menor += 1 #Calculando a soma das idades Menores de 18

print(f"Ao todo, {soma_maior} Pessoas MAIORES de 18 anos.")
print(f"E {soma_menor} Pessoas MENORES de 18 anos")
print("FIM DO PROGRAMA!!")
