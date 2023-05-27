# --------------ANO BBISSEXTO------------------------------------------- #
from datetime import date
a = int(input('Que ano quer analizar? Digite 0 para analisar o ano atual:'))
if a == 0:
    a == date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 ==0:
    print(f'O ano {a} é BISEXTO')
else:
    print('O ano {} não é BISSEXTO!')
# ------------------------------FIM------------------------------------- #