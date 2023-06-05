ano_nacimento = int(input("Digite seu ano de nacimento: "))
idade = 2023 - ano_nacimento

if idade >= 18:
    print(f"Você possui {idade} anos, você pode votar.")

else:
    print(f"Você possui {idade} anos , você ainda NÃO pode votar.")
