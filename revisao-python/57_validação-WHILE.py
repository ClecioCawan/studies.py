sexo = input("Digite o seu sexo: [ M / F ]  ").lower().strip()

while sexo != "m" and sexo != "f":
    sexo = input("Dados invalidos. Por favor, digite os dados novamente: ")
print(f"sexo {sexo} Registrado com sucesso.")
#--------------------------------------------------------------------------#
#sexo = input("Digite o seu sexo: [ M / F ] ").lower().strip()

#while sexo not in "mf": o Segredo é o not in (não estiver dentro de)
#    sexo = input("Dados invalidos. Por favor, Digite os dados novamente: ")
#print(f"Sexo {sexo} Registrado com sucesso.")
