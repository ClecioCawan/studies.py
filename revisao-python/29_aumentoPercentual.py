nome = str(input("Digite o seu nome: ")).strip()
salario = float(input("Quanto é o seu salário: R$ "))
anos_trabalho = int(input("Por quantos anos você trabalhou: "))

if anos_trabalho <= 3:
    aumento = salario + (salario * 3/100)
    print(f"O seu aumento é de 3% \nSeu salário é de R$ {aumento :.2f}")

elif anos_trabalho > 3 and anos_trabalho <= 10:
    aumento = salario + (salario * 12.5/100)
    print(f"O seu aumento é de 12.5% \nSeu salário é de R${aumento :.2f}")

elif anos_trabalho > 10:
    aumento = salario + (salario * 20/100)
    print(f"O seu aumento é de 20% \nSeu salário é de R${aumento :.2f}")

