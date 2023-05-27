# ---------------OPERADORES ARITIMETICOS-------------#
'''print(
>>> 5+3*2
11
>>> 5**2
25
>>> 5**3
125
>>> 19//2
9
>>> 19%2
1
>>> 19/2
9.5
>>> 4**3
64
>>> pow(4,3)
64
>>> 81**(1/2)
9.0
>>> 81**(1/3)
4.3267487109222245)'''

#n = str(input('Qual e o seu nome:?'))
#print(f'olá {n:=^50}')

n1 = int(input('DIGITE UM VALOR:'))
n2 = int(input('DIGITE outro VALOR:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
rd = n1 % n2
p = n1 ** n2
r1 = n1 ** (1/2)
r2 = n2 ** (1/2)
print('\n')
print(f'''OPERANDO ESSES VALORES:

SOMA = {s}

MULIPLICAÇÃO = {m}

DIVISÃO = {d}

DIVISÃO INTEIRA = {di}

RESTO DA DIVISÃO = {rd}

POTÊNCIA = {p}   

RAIZ DO PRIMEIRO = {r1:.2f}

RAIZ DO SEGUNDO = {r2:.2f}
''')