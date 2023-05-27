from math import radians, sin, cos , tan
a = float(input('Digite o âgulo desejado:'))
sin = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print(f'O ângulo {a}, o seu SENO corresponde a {sin:.2f}')
print(f'O ângulo {a}, o seu COSSENO corresponde a {cos:.2f}')
print(f'O ângulo {a}, a sua TANGENTE corresponde a {tan:.2f}')