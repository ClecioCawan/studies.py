nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float (input("Digite a segunda nota: "))
media = (nota_1 + nota_2) / 2

if media >= 7.0:
    print(f"Você foi APROVADO, com {media}")

elif media >= 5.0 and media <= 6.9:
    print(f"Você está de RECUPERAÇÃO, com {media}")

elif media <= 4.9:
    print(f"Você foi REPROVADO, com {media}")





