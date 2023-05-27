#----aula014-----------------CALCULO DE FATORIAL--------------------------------#
'''from math import factorial
n1 = int(input('Digite um número para ver o seu fatorial:'))
fatorial = factorial(n1)
print(f'O fatorial de {n1} é {fatorial}.')'''

from math import factorial
from time import sleep

n = int(input('Digite um número para calcular o seu fatorial:'))

fatorial = factorial (n)

contador = n
sleep(1.5)

print(f'CALCULANDO {n}!')
sleep(1.5)

while contador > 0:
    print(f'{contador}', end=' ')
    
    if contador > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')

    contador -= 1

print(fatorial)   
print(f' O fatorial de {n}! é {fatorial}')
#--------------------------------FIM---------------------------------#