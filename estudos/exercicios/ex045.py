# --------------------JOKENPÔ--------------------- #
from random import randint

print('''
 #============================#
 #=        JOKENPÔ           =#
 #============================#
''')

print('''BEM - VINDO AO GAME "PEDRA PAPEL E TESOURA"...
PARA JOGAR BASTA ESCOLHER UM NÚMERO CORRESPONDENTE AO
ITEM DESEJADO
''')

print(''''ESCOLHA UM DETERMINADO ITEM!!

[ 1 ] PEDRA 
[ 2 ] PAPEL
[ 3 ] TESOURA''')

print('\n')

userComputer = randint (1,3)
userPlayer = int(input('DIGITE A SUA OPÇÃO:'))

if userPlayer == 1:
    print('você escolheu [ PEDRA ]')

    if userComputer == 1:
     print('O computador escolheu [ PEDRA ]')
     print('!!! EMPATE !!!')

    elif userComputer == 2:
        print('O computador escolheu [ PAPEL ]')
        print('!!! o COMPUTADOR ganhou !!!')
    
    elif userComputer == 3:
        print('O computador escolheu [ TESOURA ]')
        print('!!! VOCÊ GANHOU !!!')
    

if userPlayer == 2:
    print('você escolheu [ PAPEL ]')

    if userComputer == 2:
        print('O computador escolheu [ PAPEL ]')
        print('!!! EMPATE !!!')

    elif userComputer == 1:
        print('O computador escolheu [ PEDRA ]')
        print('!!! VOCÊ GANHOU !!!')
    
    elif userComputer == 3:
        print('O computador escolheu [ TESOURA ]')
        print('!!! o COMPUTADOR ganhou !!!')

if userPlayer == 3:
    print('você escolheu [ TESOURA ]')

    if userComputer == 3:
        print('O computador escolheu [ TESOURA ]')
        print('!!! EMPATE !!!')

    elif userComputer == 1:
        print('O computador escolheu [ PEDRA ]')
        print('!!! o COMPUTADOR ganhou !!!')
    
    elif userComputer == 2:
        print('O computador escolheu [ PAPEL ]')
        print('!!! VOCÊ GANHOU !!!')
        