idade = int(input("Digite a sua data de nascimento: "))
idade_alistamento = 2023 - idade #Ano atual

if idade_alistamento == 18:
    print(f"Você possui {idade_alistamento} anos, já pode realizar o ALISTAMENTO MILITAR ")

if idade_alistamento > 18:
    anos_maior = idade_alistamento - 18  #Anos que passou
    print(f"Você possui {idade_alistamento} anos, já se passaram {anos_maior} anos para o seu ALISTAMENTO MILITAR ")

else:
    anos_menor = 18 - idade_alistamento #Anos que falta
    print(f"Você possui {idade_alistamento} anos, já NÃO pode realizar o ALISTAMENTO MILITAR, ainda falta {anos_menor} anos")