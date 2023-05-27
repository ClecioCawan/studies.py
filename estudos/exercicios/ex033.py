# ---------MAIOR E MENOR VALOR ------------ #
a =int(input('Digite o primeiro numero:'))
b =int(input('Digite o segundo numero :'))
c =int(input('Digite o terceiro numero:'))
menor = a
# ===menor valor=== #
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# ===maior valor=== #
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O MENOR VALOR DIGITADO É:{menor}')
print(f'O MAIOR VALOR DIGITADO É:{maior}')
# -------------FIM------------------------- #