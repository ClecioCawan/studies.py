import math
import time
print('-' * 75)
print('!!!CALCULANDO UMA EQUAÇÃO DO SEGUNDO GRAU!!!')
print('-' * 75)
time.sleep(2)
print('''Computer: Utilizando esse programa para calcular uma equação de segundo grau
pela Fórmula de Bhaskara, você deverá colocar o número segundo esta fórmula:
----------------------------------------------------------------------------
==> ax2 + bx + c = 0 <==
----------------------------------------------------------------------------

EXEMPLO:

2x2 + 3x + 1 = 0

Onde:

a = 2
b = 3
c = 1

!!!Entendido isso VAMOS CALCULAR...!!!

----------------------------------------------------------------------------''')
time.sleep(2)
a = int(input('Digite o valor de A:'))
time.sleep(1)
print('''''')
b = int(input('digite o valor de B:'))
time.sleep(1)
print('''''')
c = int(input('Digite o valor de C:'))
time.sleep(3.5)
print('''''')
print('CALCULANDO...')
time.sleep(3.5)
print('''''')
delta = (b**2) -4 * (a * c)
if delta < 1:
    print(f'O valor de DELTA e {delta} , logo NÃO EXISTE!!!')
else:
    print(f'O valor de DELTA e {delta}!!!')
    print('''''')
    x1 = (- b + (math.sqrt(delta))) / (2 * a)
    x2 = (- b - (math.sqrt(delta))) / (2 * a)
    time.sleep(2)
    print(f'O valor de X1 é {x1:.2f}')
    time.sleep(2)
    print('''''')
    print(f'O valor de X2 é {x2:.2f}')
print('OBRIGADO POR USAR O PROGRAMA :)')