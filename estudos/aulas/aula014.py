# ------------- ESTRUTURA DE REPETÇÃO (While) ----------------- #
'''for c in range (1, 11):
    print(c)
print('acabou')'''

print('''c = 1 # contador

while c < 11: # quando eu n sei o limite uso while
    print(c)
    c += 1
print('acabou')''')

'''n = 1

while n != 0: # isso e um condição de parada (FLAG)
    n = int(input('Digite um valor:'))
print('cabou')'''

"""r = 'S'
while r == 'S':
    n = int(input('Digite um valor'))
    r = str(input('quer continuar? [S / N] ')).upper()
print('FIM')"""

n = 1
par = impar = 0 # as 2 variaveis são iguais a 0

while n != 0:
    n = int(input('Digite um numero:'))
    if n != 0:
        if n % 2 == 0:
            par += 1 # contador de números pares

        else:
            impar += 1 # contador de números ímpares
print(f'Você digitou {par} números pares e  {impar} números ímpares!!!')
