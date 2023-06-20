#Média de idade geral
#homen mais velho
#mulheres menos de 20 anos
soma_idade = 0
maior_idade_homen = 0
mulher_menos_20_anos = 0
cont_nome = ""
for c in range (1, 5):
    print(f"--- PESSOA {c} ---")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M / F): ")).lower().strip()
    #Idade
    soma_idade += idade 
    media_idade = soma_idade / c
    #sexo
    if sexo == "m" and idade > maior_idade_homen:
        maior_idade_homen += 1
        maior_idade_homen = idade    
        cont_nome = nome
    elif sexo == "f" and idade < 20:
        mulher_menos_20_anos += 1
print(f"A média das idades é de {media_idade}")
print(f"O homen mais velho é {cont_nome} com {maior_idade_homen} ")
print(f"Existem {mulher_menos_20_anos} Mulheres com menos de 20 anos")
