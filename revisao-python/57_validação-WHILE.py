erro = ""
sexo = input("Digite o seu sexo: [ M / F ]  ")

if sexo != "m" and sexo != "f":
    while sexo != "m" and sexo != "f":
        erro = input("Dados invalidos. Por favor, digite os dados novamente: ")
    print(f"")
else:
    print(f"sexo {sexo} Registrado com sucesso.")
