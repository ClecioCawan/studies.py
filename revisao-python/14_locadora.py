dias = int(input("Digite o número de dias que utilizou o carro: "))
km = float(input("Digite a quantidade de km percorridos: "))
preco_dia = dias * 90
preco_km = km * 0.20
preco_total = preco_dia + preco_km
print(f'o valor a pagar pelos dias e de R$ {preco_dia:.2f}')
print(f'o valor a pagar pelos km rodados e de R$ {preco_km:.2f}')
print(f'Total a pagar e de R$ {preco_total:.2f}')
