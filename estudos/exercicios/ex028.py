# -------------------JOGO DA ADIVINHAÇÃO V.1--------------------------------- #
from random import randint
import os
import time
print('=-='*10)
print('JOGO DA ADVINHAÇÃO')
print('=-='*10)
time.sleep(3)
print('computador: PENSEI EM UM NUMERO...')
time.sleep(3)
numero = int(input('computador: EM QUE NUMERO EU PENSEI:'))
np = randint(0, 5)
print('PROCESSANDO...')
time.sleep(3)
print('.')
time.sleep(1.5)
print('.')
time.sleep(1.5)
if numero == np:
    print(f'computador: !!!PARABÉNS!!!, EU PENSEI NO NÚMERO {np}')
    print('REINICIANDO O GAME...')
    time.sleep(3)
    os.system('cls')    
else:
    print(f'computador: !HAHAHA!!VOCÊ PERDEU!, EU PENSEI NO NÚMERO {np}')
    print('REINICIANDO O GAME...')
    time.sleep(3)
    os.system('cls')
# ----------------------FIM-------------------------------------------------- #