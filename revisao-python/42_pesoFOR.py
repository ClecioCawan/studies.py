contador_mulher = 0
contador_peso_mulher = 0
homen_mais_100kg = 0
maior_peso_homen = 0
#no contador você adiciona com o elemento, se for um somatorio é sempre +1.
for c in range (1, 9):
    print(f"--PESSOA {c}--")
    sexo_pessoa = str(input("Digite o sexo, (M / F), da pessoa : ")).upper().strip()
    peso_pessoa = float(input("Digite o peso, em KG, da pessoa : "))
    
    if sexo_pessoa == "F":
        contador_mulher += 1 #Contador de mulheres (total de mulheres)
        contador_peso_mulher = contador_peso_mulher + peso_pessoa #Contador de peso (total do peso mulheres)
        media_peso_mulher = contador_peso_mulher / contador_mulher

    elif sexo_pessoa == "M" and peso_pessoa > 100:#homen maior que 100kg
        homen_mais_100kg += 1 #Contador de homens com mais de 100kg.

    if sexo_pessoa == "M" and peso_pessoa > maior_peso_homen: #Para encontrar o maior peso entre os homens
        maior_peso_homen = peso_pessoa
#NÃO PODE USAR O "elif" NESSA CONDIÇÃO, é preciso criar um novo aninhamento com o "if".
print("\n---RESULTADOS----")
print(f"Foram cadastradas {contador_mulher} mulheres.")
print(f"A média de peso entre as mulheres é de {media_peso_mulher :.2f}")
print(f"{homen_mais_100kg} homens pesam mais de 100kg.")
print(f"O maior peso entre os homens é de {maior_peso_homen} kg")

    
