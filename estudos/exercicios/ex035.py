print('-'*20)
print('ANALISADOR DE TRIÂNGULOS!!!')
print('-'*20)
r1 = float(input('Digite o PRIMEIRO segmento:'))
r2 = float(input('Digite o SEGUNDO segmento:'))
r3 = float(input('Digite o TERCEIRO segmento:'))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print(f'Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print(f'Os segmentos NÃO PODEM FORMAR um triângulo!')