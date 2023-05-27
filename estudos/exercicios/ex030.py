# ----------------PAR OU ÍMPAR--------------- #
import time
import os
n = int(input('Digite um número:'))
r = n % 2
time.sleep(1.5)
if r == 0:
    print(f'ESSE NUMERO {n} E PAR')
    time.sleep(1.5)
else:
    print(f'ESSE NUMERO {n} E IMPAR')
# -----------------FIM------------------------- #