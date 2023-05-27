d = float(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos quilômetros rodados?'))
d1 = d * 60
km1 = km * 0.15
vt = d1 + km1
print(f'o valor a pagar pelos dias e de R$ {d1:.2f}')
print(f'o valor a pagar pelos km rodados e de R$ {km1:.2f}')
print(f'Total a pagar e de R$ {vt:.2f}')