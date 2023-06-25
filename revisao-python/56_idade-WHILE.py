continuar = "s"
cont_pessoa = soma_idade = cont_idade = media_idade = cont_maior_21 = 0

while continuar == "s": #Flag de parada
    cont_pessoa += 1 #contador de pessoas
    idade = int(input(f"Digite a idade da PESSOA {cont_pessoa} :  "))
    continuar = input("Quer continuar? [ S / N ] : ").lower().strip()
    soma_idade += idade # soma das idades
    cont_idade += 1 # contador de idades
    media_idade = soma_idade / cont_idade #média das idades

    if idade >= 21:
        cont_maior_21 += 1 #Contador de maiores de 21 anos

print(f"Foram digitadas {cont_idade} Idades.")
print(f"A média entre as idades é de {media_idade} anos.")
print(f"{cont_maior_21} pessoa(s) possue(m) 21 anos ou mais. ")
