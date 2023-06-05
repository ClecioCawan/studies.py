nota_1 = float(input("Digite a nota do seu primeiro bimestre: "))
nota_2 = float(input("Digite a nota do seu segundo bimestre: "))
media = (nota_1 + nota_2) / 2

if media >= 7.0:
    print(f"Você foi APROVADO com {media} de média.")

else:
    print(f"Você foi REPROVADO com {media} de média, NÃO conseguiu atingir 7.0 pontos. ")