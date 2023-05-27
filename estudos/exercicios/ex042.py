a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a == b == c:
    tipo = 'EQUILÁTERO'
elif a == b and a != c or a == c and a != b or b == c and b != a:
    tipo = 'ISÓSCELES'
elif a != b != c:
    tipo = 'ESCALENO'
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo {}'.format(tipo))
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
