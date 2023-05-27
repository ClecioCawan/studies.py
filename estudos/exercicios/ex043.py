# ---------------CALCULANDO IMC----------------------------------#
from time import sleep

print('<=>' * 15)
print('CALCULANDO IMC')
print('<=>' * 15)
peso = float(input('Digite o seu peso: (KG) '))

altura = float(input('Digite a sua altura: (M) '))

imc = peso / (altura ** 2)

print(f'O seu indice de massa corporea (IMC) vale {imc:.2f} ')

if imc < 18.5:
    print('VOCÊ ESTA ABAIXO DO PESO IDEAL !!!')
    sleep(2)
    print('CLASSIFICAÇÃO: MAGREZA I')

elif imc >= 18.5 and imc < 25:
    print('VOCÊ ESTA NO PESO IDEAL !!!')
    sleep(2)
    print('CLASSIFICAÇÃO: NORMAL')

elif imc > 25 and imc < 30:
    print('VOCÊ ESTA COM SOBRE PESO !!!')
    sleep(2)
    print('CLASSIFICAÇÃO: SOBRE PESO I')

elif imc > 30 and imc < 40:
    print('VOCÊ ESTA COM OBESO. CUIDI-SE!')
    sleep(2)
    print('CLASSIFICAÇÃO: OBESIDADE I')

elif imc >= 40:
    print('VOCÊ ESTA COM OBESIDADE MÓRBIDA. CUIDADO!')
    sleep(2)
    print('CLASSIFICAÇÃO: OBESIDADE X')
# -----------------------------FIM----------------------------------#
