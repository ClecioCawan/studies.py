salario = float(input("Digite o salário atual:R$ "))
genero = input("Digite o seu gênero (M / F): ").lower().strip()
anos_trabalhados = int(input("Digite a quantidade de anos trabalhados na empresa: "))

if genero == "m":
    print(f"Seu gênero é MASCULINO")
    if anos_trabalhados <= 20:
        salario_atual = salario + (salario * 3/100)
        print(f"Seu salário sofreu um aumento de 3%, seu salário é de R${salario_atual}")

    elif anos_trabalhados > 20 and anos_trabalhados <= 30:
        salario_atual = salario + (salario * 13/100)
        print(f"Seu salário sofreu um aumento de 13%, seu salário é de R${salario_atual}")
    
    elif anos_trabalhados > 30:
        salario_atual = salario + (salario * 25/100)
        print(f"Seu salário sofreu um aumento de 25%, seu salário é de R${salario_atual}")

elif genero == "f":
    print(f"Seu gênero é FEMININO")
    if anos_trabalhados <= 15:
            salario_atual = salario + (salario * 5/100)
            print(f"Seu salário soreu um aumento de 5%, seu salário é de R${salario_atual}")

    elif anos_trabalhados > 15 and anos_trabalhados <= 20:
        salario_atual = salario + (salario * 12/100)
        print(f"Seu salário sofreu um aumento de 12%, seu salário é de R${salario_atual}")
    
    elif anos_trabalhados > 20:
        salario_atual = salario + (salario * 23/100)
        print(f"Seu salário sofreu um aumento de 23%, seu salário é de R${salario_atual}")



