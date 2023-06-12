valor_casa = float(input("Digite o valor da casa: R$ "))
salario_comprador = float(input("Digite o valor do salário do comprador: R$ "))
anos_pagar = int(input("Quantos anos você quer pagar: "))
prestacao_mensal = valor_casa / anos_pagar
excesso = (salario_comprador * 30/100)

if prestacao_mensal > excesso:
    print("Você não pode comprar esse imóvel.")
elif prestacao_mensal < excesso:
    print("Você PODE comprar esse imóvel.")
