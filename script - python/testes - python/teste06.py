print('='*50)
cop = float(input('Digite o comprimento do cateto oposto:'))
print('='*50)
cad = float(input('Digite o comprimento do cateto adjacente:'))
print('='*50)
hipo = (cop**2 + cad**2) ** (1/2)
sen = cop / hipo
cos = cad / hipo
tan = cop /cad
print(f' Segundo o valor dado dos dois catetos ({cop} e {cad})...')
print('='*50)
print(f' O valor da sua HIPOTENUSA vale: {hipo:.1f} ')
print('='*50)
print(f' O valor do seu SENO corresponde: {sen:.1f}')
print('='*50)
print(f' O valor do seu COSSENO corresponde: {cos:.1f}')
print('='*50)
print(f' O valor da sua TANGENTE corresponde: {tan:.1f}')
print('='*50)