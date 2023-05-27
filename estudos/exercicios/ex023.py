# ----SEPARANDO DIGITOS DE UM NUMERO--------- #
n = int(input('Imforme um numero interio:'))
m = n // 1000
c = n // 100 %10
d = n //10 % 10
u = n % 10
print(f'Analisando esse numero inteiro {n}:')
print(f'O seu MILHAR  é: {m}')
print(f'A sua CENTENA é: {c}')
print(f'A sua DEZENA  é: {d}')
print(f'A sua UNIDADE é: {u}')
# -------------------FIM---------------------- #