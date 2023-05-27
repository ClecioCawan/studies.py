from math import hypot
cop = float(input('Diga o comprimento do cateto oposto:'))
cad = float(input('Diga o comprimento do cateto adjacente:'))
hipo = hypot(cop , cad)
print(f'A hipotenusa vale {hipo:.2f}')