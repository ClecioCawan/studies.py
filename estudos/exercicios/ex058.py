# ------------------------ JOGO DA ADVINHAÇÃO V.2 --------------------- #
from random import randint
from time import sleep

computador = randint(0, 10)
acertos = False
palpites = 0

print('''
#######################
JOGO DA ADIVINHAÇÃO V.2
#######################''')

sleep(1.5)

print('''
Computador: PENSEI EM UM NÚMERO....
Computador :  SERÁ QUE VOCÊ CONSEGUE ADIVINHAR?''')

while not acertos:
    jogador = int(input('Computador: QUAL SERÁ O SEU PALPITE?'))
    palpites += 1

    if computador == jogador:
       acertos = True
    elif computador < jogador:
        print('MENOS..!')
    elif computador > jogador:
        print('MAIS....')
    sleep(2)
print(f'Parabéns você e um vitorioso!!! teve {palpites} tentativas.')
#-----------------------------------FIM--------------------------------------#