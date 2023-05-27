# -----------RADAR ELETRONICO------------------------------ #
import time
import os
v = float(input('Qual é a velocidade drigida pelo carro?'))
multa = (v - 80) * 7
if v > 80:
    print(f'''!VOCÊ FOI MULTADO! por exeder o limite de 80 km/h
a sua multa será de R$ {multa}''')
else:
    print('! VOCÉ ESTA DENTRO DO LIMITE !')
print('Tenha um bom dia! Dirija com segurança!')
time.sleep(2)
os.system('cls')
# -------------------FIM------------------------------------ #